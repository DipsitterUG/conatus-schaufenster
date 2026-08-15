# conatus-schaufenster

Vorschaubilder fuer die `bericht`-Issues in [dipsitter-cnc](https://github.com/DipsitterUG/dipsitter-cnc/issues?q=label%3Abericht).

Dieses Repo ist oeffentlich — und zwar aus genau einem Grund: GitHub laedt Bilder in Issues anonym nach. Liegt ein Bild in einem privaten Repo, bleibt im Issue ein grauer Kasten. Damit Chris eine Asset-Charge durchscrollen kann statt sechs Links anzuklicken, muessen die Vorschaubilder oeffentlich erreichbar sein.

Es ist eine **Auslage, keine Quelle**. Der Wahrheitsstand aller Assets liegt in den privaten Repos.

## Was hier hinein darf

- Renderbilder und Kontaktboegen fuer Bericht-Issues
- laengste Kante hoechstens 1200 px — die volle Aufloesung bleibt privat

## Was hier nicht hinein darf

- Quelldateien jeder Art: `.blend`, `.dae`, `.psd`, Texturen, Modelle
- unveroeffentlichter Lore-Text, auch nicht in Dateinamen oder Ordnernamen
- alles, was noch nicht entschieden ist und peinlich waere, wenn es jemand findet

Was einmal hier liegt, bleibt in der Git-Historie, auch nach dem Loeschen der Datei. Im Zweifel nicht hochladen.

## Ablage

```
berichte/JJJJ-MM-TT-charge/asset-variante.png
```

Beispiel: `berichte/2026-08-15-gebaeude-runde-1/kaserne-a.png`

Ordnername gleich Charge, gleich ein Bericht-Issue. So findet man von jedem Bild zurueck zur Entscheidung und umgekehrt.

Einbinden im Issue:

```markdown
![Kaserne A](https://raw.githubusercontent.com/DipsitterUG/conatus-schaufenster/main/berichte/2026-08-15-gebaeude-runde-1/kaserne-a.png)
```

## Rechte

Alle Rechte vorbehalten. Oeffentlich einsehbar heisst nicht frei verwendbar: keine Lizenz, keine Nutzungsfreigabe, keine Erlaubnis zur Verwendung als Trainingsmaterial.

Das ist eine Ansage, keine Sperre — technisch laesst sich das Abgreifen oeffentlicher Bilder nicht verhindern. Deshalb die Groessengrenze oben, und deshalb gehoert hier nur herein, was den Blick von aussen vertraegt.
