# German Bachelor Thesis with Topic „Neron-Models of Elliptic Curves“
## Organisation/Files
- Main file: `neron_models.tex`
- LaTeX definitions: `neron_models.tex`
- Bibliography: `neron_models.bib`
- Chapters: `neron_models-0[1-7].tex` 
  (and notices in abandoned `neron_models-appendix.tex`)


## Timeline
* to be hand in **before 29/09/2016**
* shall be printed on **26/09/2016**

## Compilation
(tested) Preliminaries: TeX Live 2016

Comment out `\includeonly{…}` in `neron_models.tex` before compiling
the first time, else you will have undefined references.

Then use 

```bash
lualatex neron_models.tex
biber neron_models
lualatex neron_models.tex
```
 
