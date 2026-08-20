# Leichter Android — gebaut (Studio#418, Stufe 1)

Die **erste Einheit, die dieses Projekt vollständig selbst gebaut hat**:
Zielbild aus unserer Bildwerkstatt, Bauplan, Geometrie und Textur aus der
eigenen Fabrik, Unit-Skript und UnitDef von Hand. Kein Byte aus BAR, Recoil
oder einem Sample-Projekt — und deshalb **kein `BAR-`-Präfix**.

Vorgeschichte: `berichte/2026-08-18-android-zielbild/` (A/B/C, der Mensch hat
**A — Arbeiter-Chassis** gewählt, cnc#101, Nennhöhe 20 Elmo).

## Was da liegt

| Datei | was |
|---|---|
| `zielbild-A.png` | das freigegebene Zielbild (Front \| 45° \| Seite) |
| `render-front.png`, `render-dreiviertel.png`, `render-seite.png`, `render-ruecken.png` | dasselbe Modell, gebaut — gleiche Ansichten wie das Zielbild, plus die Rückseite, die das Zielbild nicht zeigt |
| `render-rts.png` | Spielansicht (55° über dem Boden) |
| `windows-01..04.png` | Windows-Engine, echter Renderer (`tools/terrain_sichttest.ps1`) |
| `android_leicht-messwerte.json` | alle Zahlen des Bauskripts, Soll gegen Ist |

## Nebeneinander gehalten

Zielbild und Bau sind **dieselbe Silhouette**: fast schwarzer Zweibeiner,
heller Brustharnisch, zwei helle Schienbeinschienen, waagerechter Leuchtschlitz
im Kopf, Hüftkäfige, Gewehr in beiden Händen. Gemessen statt behauptet:

| | Zielbild | gebaut | Abweichung |
|---|---|---|---|
| Höhe | 20.00 Elmo (Freigabe) | **20.00** | 0 % |
| Breite (Front) | 6.74 | **5.91** | −12 % |
| Tiefe (Seite) | 5.10 | **6.05** | +19 % |
| Farbregister dunkel / hell / mittel / leucht | 74.5 / 13.0 / 12.1 / 0.34 % | **56.9 / 13.1 / 29.5 / 0.59 %** (Atlas) | siehe unten |
| Dreiecke | Budget 5000 | **4004** | −20 %, im Korridor 4000–5500 |
| Pieces | 18 geplant | **17** | `Root` ist kein Piece, sondern der Modellkopf |

Breite und Tiefe wandern **aus demselben einen Grund**: im Zielbild liegt das
Gewehr quer vor dem Bauch, gebaut zeigt es nach vorn. Eine Kampfeinheit zielt,
indem das Skript Torso und Arme dreht — bei einer Ruhelage quer müsste jeder
Schuss zusätzlich 80° Armdrehung nachholen. Die querstehende Waffe fällt damit
aus der Breite heraus und in die Tiefe hinein, genau wie vorhergesagt. Beides
bleibt in der 10–20-%-Toleranz, die der Mensch am 2026-08-15 gesetzt hat.

Beim **Farbregister** sind die beiden Zahlenreihen nicht dieselbe Größe: das
Zielbild ist über die *sichtbaren Frontpixel* gemessen, der Atlas über *Texel*
— und Texel verteilen sich nach UV-Fläche, also zählen Rückseiten und
Innenflächen mit. Am Frontrender desselben Modells stehen 66 % dunkel gegen
57 % im Atlas. Was zählt, steht: der Körper ist dunkel, drei helle Flecken
tragen ihn, ein Schlitz leuchtet.

## Was das Modell im Spiel kann

`tools/conatus_android_smoke.sh` (Spiel-Repo), drei Engine-Läufe, **PASS**:

| Zusage | gemessen |
|---|---|
| spawnt, Modell + Skript laden ohne Lua-Fehler | ja |
| feuert im Anlauf | **6 von 6**, erster Schuss 33–56 Frames nach dem Befehl |
| längster stummer Stillstand in Reichweite ≤ 0,5 s | **6 Frames** (0,2 s), erlaubt 15 |
| marschiert 400 Elmo | Ankunft in Frame 229 |
| steht danach als Regiment (≥ 1,5 Fußabdrücke) | **nn_faktor 1.68**, 53,7 Elmo Nachbarabstand |

**Rot-Probe** — derselbe Lauf mit einem Spielbaum ohne
`scripts/Units/android_leicht.lua`: die Engine überlebt (Ergebniszeile da,
kein Absturz), aber **0 von 6 feuern, Idle 96 %, stumm_max 804 Frames**. Der
Wächter wird also nachweislich rot, wenn das Skript fehlt — er misst etwas.

## Die Windows-Bilder, und was sie NICHT zeigen

Die vier Abzüge stammen aus der **Windows-Engine** (WSL rendert über eine
andere GL-Kette und zählt für Sichttests nicht). Sie belegen: die Einheit
**lädt und läuft im echten Renderer** — das Protokoll führt sie vier Mal als
`TERRAIN-SICHTTEST|EINHEIT|android_leicht|…|id=…`.

**Sie zeigen den Androiden nicht aus der Nähe.** Der Kameratreiber
(`terrain_sichttest.ps1`) setzt die Einheit auf den Zielpunkt der Kamera und
richtet die Kamera auf denselben Punkt; auf der Showcase-Karte liegt dieser
Punkt so, dass der Blick über die Einheit hinweg auf Wasser und Horizont
läuft. Drei Kameraserien mit verschiedenen Höhen und Neigungen haben daran
nichts geändert.

Das ist eine **Lücke, kein Ergebnis** — der Nahblick im Spiel steht aus und
gehört als eigener Auftrag nachgezogen (kleine, flache Probekarte oder ein
Kamera-Versatz im Treiber). Wer das Modell heute ansehen will, nimmt die
Blender-Ansichten oben; wie es *im Spiel* aussieht, hat noch niemand gesehen.

## Herkunft

Alles hier ist eigene Arbeit. Geometrie: `conatus-studio/tools/blender/android_leicht.py`
(Blender 5.1.2, S3O-Kit). Textur: `backen.py`, Cycles-Bake aus den Zonenfarben
des Bauplans. Zielbild: unsere Bildwerkstatt. Bauplan:
`conatus-studio/docs/assets/bauplaene/android-leicht.md`.

---

# Nachtrag 2026-08-20: der Nahblick ist da (Abnahme-Helfer)

Der Absatz oben — „wie es *im Spiel* aussieht, hat noch niemand gesehen" — ist
**ueberholt**. Er stimmte, aber nicht aus dem dort genannten Grund.

**Woran es wirklich lag.** `terrain_sichttest.ps1` setzt die Einheit auf den
Zielpunkt der Kamera und richtet die Kamera auf **den Boden** an diesem Punkt.
Die Einheit steht damit im Bild, aber mit den **Fuessen in der Bildmitte** — sie
waechst nach oben aus dem Bild heraus. Bei Sichtfeld 45° ist die halbe Bildhoehe
`0.414 x Abstand`; fuer 20 Elmo Koerperhoehe braucht es also **mindestens rund
50 Elmo Kameraabstand**, sonst ist der Kopf ab. Die frueheren Serien lagen
darunter oder weit darueber. Der Blick lief nie „auf Wasser und Horizont" — er
lief auf den Bauch.

Kein Werkzeug geaendert, nur die Kamerazeile:

```
powershell -File tools\terrain_sichttest.ps1 -Map "Conatus Feature Showcase 0.1" `
  -Einheit android_leicht -Attribution 0 `
  -Kameras "250,520,60,62|250,900,80,58|900,700,120,52|900,1200,260,45"
```

Vier Standorte statt einem, weil das Gadget **je Kamera eine eigene Einheit**
spawnt — vier Kameras auf denselben Punkt haetten vier Androiden ineinander
gestellt. Die Standorte sind flacher Boden ueber Wasserlinie (aus der Heightmap
der Karte gesucht, Streuung ≤ 13 Elmo auf 80 Elmo Umkreis).

| Bild | was |
|---|---|
| `windows-nah-00-warum-es-vorher-nicht-ging.png` | derselbe Androide bei **35** und bei **60** Elmo, gleicher Bildausschnitt — links der alte Fehlschlag, rechts die Behebung |
| `windows-nah-01-60elmo.png` | **der Nahblick**: ganze Einheit, 60 Elmo Kameraabstand, echter Windows-Renderer |
| `windows-nah-02-abstandsreihe.png` | dieselbe Einheit bei 60 / 80 / 120 / 260 Elmo — von der Nahaufnahme bis zur Spielentfernung |

Ausschnitte gerechnet, nicht gesucht: Bildmitte ist der Fussboden, die Hoehe
folgt aus `20 / (2 · d · tan 22.5°)`.

**Was jetzt zu sehen ist** — und in den Blender-Ansichten so nicht zu sehen war:
der Koerper bleibt auch unter Engine-Licht dunkel, Brustharnisch und
Schienbeinschienen tragen ihn als helle Flecken, der Leuchtschlitz im Kopf
haelt bis 120 Elmo. Ab 260 Elmo bleibt eine dunkle Silhouette mit zwei hellen
Beinflecken — genau die Wertetrennung, die Stufe 0 als das einzige beschrieben
hat, was auf Spielentfernung noch traegt.

Gemessen ist hier nichts — das ist ein **Sichtbeleg**, kein Waechter. Was das
Modell im Spiel *kann*, steht weiter oben und kommt aus
`tools/conatus_android_smoke.sh`.
