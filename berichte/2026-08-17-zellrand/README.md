# Zellrand, Transferkorridor, Fluss — vorher/nachher (Studio#386 zu cnc#75)

Sichturteil des Menschen zur Erst-Abnahme von #341 (cnc#75, 2026-08-16):

> „Die **Raender der Karten wirken verwaschen**, die **Ecken wie ein
> unnatuerlicher, gleichfoermiger Schnitt**. Dort, wo die **Transferflaechen**
> zum Kartenwechsel sind, sollte ein **Korridor/Weg/Pfad** sein; z. B. bei
> Sueden neben der Flaeche links und rechts angemessene **Berge/Huegel** —
> natuerlich nicht bei Flachland. Und **probiere es mit einem Fluss**."

Alle Bilder sind **Datenbilder aus der Hoehenkarte** (Hillshade, Sonne aus
Nordwest, dreifach ueberhoeht) — **kein gerendertes Gelaende**. WSL rendert
ueber eine andere GL-Kette; wie es aussieht, entscheidet der Sichttest unter
Windows.

Gebaut mit der vollen Kette: `generate_heightmap` → Erosion → Randlinie →
Korridor-Sohle → Neigungsgrenze, also genau das, was auch im `.sd7` landet
(ohne Texturbacken). Kartengroesse 512 Squares = 4096 Elmos, Weltband
−25…220 Elmo, Planet-Seed 20260815, Raster 10x10.

## Die Bilder

| Datei | Was |
|---|---|
| `vorher-uebersicht.png` / `nachher-uebersicht.png` | `map_3_1` (temperate, flusstal) ganz. Rot = Rand der Blendzone, gruen = Transfertore und Bahnen, blau = unter 0 Elmo. |
| `vorher-ecke.png` / `nachher-ecke.png` | Ecke Nordwest, 160x160 px, dreifach. Die blaue Linie ist die 45-Grad-Diagonale. |
| `vorher-suedrand.png` / `nachher-suedrand.png` | Suedrand ueber die volle Breite, 160 px tief, doppelt. Gruen = Transfertor (400x80 Elmo). |
| `fluss-vorher-*.png` / `fluss-nachher-*.png` | `map_3_9` (ice, flusstal) — die Muendung von `river_1`. Hier ist das Wasser. |

## Was auf den Bildern zu sehen ist

**Vorher.** `vorher-uebersicht.png` zeigt den Bilderrahmen: rundum ein glattes
Band, an allen vier Kanten gleich breit, mit sichtbaren Diagonalen in den
Ecken. In `vorher-ecke.png` liegt der Knick genau auf der blauen 45-Grad-Linie.

**Nachher.** Der Rahmen ist weg — die Feinstruktur laeuft bis an die Randlinie
durch, und der rote Rand der Blendzone schlaengelt sich, statt ein Rechteck zu
sein. In der Ecke folgt nichts mehr der Diagonale. An jedem Tor beginnt eine
flache Bahn ins Innere, flankiert von Erhebungen.

## Die Zahlen dazu

| | vorher | nachher |
|---|---|---|
| Breite der Blendzone (`map_3_1`) | 77 px an **allen vier** Kanten, bei jeder Zelle und jedem Seed | 11–48 px (`map_3_1`), 22–56 px (`map_3_9`) -- je Stelle und je Kante verschieden |
| Anteil der Karte in der Blendzone | 51 % | 21 % (`map_3_1`), 30 % (`map_3_9`) |
| Feinstruktur direkt am Rand (Anteil des Innenraums) | 7–18 % | 68–119 % (`map_3_1`), 135–161 % (`map_3_9`) |
| Randprofil-Korrelation der vier Kanten (Pearson, Mittel) | 0,897 (`map_3_1`) / 0,843 (`map_3_9`) | 0,350 / 0,301 |
| Ecke: Blendgewicht `w(x,z)` gegen `w(z,x)` | Unterschied **0,000000** (exakt gespiegelt) | die beiden Kanten einer Ecke blenden verschieden breit |
| Steigung der Bahn vom Tor ins Innere | 4,14–10,74 Grad (elf Bahnen) | 4,49–4,52 Grad (der Deckel) |
| Erhebung neben der Bahn | keine (der Generator kannte die Tore nicht) | 9,4 bzw. 15,7 Elmo laut Rezept; im Flachland 0 |
| Punkte unter 0 Elmo (Wasser) | 0 von 263 169 | 307 in `map_3_9`, tiefste Stelle −7,1 Elmo |

Die Naht zwischen zwei Nachbarzellen bleibt bei **0 Rohwerten** — alles Neue
liegt im Inneren, die aeusserste Pixelreihe gehoert weiterhin dem
Kantenvertrag.

## Was diese Bilder **nicht** zeigen

- **Wie es im Spiel aussieht.** Datenbilder, kein GL. Texturen, Splats und
  Beleuchtung fehlen ganz.
- **Ob die Bahn gut spielt.** Sie ist begehbar (Steigung gedeckelt) — ob sie
  sich richtig anfuehlt, sagt erst eine Partie.
- **Wasser als Wasser.** Hier ist nur die Geometrie unter dem Spiegel; wie es
  aussieht, ist Studio#387.
- **Mehr als eine Wasserzelle.** Auf dem Standard-Planeten liegt genau eine
  von hundert Zellen tief genug und traegt zugleich einen Fluss.

Erzeugt am 2026-08-17 im Rahmen von Conatus-Studio#386, Branch
`agent/issue-386`.
