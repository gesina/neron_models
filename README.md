# Bachelorarbeit *Neron-Modelle elliptischer Kurven*
Dies sind die Quellen meiner Bachelorarbeit im Studium Mathematik
B.Sc. an der Universität Regensburg.
Das Thema ist *Neron-Modelle elliptischer Kurven und Entwicklung
solcher aus dem Weierstrass-Modell*.
Sie wurde von [Prof. Dr. Moritz Kerz](http://www.mathematik.uni-regensburg.de/kerz/) betreut
und am 28.09.2016 eingereicht.

## Dateiübersicht
- Hauptdatei (zum Kompilieren): `neron_models.tex`
- LaTeX Definitionen: `neron_models-def.tex`
- Literaturverzeichnis: `neron_models.bib`
- Kapitelinhalte: `neron_models-0[1-7].tex` 
  (und Notizen im aufgegebenen `neron_models-appendix.tex`)

## Compilation
(Getestete) Systemvoraussetzungen:
- `TeXLive 2016`-Distribution
- Schrift [`Charis SIL`](http://software.sil.org/charis/) installiert
- Schrift [`Source Sans Pro`](http://software.sil.org/charis/) installiert

Vor dem ersten Kompilieren sollte `\includeonly{…}` in der Datei
`neron_models.tex` auskommentiert werden, sonst wird es Fehler wegen
undefinierte Querverweise geben.

Zum Kompilieren rufe auf

```bash
lualatex neron_models.tex
biber neron_models
lualatex neron_models.tex
```
