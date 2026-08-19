# Leichter Android **V2** aus dem animierten Tripo-Modell — Turnaround (Studio#428, cnc#113)

> ⚠ **Kein Sichttest.** Alles hier ist Blender/EEVEE unter WSL, gerendert aus
> den **fertig zerlegten Pieces** mit der ausgelieferten
> `android_leicht_v2_atlas.png`. Sichttests zaehlen nur unter Windows und in
> der Engine (CLAUDE.md). Diese Bilder sind eine **Entscheidungshilfe**: lohnt
> sich der Windows-Lauf.

## Was hier neu ist gegenueber V1 (`../2026-08-19-android-tripo/`)

Das ist ein **anderes Modell**, nicht dasselbe noch einmal: zweite Lieferung
des Menschen, diesmal **geskinnt und animiert** (41 Joints, drei Clips).
Daraus folgt alles Sichtbare:

* **Es traegt keine Waffe.** V1 hatte ein eigenes `Machine_Gun`-Piece; hier
  gibt es nur den Abschusspunkt `Gun_Muzzle` an den Fingerspitzen rechts.
* **Es steht in der T-Pose.** Das ist Absicht: die Ruhelage des S3O muss die
  Rest-Pose des Rigs sein, sonst kann die Animation aus Studio#429 nicht
  dagegen rechnen. Im Spiel legt das Unit-Skript die Arme an — bis #429 da
  ist, steht die Einheit mit ausgestreckten Armen da. **Kein Fehler.**
* **Es ist schlanker**: Rumpf 5.45 × 3.55 Elmo gegen 7.06 × 7.17 bei V1.

| Bild | was |
|---|---|
| `android-v2-turnaround.png` | **Front / Seite / Ruecken / 45° nebeneinander** |
| `android-v2-front.png` | Front — Visierschlitz und Brustschale |
| `android-v2-seite.png` | Seite (von der **rechten** Koerperseite) |
| `android-v2-ruecken.png` | Ruecken |
| `android-v2-dreiviertel.png` | 45° |
| `android-v2-bauvorschau.png` | dasselbe als `unitpics/android_leicht_v2.png` |
| `android-v2-kontaktbogen.png` | **44 Einzelrenders**: jedes Tripo-Teil rot auf grauem Modell, Front + Seite |

## Worauf zu achten ist

Zu sehen sind: **gelber Visierschlitz**, helle Brustschale, helle
Schienbeinplatten, gelbe Gelenkpunkte an Ellbogen und Knien. Alles sitzt auf
dem Bauteil, auf das es gehoert — das ist zugleich die Sichtprobe darauf, dass
die Zerlegung in 15 Pieces nichts verschoben hat: kein Spalt an Huefte, Knie,
Schulter oder Hals, keine Naht, die im falschen Glied haengt.

Der **Kontaktbogen** ist die zweite Haelfte dieser Probe. Jedes der 44
Tripo-Teile ist dort einzeln rot eingefaerbt — so laesst sich nachsehen, ob
`tripo_part_7` wirklich der Beckenblock ist und `tripo_part_18/19` wirklich
die beiden Hueftbleche. Die Zuordnung selbst kommt aus den **Skin-Gewichten**,
nicht aus dem Augenmass; der Bogen ist die Gegenprobe, nicht die Quelle.

## ⚠ Zwei Fallen, die beide zu einem falschen „Textur kaputt" fuehren

Beide sind beim Bauen dieser Bilder aufgetreten und stehen jetzt als
Kommentar im Bauskript:

1. **Alpha ist die Teamfarben-Maske, kein Deckungsgrad.** 94.6 % der Texel
   haben `alpha = 0`. Blender multipliziert RGB standardmaessig mit Alpha —
   das Modell wird in der Vorschau **schwarz**, obwohl die Datei stimmt.
   Gegenmittel: `image.alpha_mode = "CHANNEL_PACKED"` und im Material **nur**
   die Farbausgabe verdrahten. (Derselbe Fehlalarm wie am 2026-08-19 bei V1.)
2. **Die Datei liegt vertikal gespiegelt auf der Platte** — das ist die
   Engine-Konvention dieses Projekts. Wer sie mit den rohen UVs anschaut,
   sieht ein **zerwuerfeltes** Modell aus weissen und schwarzen Flecken. Die
   Vorschau muss `v` zuruecknehmen. Auch das ist erst passiert, dann behoben.

## Herkunft

**Tripo AI, bezahltes Konto des Menschen, geliefert ueber cnc#113 — Eigentum
Dipsitter** (`origin = commissioned`). Kein Byte aus BAR, Recoil oder einem
Sample-Projekt; deshalb **kein `BAR-`-Praefix**. Der Nachweis haengt als
`.herkunft.json` an jeder ausgelieferten Datei.

Bauweg und alle Zahlen:
`conatus-studio/docs/assets/bauplaene/android-leicht-v2-tripo.md`.
