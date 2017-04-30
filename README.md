# Bachelor Thesis *Neron-Models of Elliptic Curves*
These are the sources of my (German) Bachelor thesis.
The Topic is *Neron-Models of Elliptic Curves*, it was supervised by
[Prof. Dr. Moritz Kerz](http://www.mathematik.uni-regensburg.de/kerz/),
University of Regensburg, and handed in on 28/09/2016.

## Organisation/Files
- Main file: `neron_models.tex`
- LaTeX definitions: `neron_models-def.tex`
- Bibliography: `neron_models.bib`
- Chapters: `neron_models-0[1-7].tex` 
  (and notices in abandoned `neron_models-appendix.tex`)

## Compilation
(Tested) Preliminaries:
- `TeX Live 2016`
- font `Charis SIL` installed
- font `Source Sans Pro` installed

Comment out `\includeonly{…}` in `neron_models.tex` before compiling
the first time, else you will have undefined references.

Then use 

```bash
lualatex neron_models.tex
biber neron_models
lualatex neron_models.tex
```
