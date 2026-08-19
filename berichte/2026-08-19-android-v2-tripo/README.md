# Leichter Android **V2** aus dem animierten Tripo-Modell — Turnaround (Studio#428, cnc#113)

> ⚠ **Kein Sichttest.** Alles hier ist Blender/EEVEE unter WSL, gerendert aus
> den **fertig zerlegten Pieces** mit der ausgelieferten
> `android_leicht_v2_atlas.png`. Sichttests zaehlen nur unter Windows und in
> der Engine (CLAUDE.md). Diese Bilder sind eine **Entscheidungshilfe**: lohnt
> sich der Windows-Lauf.

## Was hier neu ist gegenueber V1 (`../2026-08-19-android-tripo/`)

Das ist ein **anderes Modell**, nicht dasselbe noch einmal: zweite Lieferung
des Menschen, diesmal **geskinnt und animiert** (41 Joints, drei Clips).
Daraus folgt alles Sichtbare:

* **Es traegt keine Waffe.** V1 hatte ein eigenes `Machine_Gun`-Piece; hier
  gibt es nur den Abschusspunkt `Gun_Muzzle` an den Fingerspitzen rechts.
* **Es steht in der T-Pose.** Das ist Absicht: die Ruhelage des S3O muss die
  Rest-Pose des Rigs sein, sonst kann die Animation aus Studio#429 nicht
  dagegen rechnen. Im Spiel legt das Unit-Skript die Arme an — bis #429 da
  ist, steht die Einheit mit ausgestreckten Armen da. **Kein Fehler.**
* **Es ist schlanker**: Rumpf 5.45 × 3.55 Elmo gegen 7.06 × 7.17 bei V1.

| Bild | was |
|---|---|
| `android-v2-turnaround.png` | **Front / Seite / Ruecken / 45° nebeneinander** |
| `android-v2-front.png` | Front — Visierschlitz und Brustschale |
| `android-v2-seite.png` | Seite (von der **rechten** Koerperseite) |
| `android-v2-ruecken.png` | Ruecken |
| `android-v2-dreiviertel.png` | 45° |
| `android-v2-bauvorschau.png` | dasselbe als `unitpics/android_leicht_v2.png` |
| `android-v2-kontaktbogen.png` | **44 Einzelrenders**: jedes Tripo-Teil rot auf grauem Modell, Front + Seite |

## Worauf zu achten ist

Zu sehen sind: **gelber Visierschlitz**, helle Brustschale, helle
Schienbeinplatten, gelbe Gelenkpunkte an Ellbogen und Knien. Alles sitzt auf
dem Bauteil, auf das es gehoert — das ist zugleich die Sichtprobe darauf, dass
die Zerlegung in 15 Pieces nichts verschoben hat: kein Spalt an Huefte, Knie,
Schulter oder Hals, keine Naht, die im falschen Glied haengt.

Der **Kontaktbogen** ist die zweite Haelfte dieser Probe. Jedes der 44
Tripo-Teile ist dort einzeln rot eingefaerbt — so laesst sich nachsehen, ob
`tripo_part_7` wirklich der Beckenblock ist und `tripo_part_18/19` wirklich
die beiden Hueftbleche. Die Zuordnung selbst kommt aus den **Skin-Gewichten**,
nicht aus dem Augenmass; der Bogen ist die Gegenprobe, nicht die Quelle.

## ⚠ Zwei Fallen, die beide zu einem falschen „Textur kaputt" fuehren

Beide sind beim Bauen dieser Bilder aufgetreten und stehen jetzt als
Kommentar im Bauskript:

1. **Alpha ist die Teamfarben-Maske, kein Deckungsgrad.** 94.6 % der Texel
   haben `alpha = 0`. Blender multipliziert RGB standardmaessig mit Alpha —
   das Modell wird in der Vorschau **schwarz**, obwohl die Datei stimmt.
   Gegenmittel: `image.alpha_mode = "CHANNEL_PACKED"` und im Material **nur**
   die Farbausgabe verdrahten. (Derselbe Fehlalarm wie am 2026-08-19 bei V1.)
