# Splat-Kanaele: Fotokacheln statt Sinus-Wellen (Studio#453)

2026-09-08, Windows-Sichttest (Zielsystem; WSL rendert ueber eine andere
GL-Kette). Je Biom eine Probekarte durch die echte Pipeline, zwei Kameras:
Draufsicht (Hoehe 1900) und Nahsicht (Hoehe 220, 65 Grad) mit einer Einheit
als Massstab.

**vorher** = Stand vor #453, **nachher** = mit den Kacheln. Beide Laeufe aus
demselben Seed, derselben Kamera, derselben Engine -- der einzige Unterschied
ist der Inhalt der Splat-Detailtexturen.

| Biom | was sich aendert |
|---|---|
| temperate | unveraendert (hatte seit R9 alle Kacheln) -- die Kontrollprobe |
| steppe | Staubfilm (Kanal 0, 19,3 %) und Felskanal (13,2 %) bekommen Korn |
| desert | die **Grundschicht** (Kanal 2, 65,5 %) war Sinus -- jetzt Duenensand |
| ice | Eisschicht unveraendert; die Schneeflaeche (54 % + 34 %) bleibt Sinus, Schneekachel fehlt noch |
| volcanic | die **Ascheflaeche** (Kanal 2, 67,8 %) und der Basalthang (32,2 %) bekommen Struktur |

Am deutlichsten in den Nahsichten von `desert` und `volcanic`: vorher eine
weich verschmierte Flaeche, nachher ein Korn mit Realmassstab (Kachelperiode
71--143 Elmo, kleiner als eine Einheit).

Quelle der Kacheln: ambientCG (CC0), bereits mit Herkunftsnachweis im
Content-Store des Studios -- fuer #453 kam **keine** neue Fremddatei dazu.
