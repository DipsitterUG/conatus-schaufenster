# Einheimische mit Siedlung -- passive Nachbarn, mit und ohne

**Vorgang:** Conatus-Studio#415 · **Ansage:** dipsitter-cnc#87, 2026-08-18 --
*„Es darf computergesteuerte Zivilbevoelkerung geben. Die sollen dem Spieler nur
nicht Ressourcen etc. wegschnappen. Es soll Karten geben, da sind ‚die'
einheimisch / haben ein Lager."* · **Designnotiz:** Loremaster #414, Empfehlung B

Aufgenommen mit der **installierten Windows-Engine** (1600x1000), nicht in WSL --
WSL rendert ueber eine andere GL-Kette und ist fuer Sichttests kein Beleg.
Karte „Conatus Feature Showcase 0.1" (2048 x 2048, also 4 x 4 Kartenquadrate),
Siedlung bei Elmo 1786/400. Werkzeug: `tools/terrain_sichttest.ps1` im
Spiel-Repo, aufgerufen mit

```
-Zusatz "LuaGaia=1|conatus_map_cell_id=schaufenster|conatus_siedlung=1|conatus_siedlung_zelle=1|conatus_myzel=0"
-Kameras "1786,400,700,30|1786,400,380,42|1024,1024,2400,3" -Frame 400
```

## Die sechs Bilder

**Zwei Laeufe, dieselben drei Kameras.** Das „ohne" ist kein frueherer Frame,
sondern ein eigener Lauf mit `conatus_siedlung=0` -- die Regel laedt sich dann
selbst ab (im Log steht **keine** einzige `[Conatus][Siedlung]`-Zeile), es ist
also garantiert nichts da. Damit ist das Bildpaar zugleich die Sichtprobe zum
Regler.

| Datei | Lauf | Was zu sehen ist |
|---|---|---|
| `siedlung-aus-01-schraeg` | Regler **aus** | leerer Hang mit Baeumen, Tuempel, Baumstamm |
| `siedlung-aus-02-nah` | Regler **aus** | dieselbe Stelle nah, unberuehrt |
| `siedlung-aus-03-uebersicht` | Regler **aus** | ganze Karte |
| `siedlung-an-01-schraeg` | Regler **an** | sechs Schuppen im Ring, vier Karren unterwegs |
| `siedlung-an-02-nah` | Regler **an** | dasselbe nah -- die Schuppen stehen zwischen den Baeumen, nicht auf ihnen |
| `siedlung-an-03-uebersicht` | Regler **an** | die Siedlung als kleiner Fleck am Kartenrand |

Das lohnendste Paar ist `siedlung-aus-02-nah` gegen `siedlung-an-02-nah`.

## Was die Bilder belegen -- und was nicht

**Belegen sie:** dass die Siedlung steht, dass sie 6 + 4 Teile hat, dass sie
**an Land** und **neben**, nicht **auf** den Baeumen und Felsen steht, und dass
der Regler sie vollstaendig verschwinden laesst.

**Belegen sie nicht:** „nimmt dem Spieler nichts weg". Das ist eine Aussage ueber
eine Abwesenheit und im Bild grundsaetzlich nicht zu sehen -- dafuer ist
`tools/conatus_zivil_smoke.sh` da (Konto, Lager und Vorkommen nach 10 Minuten
byte-identisch mit und ohne Siedlung, mit Rot-Probe).

## Zwei Fehler, die erst diese Bilder gezeigt haben

1. **Die Siedlung stand im Meer.** Der erste Abzug zeigte das Dorf auf dem
   Meeresboden bei Hoehe -15,7. Grund war eine Engine-Vorgabe: fuer ein Gebaeude
   ist `maxWaterDepth` per Default `+10e6`, die Tiefenpruefung laesst dann jede
   Tiefe zu. Der Schuppen traegt jetzt `maxwaterdepth = 0`, und die Platzsuche
   verlangt zusaetzlich Bodenhoehe >= 0.
2. **Der Platz ist knapper, als er aussieht.** In ConatusV0 traegt jedes Baum-
   und Felsmodell `conatus_resource` -- ein „Vorkommen" ist hier auch jeder Baum.
   Auf dieser Karte erreicht der weiteste Punkt nur 358 Elmo Abstand zum
   naechsten; der urspruenglich geforderte Abstand von 510 fuers Zentrum war
   nirgends erfuellbar.

## Herkunft

Eigene Arbeit (Conatus). Verwendete Modelle: `Units/lager-3x3.s3o` und
`Units/lore.s3o`, beide aus der eigenen Assetfabrik mit Herkunftsnachweis. Ein
eigenes Siedlungsmodell im industriellen Register (Wellblech, Zaun, Rauch) ist
beim `assetmanager` **bestellt**, nicht gebaut -- was hier steht, ist bewusst
das Vorhandene.
