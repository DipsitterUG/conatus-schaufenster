# Kontinentfeld: Hoehenmischung und zellenuebergreifende Gewaesser

**Studio#396** (cnc#75), 2026-08-18. Alles hier sind **Datenbilder** aus dem
Kontinentfeld und aus erzeugten Hoehenkarten — kein GL, keine Engine, keine
Sichtprobe. Wie das Gelaende *aussieht*, sagt nur Windows (#16).

Ansage des Menschen (dipsitter-cnc#75): *„Ein **Fluss ueber mehrere Karten**
waere zu wuenschen. Es muss auch nicht so viel Hochland sein — gesunde
Mischung. Kein Vorteil in hohen Karten; die **Differenz zwischen Boden und
Gipfel** macht den Effekt. Die meisten Karten Hoehe > 0 und nur vereinzelte
Hochlandgebirge/hohe Karten, auch da tief schneidende Fluesse; eine **Furt**
waere anspruchsvoll. Auch **Fjorde** und **kartenuebergreifende Seen**."*

## Der Befund in einer Zeile

Ein Fluss war an **jeder** Zellnaht trocken — nicht, weil er im Hochland
endete, sondern weil das Kantenprofil ueberhaupt kein Flussbett kannte.
Gemessen am Alt-Stand: **0 von 18** Flussquerungen lagen unter dem
Wasserspiegel, der tiefste Stuetzpunkt einer Flusskante 33 Elmos darueber.

## Zahlen, Standard-Planet 20260815, 10x10

| Kennzahl | vorher | nachher |
|---|---|---|
| Hochlandzellen (Feldhoehe ≥ 0,62) | **36** von 100 | **9** von 100 |
| Median der Zellhoehe | 0,560 (112 Elmos) | 0,279 (43 Elmos) |
| Zellen mit Wasser | **1** von 100 | **23** von 100 |
| Fluesse / mittlere Laenge | 3 / 4,0 Zellen | 6 / 5,5 Zellen |
| Laeufe, die im Wasser enden | 1 von 3 | **6 von 6** |
| laengster Lauf / davon nass | 5 / 1 Zelle | **9 / 7 Zellen** |
| Flussquerungen mit Wasser an der Naht | **0 von 18** | **34 von 54** |
| `fluss_lage` auf einer Zellecke (Befund F1) | 14 von 18 | **2 von 54** |
| Naht zweier Nachbarn | 0 Rohwerte | **0 Rohwerte** (unveraendert) |

Ueber **50 Planeten x 100 Zellen** gemessen: Meer 10,8 %, Tiefland/Huegel
67,3 %, Bergland 8,8 %, **Hochland 13,1 %** — die Vorgabe war „hoechstens
15 %".

## Bilder

### `kontinentfeld-nachher.png`
Der ganze Kontinent, 400 x 400 Stuetzstellen aus `ContinentField.sample`, also
**mit** Flussbett. Gitter = die 10 x 10 Zellgrenzen, rote Linie = der Flusszug
laut Abflusskarte. Blau ist alles unter 0 Elmo. Gut zu sehen: die Oberlaeufe im
Gebirge (rote Linie ohne Blau) sind tief eingeschnitten, aber **trocken** — ein
Gebirgstal auf 150 Elmos kann den einen Wasserspiegel der Engine nicht
erreichen. Erst im Unterlauf wird die Linie blau, und dann ueber mehrere Zellen.

### `kontinentfeld-grundrelief.png`
Dasselbe aus `basis_sample` — **ohne** Flussbett. Der Vergleich zeigt, was das
Bett am Feld ausmacht und was Grundrelief ist. Diese Trennung ist nicht Kosmetik:
das Hoehenband einer Karte wird aus dem Grundrelief gelegt. Nimmt man das Bett
mit, stuende die Karte zur Haelfte unter Wasser, obwohl nur das Tal nass ist
(an `map_5_0` gemessen: 26,5 % der Flaeche).

### `naht-fluss-map_2_6-map_2_7.png` + `naht-fluss-ausschnitt-2_6-2_7-3x.png`
**Das Kernbild.** Zwei Nachbarzellen, jede einzeln gebaut, ohne dass eine von
der anderen weiss. Gelbe Linie = die gemeinsame Naht. Der Fluss laeuft durch,
und zwar auf demselben Niveau: **0 Rohwerte Differenz** an der Naht, 55 von 385
Nahtpixeln nass. In `map_2_6` ist links der Zufluss (`river_5` muendet in
`river_2`) zu sehen, in `map_2_7` die Einschnuerung — das ist die **Furt**.

### `naht-fluss-map_5_0-map_6_0.png` + `naht-fluss-ausschnitt-3x.png`
Dasselbe an der Kueste (`river_3`, Unterlauf): 285 von 385 Nahtpixeln nass,
Naht 0. Hier laeuft der Fluss durch flaches Kuestenland und wird zur
Flussmuendung breit — das ist der Fjord-/Ria-Fall: ein ertrunkenes Tal.

### `oberlauf-trocken-map_3_2.png`
Die Gegenprobe: derselbe Fluss (`river_3`) im Hochland. Tief eingeschnittenes
Tal, tiefste Stelle deutlich **ueber** 0 Elmo — kein Wasser. Das ist die Regel
und kein Mangel: eine Kerbe, die dort Wasser fuehren sollte, waere ein 150 Elmo
tiefer Schacht.

### `hoehenklassen-vorher-nachher.png`
Die Hoehenmischung als Balken, je 100 Zellen, dieselben Klassengrenzen fuer
beide Staende.

## Was hier NICHT gelungen ist

**Ein abflussloser See ueber mehrere Zellen entsteht auf dem Standard-Planeten
nicht.** Die Mechanik (Seebecken an Senken auf dem Flusslauf) ist gebaut und
greift — 15 Zellen werden erst durch Flussbett und Becken nass, die groesste
zusammenhaengende Wasserflaeche ist 13 Zellen gross. Aber weil jeder Lauf bis
ins Meer durchlaeuft, haengen alle diese Flaechen daran und heissen darum
`meer`, nicht `see`. Ueber 30 Planeten: 0,5 mehrzellige Binnenseen je Planet.

Ausserdem: die Laeufe sind auf Kontinentebene **achsenparallele L-Formen**
(sie verbinden Zellmitten). Auf der einzelnen Karte sieht man das nicht, in der
Uebersicht schon. Eine Glaettung waere ein eigener Zug.

## Verweise

- Vorgang: <https://github.com/DipsitterUG/Conatus-Studio/issues/396>
- Vorgaenger: <https://github.com/DipsitterUG/Conatus-Studio/issues/386>
  (Zellrand, Transferkorridor, erstes Flusswasser) und
  <https://github.com/DipsitterUG/Conatus-Studio/issues/341> (geerbte Geografie)
- Doku: `docs/worldgen/kontinentfeld.md`, Abschnitt „Hoehenmischung und
  Gewaesser"

Herkunft: Eigenarbeit. Kein fremdes Bildmaterial, keine fremden Daten; alle
Bilder aus Zahlen dieses Projekts erzeugt.
