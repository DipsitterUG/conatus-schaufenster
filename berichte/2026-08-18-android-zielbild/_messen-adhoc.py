#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Messung und Boegen fuer die Android-Zielbilder (Studio#418, Stufe 0).

Ad-hoc, wie beim Leitbaum (#349), beim Lager (#363) und beim Nadelbaum (#397):
Regel 8 des Bauplan-Verfahrens sagt seit dem Erstlauf, dass `zielbild-messen`
und `vergleichsbogen` Studio-Verben werden sollen. Das ist die VIERTE Kopie.
Sie steht hier nur, damit die Zahlen nachstellbar sind.

Was gemessen wird:
  1. Die drei Ansichten je Bild werden ueber weisse Spalten getrennt.
  2. Je Ansicht Breite/Hoehe der Silhouette -- Regel 5: ob drei Ansichten
     dasselbe Objekt zeigen, wird NACHGEMESSEN, nicht behauptet. Ein echtes
     gedrehtes Mesh nimmt von Front ueber 45 Grad zur Seite in der Breite ab
     oder bleibt gleich; springt die Hoehe, war es kein Objekt.
  3. Heller Plattenanteil gegen dunklen Unterbau -- die Achse der drei
     Lesarten (wie viel Panzerung).
  4. Silhouetten-Deckung auf Spielentfernung.

Drei Boegen:
  stil-ABC-bogen.png     A | B | C nebeneinander (die Frontansichten)
  massstab.png           A | B | C auf gemeinsamer Elmo-Skala, mit den
                         belegten Hoehenlinien der Nachbarn
  silhouetten-probe.png  Umriss auf Spielentfernung, plus 6x Lupe
"""

import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HIER = Path(__file__).resolve().parent
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

KANDIDATEN = [
    ("A", "Arbeiter-Chassis", "android-A-arbeiter-chassis.png"),
    ("B", "Sicherungs-Chassis", "android-B-sicherungs-chassis.png"),
    ("C", "Rahmenlaeufer", "android-C-rahmenlaeufer.png"),
]

#: Nennhoehe des Leichten Androiden, Vorschlag dieses Zugs. Herleitung im
#: README (roboterlight.s3o misst 18.64 Elmo, BAR-armpw.s3o 26.02).
NENNHOEHE_ELMO = 20.0

#: px je Elmo der Silhouettenprobe. Dieselbe Skala wie die Nadelbaum-Probe
#: (42 Elmo -> 56 px), damit beide Proben vergleichbar sind.
PX_JE_ELMO = 56.0 / 42.0

#: Belegte Nachbarhoehen in Elmo -- alle im README mit Datei:Zeile.
NACHBARN = [
    (18.64, "Grunt heute (roboterlight.s3o)"),
    (26.02, "BAR-armpw.s3o (nicht geladen)"),
    (36.00, "Leitbaum"),
]

#: Ab hier gilt ein Pixel als Objekt statt als weisser Grund.
GRUND_SCHWELLE = 238
#: Ab hier gilt ein Objektpixel als helle Panzerplatte.
HELL_SCHWELLE = 150


def maske(bild):
    """True, wo ein Objekt steht (nicht weisser Grund)."""
    grau = np.asarray(bild.convert("L"), dtype=np.int16)
    return grau < GRUND_SCHWELLE


def spalten_bloecke(m, mindestluecke=25, mindestbreite=60):
    """Die drei Ansichten anhand leerer Spalten trennen."""
    belegt = m.any(axis=0)
    bloecke, start = [], None
    leer = 0
    for x, b in enumerate(belegt):
        if b:
            if start is None:
                start = x
            leer = 0
        else:
            if start is not None:
                leer += 1
                if leer >= mindestluecke:
                    bloecke.append((start, x - leer + 1))
                    start = None
    if start is not None:
        bloecke.append((start, len(belegt)))
    return [(a, b) for a, b in bloecke if b - a >= mindestbreite]


def freistellen(bild, m, x0=None, x1=None):
    """Zuschnitt auf die Silhouette; gibt Bild + Maske zurueck."""
    if x0 is not None:
        m = m[:, x0:x1]
        bild = bild.crop((x0, 0, x1, bild.height))
    zeilen = np.where(m.any(axis=1))[0]
    spalten = np.where(m.any(axis=0))[0]
    o, u = int(zeilen[0]), int(zeilen[-1]) + 1
    l, r = int(spalten[0]), int(spalten[-1]) + 1
    return bild.crop((l, o, r, u)), m[o:u, l:r]


def auf_hoehe(bild, hoehe):
    breite = max(1, round(bild.width * hoehe / bild.height))
    return bild.resize((breite, hoehe), Image.LANCZOS)


def beschriften(bild, zeilen, groesse=22, rand=10):
    """Textstreifen unter ein Bild setzen."""
    font = ImageFont.truetype(FONT, groesse)
    hoehe = groesse + 6
    neu = Image.new("RGB", (bild.width, bild.height + hoehe * len(zeilen) + rand),
                    "white")
    neu.paste(bild.convert("RGB"), (0, 0))
    d = ImageDraw.Draw(neu)
    for i, (text, farbe) in enumerate(zeilen):
        breite = d.textlength(text, font=font)
        d.text(((bild.width - breite) / 2, bild.height + rand // 2 + i * hoehe),
               text, font=font, fill=farbe)
    return neu


def main():
    werte = {}
    fronten, ganze = {}, {}

    for kuerzel, name, datei in KANDIDATEN:
        bild = Image.open(HIER / datei)
        m = maske(bild)
        bloecke = spalten_bloecke(m)
        ansichten = []
        for x0, x1 in bloecke:
            teil, tm = freistellen(bild, m, x0, x1)
            grau = np.asarray(teil.convert("L"))[tm]
            ansichten.append({
                "x": [x0, x1],
                "breite": teil.width,
                "hoehe": teil.height,
                "b_zu_h": round(teil.width / teil.height, 3),
                "fuellgrad": round(float(tm.mean()), 3),
                "objektpixel": int(tm.sum()),
                "median_helligkeit": int(np.median(grau)),
                "anteil_hell": round(float((grau >= HELL_SCHWELLE).mean()), 3),
                "anteil_dunkel": round(float((grau < 90).mean()), 3),
            })
        hoehen = [a["hoehe"] for a in ansichten]
        werte[kuerzel] = {
            "name": name, "datei": datei,
            "ansichten_gefunden": len(bloecke),
            "hoehenstreuung": round((max(hoehen) - min(hoehen)) / max(hoehen), 4)
            if hoehen else None,
            "objektpixel_gesamt": sum(a["objektpixel"] for a in ansichten),
            "ansichten": ansichten,
        }
        if bloecke:
            x0, x1 = bloecke[0]
            fronten[kuerzel], _ = freistellen(bild, m, x0, x1)
        ganz, _ = freistellen(bild, m)
        ganze[kuerzel] = ganz

    # --- Bogen 1: die drei Turnarounds untereinander --------------------
    zielbreite = 1180
    teile = []
    for kuerzel, name, _ in KANDIDATEN:
        b = ganze[kuerzel]
        b = b.resize((zielbreite, round(b.height * zielbreite / b.width)),
                     Image.LANCZOS)
        teile.append(beschriften(b, [(f"{kuerzel} — {name}"
                                      "   (Front | 45° | Seite)", "black")],
                                 groesse=26))
    hoehe = sum(t.height + 16 for t in teile) + 16
    bogen = Image.new("RGB", (zielbreite + 32, hoehe), "white")
    y = 16
    for t in teile:
        bogen.paste(t, (16, y))
        y += t.height + 16
    bogen.save(HIER / "stil-ABC-bogen.png")

    # --- Bogen 2: Massstab auf gemeinsamer Elmo-Skala -------------------
    px_je_elmo_gross = 22.0
    hoehe_bild = round(40.0 * px_je_elmo_gross) + 90
    spalte = 300
    mass = Image.new("RGB", (spalte * 3 + 520, hoehe_bild), "white")
    d = ImageDraw.Draw(mass)
    font_klein = ImageFont.truetype(FONT, 19)
    font_gross = ImageFont.truetype(FONT, 26)
    boden = hoehe_bild - 60
    for elmo, text in NACHBARN:
        y = boden - round(elmo * px_je_elmo_gross)
        d.line([(20, y), (mass.width - 20, y)], fill=(190, 190, 190), width=2)
        d.text((mass.width - 500, y - 24), f"{elmo:.1f} Elmo — {text}",
               font=font_klein, fill=(110, 110, 110))
    y_ziel = boden - round(NENNHOEHE_ELMO * px_je_elmo_gross)
    d.line([(20, y_ziel), (mass.width - 20, y_ziel)], fill=(200, 120, 0), width=3)
    d.text((mass.width - 500, y_ziel - 26),
           f"{NENNHOEHE_ELMO:.0f} Elmo — Vorschlag Leichter Android",
           font=font_klein, fill=(200, 120, 0))
    d.line([(20, boden), (mass.width - 20, boden)], fill=(60, 60, 60), width=2)
    for i, (kuerzel, name, _) in enumerate(KANDIDATEN):
        f = auf_hoehe(fronten[kuerzel], boden - y_ziel)
        x = 40 + i * spalte + (spalte - f.width) // 2
        mass.paste(f.convert("RGB"), (x, y_ziel))
        breite = d.textlength(kuerzel, font=font_gross)
        d.text((40 + i * spalte + (spalte - breite) / 2, boden + 14), kuerzel,
               font=font_gross, fill="black")
    mass.save(HIER / "massstab-neben-dem-grunt.png")

    # --- Bogen 3: Silhouettenprobe auf Spielentfernung ------------------
    klein_h = max(4, round(NENNHOEHE_ELMO * PX_JE_ELMO))
    lupe = 6
    spalte3 = 330
    probe = Image.new("RGB", (spalte3 * 3 + 40, klein_h * lupe + 150), "white")
    d3 = ImageDraw.Draw(probe)
    font3 = ImageFont.truetype(FONT, 20)
    for i, (kuerzel, name, _) in enumerate(KANDIDATEN):
        f = auf_hoehe(fronten[kuerzel], klein_h)
        fm = np.asarray(f.convert("L")) < GRUND_SCHWELLE
        deckung = float(fm.mean())
        werte[kuerzel]["silhouette_klein"] = {
            "hoehe_px": klein_h, "breite_px": f.width,
            "b_zu_h": round(f.width / klein_h, 3),
            "deckung": round(deckung, 3),
        }
        umriss = Image.fromarray(np.where(fm, 30, 255).astype(np.uint8))
        gross = umriss.resize((f.width * lupe, klein_h * lupe), Image.NEAREST)
        # Umriss links, das echte verkleinerte Bild rechts daneben -- was der
        # Spieler sieht, ist nicht der Umriss allein.
        echt = f.convert("RGB").resize((f.width * lupe, klein_h * lupe),
                                       Image.NEAREST)
        paar = Image.new("RGB", (gross.width * 2 + 14, gross.height), "white")
        paar.paste(gross.convert("RGB"), (0, 0))
        paar.paste(echt, (gross.width + 14, 0))
        x = 20 + i * spalte3 + (spalte3 - paar.width) // 2
        probe.paste(paar, (x, 40))
        probe.paste(f.convert("RGB"),
                    (20 + i * spalte3 + spalte3 // 2 - f.width // 2, 10))
        for j, txt in enumerate([f"{kuerzel} — {name}",
                                 f"{f.width}x{klein_h} px, Deckung {deckung*100:.0f} %"]):
            b = d3.textlength(txt, font=font3)
            d3.text((20 + i * spalte3 + (spalte3 - b) / 2,
                     60 + klein_h * lupe + j * 26), txt, font=font3, fill="black")
    d3.text((20, probe.height - 26),
            f"oben: echte Groesse ({klein_h} px bei {NENNHOEHE_ELMO:.0f} Elmo, "
            f"{PX_JE_ELMO:.3f} px/Elmo wie die Nadelbaum-Probe) · darunter {lupe}x",
            font=ImageFont.truetype(FONT, 17), fill=(110, 110, 110))
    probe.save(HIER / "silhouetten-probe.png")

    (HIER / "messwerte.json").write_text(
        json.dumps(werte, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(werte, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
