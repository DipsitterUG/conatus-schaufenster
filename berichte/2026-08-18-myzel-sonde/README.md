# Myzelteppich als wachsende Gelaendeschicht — Machbarkeitssonde

Studio#403, Loremaster-Idee A aus cnc#87 (2026-08-17). Stand 2026-08-18.
**Sonde, keine Spielregel.** Ob die Biowaffe so gebaut wird, entscheidet der
Mensch (cnc#87 A/B/C). Hier steht nur, ob es geht und was es kostet.

## Die Frage

Der Vorschlag: die Praesenz der Biowaffe ist **Boden, keine Einheiten** — ein
Myzelteppich, der je Takt am Rand waechst; Kampfeinheiten reifen nur aus Kokons
in Spielernaehe. Begruendung: Recoil skaliert an der **Einheitenzahl**, nicht an
der Flaeche. Am 17.08.2026 ist WSL zweimal an sechs gleichzeitigen Engines mit
je rund 3 GB erstickt — das Rechenbudget ist der Engpass, nicht die Karte.

## Antwort in drei Zahlen (headless, EIN Lauf, 10 min Spielzeit)

| | Ruhe (Frame 1800) | 6 257 Kacheln (Frame 13 500) | 8 657 Kacheln (Frame 18 000) |
|---|---|---|---|
| Einheiten der Biowaffe | 0 | 0 | 0 |
| ms je Sim-Frame | 2,99 | 2,56 | 2,56 |
| RSS der Engine | 3 728 MiB | 3 729 MiB | 3 739 MiB* |

\* die 10 MiB im letzten Abschnitt gehen auf den Vergleichsblock (4 096
Features), nicht auf den Teppich.

**8 657 Kacheln = 554 048 Elmo², rund die halbe Zelle. Kosten in Sim-Zeit: null.
Kosten in Speicher: rund 1 MiB.** Volle Tabelle: `myzel_messung.txt`.

Bildrate am Windows-PC (Intel Arc, 1600x1000, echte Engine), waehrend der
Teppich von 1 auf 10 261 Kacheln waechst: **87 → 101 Bilder/s**, kein Einbruch.
Der Teppich wird additiv gemalt — Zeichenarbeit haengt am **Zuwachs**, nicht an
der bewachsenen Flaeche. Zum Vergleich derselbe Lauf mit vollem Neuaufbau der
Zellentextur je Sekunde (`conatus_myzel_vollbild=1`): 65 → 46-60 Bilder/s.

## Die Bilder

| Datei | Was |
|---|---|
| `myzel-sonde-01-sichttest_01.png` | **Vorher.** Frame 150, eine Kachel. Gleiche Kamera wie 02/03 — die Gegenprobe. |
| `myzel-sonde-02-sichttest_02.png` | Frame 450, 3 061 Kacheln |
| `myzel-sonde-03-sichttest_03.png` | Frame 750, 6 661 Kacheln |
| `myzel-sonde-04-sichttest_04.png` | Frame 1 050, 10 261 Kacheln, Draufsicht auf die ganze Zelle |
| `myzel_fbo_00_basis.png` | Inhalt der Zellentextur direkt nach dem Grundbild-Blit (Diagnose) |
| `myzel_fbo_01_wachstum.png` | Inhalt derselben Textur bei 9 661 Kacheln (Diagnose) |

Alle vier Weltbilder kommen aus der **installierten Windows-Engine**
(`tools/conatus_myzel_bild.sh` → `tools/terrain_sichttest.ps1`), nicht aus WSL.
Karte: Conatus First Map 0.1, Zelle 2,2 (Elmo 2048–3072).

Die Farbe — bleiches Knochen-Ocker — ist ein **Platzhalter der Sonde**, keine
Kanonentscheidung. Der Ton gehoert dem Loremaster.

## Der gewaehlte Weg und die beiden anderen

**Weg 1 — Kachel-Textur je Kartenquadrat** (`Spring.SetMapSquareTexture`).
Gebaut. Ein Kartenquadrat ist genau 1024×1024 Elmos mit 1024×1024 Texeln.
**Null zusaetzliche Draw-Calls** — das Quadrat wird gezeichnet wie vorher, nur
mit einer anderen Textur-ID. Speicher: netto rund 4 MiB je bewachsener Zelle.

**Weg 2 — Ground-Decals.** Alle Decals gehen in **einen** Draw-Call, 192 Byte
je Decal. Zwei harte Hindernisse: die Textur muss im Decal-Atlas liegen (nur
ueber `gamedata/resources.lua`, Lua kann nichts nachtragen) — also eine
Bestellung beim Assetmanager; und der **Spieler kann Decals abschalten**
(`CONFIG(bool, GroundDecals)`). Eine Schicht, die Gegner-Praesenz zeigt, darf
nicht in den Grafikoptionen verschwinden.

**Weg 3 — Feature-Teppich.** Im selben Lauf mitgemessen: 4 096 Features kosten
rund 10 MiB und (bei diesem leichten FeatureDef) keine messbare Sim-Zeit. Der
Killer ist die harte Engine-Grenze **32 000 Features insgesamt** — eine volle
Zelle im 8-Elmo-Raster braeuchte 16 384. Zwei bewachsene Zellen, und die Engine
ist am Anschlag. Genau der Fehler, den Idee A vermeiden will.

**Nicht auf der Minimap.** Weder Weg 1 noch Weg 2 erscheint dort: die Minimap
zeichnet eine eigene Textur aus der SMF-Datei. Wer den Teppich dort sehen will,
braucht zusaetzlich `Spring.SetMapShadingTexture("$minimap", …)`.

## Was diese Sonde NICHT sagt

- Nichts ueber Spielregeln: kein Schaden, kein Bauverbot, keine Bewegungskosten
  auf dem Teppich. Das ist die Entscheidung an cnc#87.
- Nichts ueber Mehrspieler: die Schicht ist **unsynchron** (reines Rendering).
  Das Wachstumsmodell selbst laeuft synchron und ist damit auf allen Rechnern
  gleich — geprueft ist das aber nicht, es lief nur ein Rechner.
- Nichts ueber viele Zellen gleichzeitig: gemessen ist **eine** Zelle.
