# Lava glueht — vorher gegen nachher (Studio#410)

Windows-Abzuege, echter Renderer (`tools/terrain_sichttest.ps1`, Water = 4 /
BumpWater aus `config/conatus_springsettings.cfg`). WSL-Bilder zaehlen fuer
Sichturteile nicht und sind hier darum keine.

**Beide Reihen zeigen dieselbe Karte, dieselben drei Kameras, denselben
Frame.** Der einzige Unterschied ist die Modoption `conatus_lava`:

| Reihe | Modoption | Was zu sehen ist |
|---|---|---|
| `lava-vorher-*` | `conatus_lava=0` | Lava als **Wasserart** aus Studio#387 — der Stand vor diesem Vorgang |
| `lava-nachher-*` | `conatus_lava=auto` | dasselbe plus `LuaRules/Gadgets/conatus_lava.lua` |

| Bild | Kamera (Elmos, Hoehe, Grad) |
|---|---|
| `-01` | 704, 512, 900, 18 — der Lavasee von schraeg oben |
| `-02` | 704, 512, 320, 32 — nah auf die Oberflaeche |
| `-03` | 2048, 2048, 4700, 3 — die ganze Karte |

## Warum das Vorherbild braun ist

Das ist kein schlechter Farbwert, sondern die Grenze des Wasser-Renderers.
`cont/base/springcontent/shaders/GLSL/BumpWaterFS.glsl:287-289` kennt keinen
Emissions-Eingang; der einzige sonnenunabhaengige Regler (`ambientFactor`)
addiert `vec3(ambient)`, also **Grau**. Und mit Brechung mischt Zeile 299 die
Wasserfarbe mit hoechstens rund 20 Prozent ins Bild — die uebrigen 80 Prozent
sind der gebrochene Bildschirmabzug des Grundes. Deshalb liest die Lava aus
Studio#387 als dunkle Pfuetze, egal wie orange die `mapinfo` sie einstellt.

## Die Karte

`Conatus Lava Zelle 0.1` — eine **Wegwerf-Probe**, gebaut aus der
ausgelieferten `conatus-biome-volcanic.sd7` mit dem `water`-Block der
Wasserart `lava` aus Studio#387 (`src/conatus_studio/world_biomes/
wasserarten.py:507-542` auf `agent/issue-387`), einschliesslich
`damage = 120.0`. Sie liegt in keinem Repo. Grund: die Kartenpakete aus
Studio#387 sind noch nicht gebaut, und im Spiel-Repo steht keine Karte mit
`water.damage > 0`. Der Schaden auf dieser Karte ist im selben Lauf gemessen
worden: **120,0 HP/s**, mit und ohne Gadget gleich.

## Was das Nachherbild NICHT zeigt

* Kein Sicht-/Nebelabgleich: die Glut leuchtet auch ausserhalb der eigenen
  Sicht (BAR daempft das im Shader, wir haben keinen).
* Keine Gezeiten: der Pegel steht. Unsere Kessel sind Gelaende.
* Keine Blasen, kein Rauch, kein Ton.
