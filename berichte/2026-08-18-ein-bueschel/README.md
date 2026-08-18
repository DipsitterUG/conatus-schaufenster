# Ein-Bueschel-Laubbaum nachgebessert — vorher / nachher (Studio#419)

**Anlass:** dein Sichturteil vom 2026-08-18 (cnc#97) am Bogen aus #397:

> „bei den neuen Baeumen der Baum mit nur einem Bueschel sieht nicht gut aus.
> Ich meinte, dass der Baum nur **eine** Baumkrone hat und maximal ein/zwei
> kleine Bueschel. **Ohne Aeste, die keine Blaetter tragen.**"

Alle Bilder unten sind **Windows-Bilder** (echte Engine, echter Renderer) --
gleiche Karte, gleiche Kameras, gleicher Baum. Nur die Modelle sind getauscht.

## Der Befund als Zahl

| | vorher (#397) | nachher (#419) |
|---|---|---|
| kahle Aeste ueber acht Varianten | **43** | **0** |
| Varianten, in denen KEIN Ast Laub trug | 5 von 8 | -- |
| Laubkoerper je Baum | 1 (klein, oben) | 1 grosse Krone + 0..2 kleine Bueschel |
| Dreiecke je Baum | 894 .. 1000 | 320 .. 576 |

Der alte Baum liess das ganze Astgeruest stehen und haengte ein einziges
Blattbueschel obenauf. Jetzt gibt es die laublosen Aeste nicht mehr — sie
werden nicht abgeschnitten, sie entstehen gar nicht erst.

## Vorher / nachher, gleiche Kamera

| Ansicht | vorher | nachher |
|---|---|---|
| Baum 05, nah | [`vorher-reihe2-nah-windows.png`](vorher-reihe2-nah-windows.png) | [`nachher-reihe2-nah-windows.png`](nachher-reihe2-nah-windows.png) |
| Baum 02, nah | [`vorher-reihe1-nah-windows.png`](vorher-reihe1-nah-windows.png) | [`nachher-reihe1-nah-windows.png`](nachher-reihe1-nah-windows.png) |
| Leitbaum-Reihe (Massstab) | [`vorher-leitbaum-massstab-windows.png`](vorher-leitbaum-massstab-windows.png) | [`nachher-leitbaum-massstab-windows.png`](nachher-leitbaum-massstab-windows.png) |
| ganzes Raster von oben | [`vorher-raster-aufsicht-windows.png`](vorher-raster-aufsicht-windows.png) | [`nachher-raster-aufsicht-windows.png`](nachher-raster-aufsicht-windows.png) |

Auf dem Raster stehen oben und in der Mitte die **acht** Ein-Bueschel-Baeume,
unten vier **Leitbaeume** als Vergleich. Der kleine Mech (`armpw`, 26 Elmos)
steht als Massstab dabei.

Dazu der Fabrikbogen der acht neuen Varianten (Front / Aufsicht / RTS):
[`bogen-bueschel-neu.png`](bogen-bueschel-neu.png). Die Fusszeile je Spalte
liest sich `Nr · Dreiecke · Hoehe in Elmos · Zahl der Bueschel`.

## Was du entscheidest

1. **Sieht der Baum jetzt gut aus?** Eine Krone, hoechstens zwei kleine
   Bueschel, kein kahler Ast — so war die Ansage.
2. **Vier von acht Baeumen haben gar kein Bueschel** (nur die Krone). Das
   liegt an „maximal ein/zwei": gezogen wird 0, 1 oder 2. Sollen es immer
   mindestens eines sein, ist das **eine Zahl** im Bauplan
   (`BUESCHEL_ANZAHL_SPANNE` von `0 .. 2` auf `1 .. 2`).
3. **Die Bueschel sitzen teils recht tief am Stamm** (Baum 02 und 04). Sie
   koennen naeher unter die Krone — auch das ist eine Zahl
   (`BUESCHEL_AUSLAGE`), kostet aber mehr verworfene Wuerfe.

## Herkunft

Alles aus der eigenen Fabrik: Geometrie und Textur entstehen in Blender 5.1.2
aus den Zahlen des Leitbaum-Bauplans (`tools/blender/leitbaum_etagen.py` +
`backen.py`), Bauplan-Abschnitt **V11**. Kein Fremdmaterial, kein
`BAR-`-Praefix, je Datei ein Herkunftsnachweis (`license_id: own`).
