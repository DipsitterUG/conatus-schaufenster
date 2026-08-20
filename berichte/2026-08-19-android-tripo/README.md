# Leichter Android aus dem Tripo-Modell — Turnaround (Studio#427, cnc#113)

> ⚠ **Kein Sichttest.** Alles hier ist Blender/EEVEE unter WSL, gerendert aus
> dem **exportierten S3O** (Reimport ueber das S3O-Kit) mit der ausgelieferten
> `android_leicht_atlas.png`. Sichttests zaehlen nur unter Windows und in der
> Engine (CLAUDE.md). Diese Bilder sind eine **Entscheidungshilfe**: lohnt sich
> der Windows-Lauf.

## Die texturierten Bilder — hier anfangen

| Bild | was |
|---|---|
| `android-tripo-texturiert-turnaround.png` | **Front / 45° / Seite nebeneinander** |
| `android-tripo-texturiert-1-front.png` | Front |
| `android-tripo-texturiert-2-dreiviertel.png` | 45° |
| `android-tripo-texturiert-3-seite.png` | Seite |
| `android-tripo-uv-probe.png` | der UV-Beweis, siehe unten |

Zu sehen sind: heller Brustharnisch, zwei helle Schienbeinschienen, gelber
Visierschlitz, gelb-schwarze Warnstreifen an den Huefttaschen, olivbrauner
Trageriemen. Alles sitzt auf dem Bauteil, auf das es gehoert.

## ⚠ Die vier `android-tripo-*.png` OHNE `texturiert` sind unbrauchbar

Sie zeigen ein **schwarzes** Modell und haben den Verdacht ausgeloest, die
Textur sei zerschossen. **War sie nicht** — der Fehler steckte im Vorschau-
Material, nicht im Asset:

In `tex1` ist der **Alphakanal die Teamfarben-Maske**, kein Deckungsgrad. Bei
uns sind 94.5 % der Texel `alpha = 0`. Blender liest Alpha standardmaessig als
Deckung und multipliziert RGB damit — `50 × 0 = 0`, also schwarz. Recoil tut
das **nicht**: dort ist tex1-Alpha per S3O-Definition die Teamfarbe.

Nachgerechnet an der ausgelieferten Datei:

```
Atlas RGB-Mittel:                                  [50.2 50.4 46.0]
RGB dort, wo Alpha = 0:                            [50.6 50.8 46.2]   <- Farbe IST da
RGB x Alpha (was die alte Vorschau zeigte):        [ 2.4  2.4  2.3]   <- schwarz
Alpha: 0 auf 94.54 % der Flaeche, 255 auf 5.46 %
```

Abhilfe in der Vorschau: `image.alpha_mode = "CHANNEL_PACKED"`. Die Dateien
bleiben unveraendert. Die schwarzen Bilder liegen absichtlich noch hier — damit
niemand denselben Verdacht ein zweites Mal aufmacht.

## Was `android-tripo-uv-probe.png` belegt

Zwei Mal dieselbe Datei, dieselben UVs, nur die V-Richtung getauscht — beide
unbeleuchtet, damit nur die Textur urteilt:

* **links, V gedreht** (die Datei liegt fuer die Engine gespiegelt auf der
  Platte, wie `backen.py` es seit dem Fabrikmodell tut): Brustplatte auf der
  Brust, Schienen auf den Schienbeinen, Visier im Kopfschlitz, Warnstreifen auf
  der Huefttasche.
* **rechts, V roh**: Platten verrutscht, Visier zerlegt, ein gelber Fleck auf
  der Waffe.

→ **Die UVs im S3O stimmen, und die V-Flip-Richtung stimmt.** Das war die
offene Frage; sie ist damit beantwortet, ohne auf den Windows-Lauf zu warten.

Gegenprobe in die andere Richtung: das **unveraenderte GLB** mit seinem eigenen
Material sieht genauso aus wie die linke Seite — gleiche Platten an gleicher
Stelle. Unsere Kette hat am Mapping also nichts verschoben.

## Was diese Bilder trotzdem NICHT belegen

* **Wie es in Recoil aussieht.** Beleuchtung, Teamfarben-Einfaerbung und das
  tex2-Leuchten rechnet die Engine anders als EEVEE.
* **Die Bewegung.** Gehen, Zielen, Rueckstoss, Zerlegen beim Tod — dazu sagt
  nur `tools/conatus_android_smoke.sh` etwas (er sagt PASS), und der misst
  Spiellogik, kein Aussehen.

Herkunft der Geometrie: **Tripo AI, bezahltes Konto des Menschen, geliefert
ueber cnc#113, Eigentum Dipsitter.** Zerlegung, Pivots und Texturmasken:
`conatus-studio/tools/blender/android_tripo.py`.
