# Myzelteppich Stufe 2 -- lebendiger, tiefer, und wieder abtragbar

**Vorgang:** Conatus-Studio#423 · **Ansage:** dipsitter-cnc#104, 2026-08-18 --
*„ist schon cool. Lebendiger: Pilze, seltsame Gebilde, Geflechte … mir fehlt
noch Tiefe … laesst sich das rueckgaengig machen, das Land ‚reinigen'?"* ·
**Regel dahinter:** Loremaster-Notiz
`conatus-studio/docs/lore/myzel-rueckbau-2026-08-18.md`, Empfehlung c
(gestaffelt), Vorentscheidungen E-M1..E-M4 · **Vorlaeufer:** Stufe 1 in
`berichte/2026-08-18-myzelteppich/`

Aufgenommen mit der **installierten Windows-Engine** (1600x1000), nicht in WSL:
die Schicht ist reines Rendering, und WSL rendert ueber eine andere GL-Kette.
Probekarte **„Conatus Mapserver Probe 0.1"** -- 2048x2048 Elmo, also 4x4
Map-Units, die kleinste Karte im Bestand. Herd in Elmo 1536,1536
(Kartenquadrat 1,1). Werkzeug: `tools/conatus_myzel_bild.sh` im Spiel-Repo,
mit `CONATUS_MYZEL_BILD_RUECKBAU=1`.

## Die acht Bilder

**Zwei Laeufe, dieselbe Kamera viermal** (1536,1536, Hoehe 850, 18 Grad
Neigung). Das „vorher" ist kein frueher Frame, sondern ein eigener Lauf mit
`conatus_myzel=0`: die Regel laedt sich dann selbst ab, es ist also garantiert
nichts da.

| Datei | Frame | Was zu sehen ist |
|---|---|---|
| `01-vorher-regel-aus-01..04` | 400 / 900 / 1400 / 1900 | derselbe Blick, unberuehrter Boden. Vier gleiche Bilder -- das ist der Zweck |
| `02-nachher-stufe2-01` | 400 | der Teppich waechst. **Rand duenn, Kern dicht**; dazwischen die grauen **Myzelknoten** |
| `02-nachher-stufe2-02` | 900 | alle Knoten sind **getrennt** -- die Flaeche liegt als helle, rissige **Kruste** da. Sie verschwindet nicht |
| `02-nachher-stufe2-03` | 1400 | der **Sanierer** (Kasten in der Mitte) traegt ab: um ihn herum liegt wieder Boden |
| `02-nachher-stufe2-04` | 1900 | mehr Boden. Der Herd in der Mitte lebt weiter und legt neue Knoten an |

Das lohnendste Paar ist **`02` gegen `03`**: dieselbe Flaeche, einmal als
Kruste, einmal abgetragen. Der Sprung dazwischen ist der ganze Vorgang.

## Was die Bilder ausdruecklich NICHT zeigen

- **Kein Tempo.** Die Bilderfolge ist ein Zeitraffer: Wachstum 300 Kacheln je
  Takt statt 16, Sanierung 400 statt 40, Arbeitsradius 700 statt 256 Elmo.
  Sonst braeuchte eine Folge dieser Art zwanzig Minuten Spielzeit. Wer Zahlen
  pruefen will, nimmt `tools/conatus_myzel_rueckbau_smoke.sh` -- der faehrt
  die Vorgabewerte.
- **Kein fertiges Aussehen.** Die Myzelknoten sind **Platzhalter**
  (`boulder-01/03/05.s3o`, Kenney Survival Kit, CC0, seit Projektbeginn im
  Repo), der Sanierer ebenfalls (`Units/lager-3x3.s3o` aus der eigenen
  Assetfabrik). Die eigenen Modelle -- verdickte Strangkreuzung mit
  Sporentraegern, Sanierer im industriellen Register -- sind beim
  assetmanager **bestellt, nicht gebaut**.
- **Kein Farbbefund fuer alle Karten.** Diese Probekarte hat ein warmes
  Bodenlicht und grosse dunkle Gesteinsflaechen; die Kruste liest sich darauf
  waermer, als sie in der Textur ist (dort ist sie entsaettigt, R und B liegen
  0,05 auseinander). Auf einer kuehlen Karte sieht dieselbe Stufe anders aus.
- **Die Kachelkante ist echt.** Eine Kachel ist 8 Elmo; die abgetragene Flaeche
  hat darum eine treppige Kante. Das ist die Aufloesung der Regel, kein
  Zeichenfehler.

## Zwei Dinge, die der erste Abzug am selben Tag gezeigt hat

1. **Der Rand war zu duenn.** Mit einer Deckung von 0,28..0,50 zerfiel er ueber
   dunklem Boden in ein sichtbares Kachelraster, statt auszulaufen -- der
   Ueberstand benachbarter Kacheln deckte einander nicht mehr. Jetzt 0,45..0,67,
   der Kern 0,62..0,92. Duenner als der Kern bleibt er deutlich.
2. **Der Riss lag immer waagerecht.** Das las sich als Zeilenmuster, nicht als
   aufgeplatzter Beton. Jetzt entscheidet der Streuwert der Kachel auch die
   Richtung.

Beides steht so im Quelltext (`LuaRules/Gadgets/conatus_myzel.lua`,
`kachelZeichnen`) -- samt Grund, damit es niemand versehentlich zurueckdreht.
