# Objektverteilung: Cluster statt Gleichverteilung (Studio#438) + Eis-Biom aus dem Bestand (Studio#443)

Draufsichten der Testkarte 4x4 Map-Units. **Reines PIL, kein GL** — eine
Punktekarte, keine Sichtabnahme. Sichturteile zaehlen nur unter Windows.

Relief graugruen, Wasser blau, Korridorbahnen hell hinterlegt, Objekte als
Punkte in Kategoriefarbe. Erzeugt mit
`PYTHONPATH=src python3 tools/verteilung_draufsicht.py --biome <biom>
--map-units 4 --seed <seed> --marke <alt|neu>`.

Abgelegt vom Abnahme-Helfer (2026-08-20), weil `output/` in den Worktrees
gitignoriert ist und die Belege sonst mit dem Worktree verschwinden.

## Studio#438 — vorher/nachher, Seed 438

| Biom | R(alle) alt | R(alle) neu |
|---|---:|---:|
| temperate | 0,992 | 0,660 |
| steppe | 1,095 | 0,561 |
| ice | 0,930 | 0,531 |

`*-alt.png` = `origin/main`-Stand vor dem Umbau (mit alter Balance-Tabelle),
`*-neu.png` = danach, gezeichnet vom selben Zeichner. R = Clark-Evans-Index
gegen die **zulaessige** Flaeche; < 1 geklumpt, ~1 zufaellig, > 1 regelmaessig.
Messwerte je Bild im gleichnamigen `.json`.

## Studio#443 — Eis-Biom, Seed 443

`ice-4x4-seed443-alt.png` (Kenney-Staemme) gegen `-neu.png` (eigener Bestand:
Schnee-Leitbaeume, Fichte, Kiefer). Schnee-Baeume sind eigens eingefaerbt.

| | Objekte | Baeume | R(Baeume) | R(alle) |
|---|---:|---:|---:|---:|
| alt | 319 | 237 | 0,435 | 0,502 |
| neu | 317 | 239 | 0,486 | 0,562 |

Vom Abnahme-Helfer nachgefahren, Zahlen bitgleich reproduziert.