2. **Die Datei liegt vertikal gespiegelt auf der Platte** — das ist die
   Engine-Konvention dieses Projekts. Wer sie mit den rohen UVs anschaut,
   sieht ein **zerwuerfeltes** Modell aus weissen und schwarzen Flecken. Die
   Vorschau muss `v` zuruecknehmen. Auch das ist erst passiert, dann behoben.

## Herkunft

**Tripo AI, bezahltes Konto des Menschen, geliefert ueber cnc#113 — Eigentum
Dipsitter** (`origin = commissioned`). Kein Byte aus BAR, Recoil oder einem
Sample-Projekt; deshalb **kein `BAR-`-Praefix**. Der Nachweis haengt als
`.herkunft.json` an jeder ausgelieferten Datei.

Bauweg und alle Zahlen:
`conatus-studio/docs/assets/bauplaene/android-leicht-v2-tripo.md`.

---

# Nachtrag Studio#432: die Loecher, die man erst im Spiel sah

Der Mensch hat V2 im Spiel gesehen (cnc#114) und **zwei** Dinge gemeldet:
eine **Luecke am Hals** waehrend der Animation — und dass man **vom Kopf aus
durch die Unterseite auf den Boden schaut**.

Beides ist in den Bildern oben nicht zu sehen, und das hat einen Grund:

* die **Strichfiguren** von #429 haben weder Haut noch Rueckseiten;
* die **texturierten Ansichten** von #428 sind ohne Backface-Culling
  gerendert. Blender zeichnet Rueckseiten mit, die Engine nicht. Ein offenes
  Netz sieht in Blender geschlossen aus.

Die Bilder in diesem Nachtrag sind deshalb **mit Culling** gerendert, aus den
**echten S3O-Pieces** in den Posen, die das erzeugte Lua-Skript aufbaut
(`tools/blender/anim_lua_vorschau.py --art pieces`).

| Bild | was |
|---|---|
| `anim-pieces-kopf-unten-vorher.png` | **das Kopf-Piece allein, von unten** — man sieht glatt hindurch. Das ist der Befund des Menschen, isoliert. |
| `anim-pieces-kopf-unten-nachher.png` | dasselbe nach dem Deckeln: geschlossen |
| `anim-pieces-death-hals-vorher.png` | Tot-Clip bei t = 1.54 s: Kopf loest sich sichtbar vom Kragen, dazwischen schwarzes Nichts |
| `anim-pieces-death-hals-nachher.png` | dasselbe mit Deckel und neuem Kopf-Pivot |
| `anim-pieces-bow-hals-vorher.png` | Verbeugen bei t = 3.04 s, von hinten |
| `anim-pieces-bow-hals-nachher.png` | dasselbe danach |

## Was gemessen wurde (nicht geschaetzt)

**Die Tripo-Teile sind keine geschlossenen Koerper.** 332 offene Kanten im
ganzen Modell, davon 46 am Kopf: eine Randschleife am Halsschnitt (6.6 Elmo
Umfang) und eine oben im Helm (13.9 Elmo). Der Kragen (`tripo_part_8`) traegt
die Gegenseite desselben Schnitts. Nach dem Deckeln: **332 → 4** Randkanten,
und die vier bilden keinen Kreis, umschliessen also keine Flaeche. Preis:
**+235 Dreiecke** (5103 → 5338, +4.6 %).

**Die Halsluecke ist etwas anderes** und laesst sich nicht schliessen, nur
verkleinern. Kopf und Kragen teilen sich 136 deckungsgleiche Punkte; drehen
sich die beiden starren Pieces gegeneinander, reissen die auseinander. Der
Abstand haengt allein am **Pivot** (nicht am Leitjoint — die drei Halsjoints
drehen sich in diesem Rig identisch). Groesster Spalt in Elmo:

| Kopf-Pivot | walk | death | bow |
|---|---:|---:|---:|
| Gelenkkopf `NeckTwist01` (Stand #428) | 0.94 | 1.80 | 0.95 |
| **Mitte des Halsschnitts (jetzt)** | **0.58** | **1.41** | **0.57** |
| das gelieferte Modell selbst, echte Skin-Verformung | 0.72 | **1.29** | 0.72 |

Die letzte Zeile ist die Untergrenze: **das Original reisst an derselben Naht
selbst um 1.29 Elmo auf.** Ein Spalt „unter 0.3 Elmo" ist an diesem Modell
nicht zu haben — dafuer muesste die Geometrie am Hals anders geschnitten sein.

> ⚠ **Kein Sichttest.** Blender/EEVEE unter WSL. Ob es im Spiel jetzt gut
> aussieht, sieht nur der Mensch unter Windows.

---

# Nachtrag 2026-08-20: **jetzt mit Sichttest** (Abnahme-Helfer)

Ueber diesem Nachtrag steht zweimal „⚠ Kein Sichttest — Blender/EEVEE unter
WSL". Das gilt fuer die Bilder darueber weiter. Die beiden hier sind **anders**:
Windows-Engine, echter Renderer, Spielbaum `ConatusV0` auf `6c393d4` — also
**mit** den gedeckelten Netzen und dem neuen Kopf-Pivot aus Studio#432.

| Bild | was |
|---|---|
| `windows-v1-gegen-v2.png` | **A/B/C**: V1 · V2 stehend · V2 mitten im Verbeugen — gleiche Karte, gleiche Kamera (60 Elmo, 62°), gleicher Ausschnitt |
| `windows-v2-idle-phasen.png` | die Ruhelage ueber 270 Frames: steht, steht, kippt, liegt |
| `windows-v2-kopf-von-oben.png` | Kamera **8°** und **25°** von der Senkrechten — der Kopf von oben |

**Was die Phasenreihe zeigt.** Der Idle-Wechsel aus #429 laeuft im Spiel: die
Einheit steht bei Frame 60 und 150 aufrecht, kippt bei 240 nach vorn und liegt
bei 330 flach auf dem Boden. Das Umfallen ist also **kein Einfrieren und kein
Absturz** — es ist der Clip.

**Was der A/B/C-Bogen zeigt** — drei Unterschiede zu V1, alle sichtbar, keiner
gemessen:

1. **V2 traegt keine Waffe.** Bei V1 liegt das Gewehr in beiden Haenden, bei V2
   sind die Haende leer. Das ist bekannt (nur `Gun_Muzzle`, kein
   `Machine_Gun`-Piece) — im echten Renderer faellt es deutlicher auf als in
   der Blender-Ansicht.
2. **Die Teamfarbe traegt viel mehr Flaeche.** Bei V1 ist Blau auf die
   Schultern begrenzt, bei V2 nimmt es den ganzen Brustpanzer ein. In der
   verbeugten Haltung (C) ist von oben fast nur noch Blau zu sehen.
3. **Der Umriss ist schmaler und laenger**, mit sichtbar duenneren Armen.

**Der Durchblick von oben in den Kopf** — der zweite Befund des Menschen aus
cnc#114 — braucht eine eigene Kamera: die beiden Bilder oben stehen 62° von der
Senkrechten, also fast waagerecht, und sehen den Kopf nie von oben. Dafuer ist
`windows-v2-kopf-von-oben.png` da: 8° und 25° von der Senkrechten, fast
Draufsicht. **Der Helm ist geschlossen, kein Boden durch den Kopf.** Das ist der
Sichtbeleg dafuer, dass das Deckeln aus #432 auch in der Engine ankommt — in
Blender war es nicht zu sehen, weil dort ohne Backface-Culling gerendert wurde.

> Diese zwei Bilder sind ein **Sichtbeleg**, kein Waechter. Ob es *gefaellt*,
> entscheidet nur der Mensch; die Punkte 1 und 2 sind das, was ich ihm dafuer
> hinlege.
