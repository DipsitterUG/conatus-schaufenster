# Myzelteppich Stufe 2 im Spiel — Windows-Abzuege (Studio#423)

**2026-08-20, Abnahme-Helfer.** Echte Windows-Engine
(`tools/conatus_myzel_bild.sh` → `tools/terrain_sichttest.ps1`, Fenster
ausserhalb des Bildschirms), Karte „Conatus First Map 0.1", Zelle 2,2,
Herd 2560/2560. Ein Lauf, vier Standpunkte, Zeitraffer.

Diese Bilder ersetzen die vom 18.08. in `2026-08-18-myzel-stufe2/`: die waren
**vor** der Kacheltextur aus #416 und zeigten die Oberflaeche nicht.

## Was im Lauf passiert ist (aus dem Infolog)

| Frame | Ereignis |
|---:|---|
| 0 | Zeichenschicht aktiv, Kachelbild `Metal022` gebunden, erster Myzelknoten |
| 500 | zwei Knoten getrennt (derselbe Callin wie ein Waffentreffer) → **1301 Kacheln trocken** |
| 900 | Sanierer gesetzt (Reichweite 700) |
| 1845 | Ende: 15980/16384 Kacheln, **abgetragen 1200**, **wieder befallen 800**, 5 lebende Knoten, 1 Kokon |

## Uebersicht (Kamera 1500 elmo)

| | |
|---|---|
| ![01](https://raw.githubusercontent.com/DipsitterUG/conatus-schaufenster/main/berichte/2026-08-20-myzel-stufe2-windows/uebersicht-01.png) | **Frame 30** — der Teppich beginnt |
| ![02](https://raw.githubusercontent.com/DipsitterUG/conatus-schaufenster/main/berichte/2026-08-20-myzel-stufe2-windows/uebersicht-02.png) | **Frame 630** — kurz nach dem Trennen, 1301 Kacheln sind trocken |
| ![03](https://raw.githubusercontent.com/DipsitterUG/conatus-schaufenster/main/berichte/2026-08-20-myzel-stufe2-windows/uebersicht-03.png) | **Frame 1230** — der Sanierer (Mitte) hat eine Bahn freigeraeumt |
| ![04](https://raw.githubusercontent.com/DipsitterUG/conatus-schaufenster/main/berichte/2026-08-20-myzel-stufe2-windows/uebersicht-04.png) | **Frame 1830** — der Herd holt sich zurueck, was gereinigt wurde |

## Nahsicht (Kamera 650 elmo), gleiche Frames

`nah-01.png` … `nah-04.png` — dieselbe Folge aus der Hoehe, aus der ein
Spieler seine Einheiten fuehrt.

## Was diese Bilder NICHT zeigen

Die drei Kachelstufen (Rand duenn / Kern dicht / trocken) sind hier **nicht
auseinanderzuhalten** — weder in der Uebersicht noch in der Nahsicht, obwohl
im selben Frame 1301 Kacheln als trocken gebucht waren. Die Myzelknoten sind
Platzhalter (Kenney-Findlinge) und gehen in der Flaeche unter.
Funktional ist alles belegt (`conatus_myzel_rueckbau_smoke.sh` 9 Punkte + 2
Rot-Proben, `conatus_myzel_smoke.sh` 3/3 + Kostentor); sichtbar ist davon
wenig.
