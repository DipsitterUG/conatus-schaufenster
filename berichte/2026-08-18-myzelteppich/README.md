# Myzelteppich -- Befall als Bodenschicht, vorher und nachher

**Vorgang:** Conatus-Studio#411 · **Entscheidung:** dipsitter-cnc#87, 2026-08-18,
Idee A -- *„Sporen sind Boden, nicht Einheiten"* · **Vorlaeufer:** die Sonde aus
#403 (`berichte/2026-08-18-myzel-sonde/`)

Aufgenommen mit der **installierten Windows-Engine** (Intel Arc, 1600x1000),
nicht in WSL: die Schicht ist reines Rendering, und WSL rendert ueber eine
andere GL-Kette. Karte „Conatus First Map 0.1", Kartenquadrat 2,2 (Elmo
2560,2560). Werkzeug: `tools/conatus_myzel_bild.sh` im Spiel-Repo.

## Die acht Bilder

**Zwei Laeufe, dieselben vier Kameras.** Das „vorher" ist kein frueher Frame,
sondern ein eigener Lauf mit `conatus_myzel=0` -- die Regel laedt sich dann
selbst ab, es ist also garantiert nichts da. Damit ist der Vergleich zugleich
die Sichtprobe zur Rot-Probe des Smokes.

| Datei | Lauf | Was zu sehen ist |
|---|---|---|
| `myzel-aus-01..03` | Regel **aus** | derselbe Blickwinkel, unberuehrter Boden: Gras, Sandbank, See |
| `myzel-aus-04` | Regel **aus** | Draufsicht auf dieselbe Stelle, unberuehrt |
| `myzel-an-01..03` | Regel **an** | der Teppich waechst aus einem Punkt, mit ausgefranstem Rand |
| `myzel-an-04` | Regel **an** | Draufsicht: die Zelle ist zu einem guten Teil ueberwachsen |

Das lohnendste Paar ist `myzel-aus-04` gegen `myzel-an-04`. Dort sieht man auch
die **Grenze dieser Fassung**: die obere Kante des Flecks ist gerade, nicht
ausgefranst. Der Teppich haelt an der Kante des Kartenquadrats an -- eine Zelle
ist 1024 Elmo, und `Spring.SetMapSquareTexture` arbeitet je Quadrat. Ausbreitung
ueber Zellgrenzen ist ein eigener Vorgang, kein Fehler dieses Bildes.

## Warum das „vorher" ein eigener Lauf ist

Zwei Anlaeufe, das erste Bild im selben Lauf **vor** den ersten Wachstumstakt zu
legen, lieferten beide ein „vorher" mit fertigem Fleck:

1. Erster Abzug bei Frame 3 -- der Kameratreiber schoss, **bevor** er die erste
   Kamera gestellt hatte. Das Bild hatte einen anderen Standpunkt als die
   folgenden; ein Vergleich, der nichts vergleicht.
2. Wachstumstakt auf 90 Frames gestellt, Abzug bei Frame 30 -- trotzdem lag ein
   Fleck. Die Frame-Zahlen des Kameratreibers und die Takte des Gadgets sind
   **nicht dieselbe Uhr**.

Der Lauf mit abgeschalteter Regel braucht diese Uhr nicht. Er ist die strengere
Gegenprobe, nicht die bequemere.

## Die Farbe ist ein Platzhalter

Bleiches Knochen-Ocker, entsaettigt, zur Laufzeit gerechnet -- **kein Bild, keine
Textur, kein Fremdmaterial**. Welche Farbe der Befall am Ende hat, entscheidet
der Loremaster, nicht der Builder.

## Was diese Bilder nicht zeigen

- **Kokons.** Sie sind in dieser Fassung Buchhaltung, kein Objekt: nicht
  sichtbar, nicht angreifbar. Dass sie reifen und schluepfen, belegt der
  headless-Smoke mit Zahlen, nicht ein Bild.
- **Die Minimap.** Dort erscheint der Teppich nicht; die Minimap zeichnet eine
  eigene Textur.
- **Die Kosten.** Was die Schicht rechnet, misst
  `tools/conatus_myzel_smoke.sh`, nicht diese Abzuege.

Herkunft: eigene Arbeit (Conatus). Alle Bilder stammen aus der installierten
Windows-Engine dieses Rechners.
