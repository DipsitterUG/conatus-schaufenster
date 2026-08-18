# Leichter Android — Zielbilder A/B/C (Studio#418, Stufe 0)

Die erste eigene Einheit des Spiels. Drei Lesarten desselben Auftrags, alle im
selben Maßstab, alle mit derselben Waffe — die Skizze des Menschen ist
unbewaffnet, das MG ist Pflicht (`objekte.md:55-57`).

**Die eine Frage: woher stammt das Chassis, und wie viel Verkleidung trägt es?**

| | |
|---|---|
| **A — Arbeiter-Chassis** | umgerüsteter Industrie-Androide: Platten aufgeschraubt, Kabel offen, leere Werkzeug-Aufnahmen, MG am Trageriemen |
| **B — Sicherungs-Chassis** | von Anfang an für Wachdienst gebaut: geschlossene Panzerschale, Helmvisier, kompakt |
| **C — Rahmenläufer** | Skelett aus Streben, Verkleidung nur am Brustkasten, Umriss mit Durchblicken |

## Was da liegt

| Datei | was |
|---|---|
| `stil-ABC-bogen.png` | die drei Turnarounds untereinander (Front \| 45° \| Seite) |
| `massstab-neben-dem-grunt.png` | A · B · C auf gemeinsamer Elmo-Skala, mit den belegten Höhenlinien der Nachbarn |
| `silhouetten-probe.png` | Umriss und echtes Bild auf Spielentfernung (27 px), 6x vergrößert |
| `android-A-arbeiter-chassis.png` | Kandidat A, 1536x1024 |
| `android-B-sicherungs-chassis.png` | Kandidat B, 1536x1024 |
| `android-C-rahmenlaeufer.png` | Kandidat C, 1536x1024 |
| `messwerte.json` | alle Zahlen |
| `_messen-adhoc.py` | Messung und Bögen, nachstellbar |

## Der Befund, der vor dem Bauen umfiel

Die tradierte Maßstabszahl „`armpw` ist 26 Elmo hoch" gilt für ein Modell, das
im Spiel **nicht geladen wird**. `units/BAR-armpw.lua:22` lädt
`roboterlight.s3o` — und das misst **18.64 Elmo**, nicht 26. Alle Größen hier
sind gegen 18.64 gerechnet.

## Unser Vorschlag: A

Er schreibt die Skizze fort (helle aufgesetzte Platten auf fast schwarzem
Unterbau) und trifft den Kanon-Ton wörtlich — ein Arbeiter mit Waffe, kein
Held. Und er hat den Wertekontrast, der auf 50 m als einziges noch trägt,
nachdem der Umriss aufgehört hat zu tragen: auf 27 px sind alle drei derselbe
Umriss (9–11 px breit), was sie trennt, ist die Helligkeit.

## Herkunft

Alles aus eigener Erzeugung: Bildwerkstatt (`gpt-image-2` über die
ChatGPT-Anmeldung, `--register einheit` mit den Skizzen des Menschen als
Stilanker), numpy/PIL. Kein Fremdmaterial, keine Fremd-Repos, kein
`BAR-`-Präfix.

Vollständiges Protokoll mit allen Belegen:
`conatus-studio/docs/abnahme/2026-08-18-android-zielbild/README.md`.
