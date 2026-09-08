# Splat-Kanaele ohne Fotokachel geschlossen (Studio#453)

Windows-Engine-Abzuege, je Biom eine Probekarte von 4x4 Map-Units, gleiche
Saat, gleiche Kamera, gleicher Wasser-Renderer (Water=4) -- **einziger**
Unterschied zwischen `vorher` und `nachher` ist die Belegung der vier
Splat-Kanaele mit CC0-Fotokacheln (ambientCG) statt mit Sinus-Wellen.
Aufgenommen mit `tools/terrain_sichttest.ps1`, 2026-09-08.

| Datei | Kamera |
|---|---|
| `*-drauf-*.jpg` | Draufsicht, Kamerahoehe 1900 Elmo ueber Kartenmitte |
| `*-nah-*.jpg` | Nahsicht, 220 Elmo Hoehe, 65 Grad von der Senkrechten; die Figur in der Mitte ist eine Einheit als Massstab |

## Was zu sehen ist

- **volcanic** und **desert**: der groesste Sprung. Vorher eine weiche,
  glaenzende Flaeche mit grossen Schlieren ("geschmolzenes Plastik"), nachher
  ein koerniges Schlacke- bzw. Sandfeld. Gemessener Feinkontrast der Nahsicht:
  volcanic +121 %, desert +12 %.
- **steppe**: kleiner Sprung (+1 %). Die Grundschicht hatte schon eine Kachel;
  neu sind Staubfilm und Fels, und der Fels liegt an Haengen, die diese Kamera
  kaum zeigt.
- **temperate**: **Kontrollbild.** Hier wurde nichts geaendert, und die Bilder
  sind praktisch deckungsgleich (mittlere Pixelabweichung 0,0 bzw. 0,2 von
  255). Ohne dieses Paar waere nicht belegt, dass die Unterschiede oben von
  der Aenderung kommen und nicht vom Aufnahmeverfahren.
- **ice**: ebenfalls unveraendert -- und das ist hier **kein** Erfolg, sondern
  der offene Rest. Die beiden Kanaele, die 88 % der Eisflaeche tragen, sind
  Schnee, und eine Schneekachel gibt es noch nicht. Die schlierige Oberflaeche
  auf `ice-nah-nachher.jpg` ist genau der Zustand, den desert und volcanic
  gerade verlassen haben.
