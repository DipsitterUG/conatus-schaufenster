# Naturobjekte sterben sichtbar (Studio#420) — Sichtprobe nach dem Fix

Windows-Engine, echter Renderer. Karte *Conatus Feature Showcase 0.1*
(4x4 Map-Units), Sonde `conatus_naturtod_probe=2`: 200 Baeume bei Frame 60
gesetzt, bei Frame 120 im selben Frame getoetet. Gleiche Kamera in allen
Bildern; die Frames stehen im Dateinamen.

| Frame | Bild | Was zu sehen ist |
|---|---|---|
| 110 | [`01-vorher-baeume-stehen.png`](01-vorher-baeume-stehen.png) | die 200 Baeume stehen |
| 125 | [`02-bersten-frame-125.png`](02-bersten-frame-125.png) | Holzsplitter, Laub und Staub — und die Stuempfe, die liegen bleiben |
| 140 | [`03-bersten-frame-140.png`](03-bersten-frame-140.png) | dieselbe Wolke, weiter aufgeloest |
| 200 | [`04-danach-stuempfe-bleiben.png`](04-danach-stuempfe-bleiben.png) | Partikel vorbei, der Rest steht |

## Warum das ein zweiter Anlauf ist

Die erste Abnahme (2026-08-18, gleiche Kamera, gleiche Sonde) zeigte **kein
einziges Partikel**: `Spring.SpawnCEG` bekam die CEG-Nummer statt des Namens,
die Engine suchte einen Effekt namens „122" und meldete das nur im Infolog.
Alle Wachen waren trotzdem gruen. Nach dem Fix:

| Bildpaar | mittlere Pixeldifferenz |
|---|---|
| Frame 125 gegen 140 (waehrend des Effekts), **vorher** | 0,002 von 255 — nichts passierte |
| dasselbe Paar **nachher** | **16,971 von 255** |
| Frame 200 gegen 215 (nach dem Effekt) | 0,002 von 255 — so sieht „nichts passiert" aus |

`[CCEG::Load] … invalid` im Infolog des Laufs: **0 Treffer**.

Die Baeume im Bild sind `cc0_birke_01` mit Rest `cc0_stumpf_01` (Studio#422) —
die Sonde nimmt den alphabetisch ersten Baum mit Rest. Die Regel greift also an
den frisch gelieferten CC0-Stuecken mit.
