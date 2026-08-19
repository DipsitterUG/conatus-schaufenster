# Leichter Android aus dem Tripo-Modell — Turnaround (Studio#427, cnc#113)

> ⚠ **Das ist KEIN Sichttest.** Die Bilder sind Blender/EEVEE unter WSL,
> gerendert aus dem **exportierten S3O** (Reimport ueber das S3O-Kit) mit der
> ausgelieferten `android_leicht_atlas.png`. Sichttests zaehlen nur unter
> Windows und in der Engine (CLAUDE.md). Was hier steht, ist eine
> **Entscheidungshilfe**: lohnt sich der Windows-Lauf.

| Bild | was |
|---|---|
| `android-tripo-1-front.png` | Front (Modellvorderseite = Blender +Y) |
| `android-tripo-2-dreiviertel.png` | 45 Grad |
| `android-tripo-3-seite.png` | Seite |
| `android-tripo-turnaround.png` | die drei nebeneinander |

## Was die Bilder belegen

* Die Front zeigt nach vorn, die Waffe wird vor dem Bauch getragen und zeigt
  nach vorn — die 180-Grad-Drehung beim Bau sitzt.
* Das Modell steht auf dem Boden (Sohle z = 0), nur die Fuesse beruehren ihn.
* Der Reimport findet 17 Pieces mit den Namen, die
  `scripts/Units/android_leicht.lua` ansteuert.

## Was sie NICHT belegen

* **Farbe und Helligkeit im Spiel.** Der Android ist von Haus aus sehr dunkel
  (Median-Helligkeit 44 von 255 in der gelieferten Tripo-Textur). Ob er auf
  Spielentfernung noch lesbar ist, entscheidet Recoils Beleuchtung, nicht
  EEVEE.
* **Ob `tex1` senkrecht richtig herum sitzt.** Die Datei liegt gespiegelt auf
  der Platte, wie es `backen.py` seit dem Fabrikmodell tut; der Zahlenvergleich
  gegen das Original stuetzt das (mittlerer Fehler 0.36 gespiegelt gegen 33.2
  ungespiegelt). Der Beweis ist trotzdem erst der Blick ins Spiel.
* **Die Bewegung.** Gehen, Zielen, Rueckstoss, Zerlegen beim Tod — dazu sagt
  nur `tools/conatus_android_smoke.sh` etwas (er sagt: PASS), und der misst
  Spiellogik, kein Aussehen.

Herkunft der Geometrie: **Tripo AI, bezahltes Konto des Menschen, geliefert
ueber cnc#113, Eigentum Dipsitter.** Zerlegung, Pivots und Texturmasken:
`conatus-studio/tools/blender/android_tripo.py`.
