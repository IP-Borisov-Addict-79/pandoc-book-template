# Template for generating books using Pandoc

## Quickstart:

- `make` - to produce html;
- `make demo.epub` - to produce epub;
- `make demo.pdf` - to produce pdf;
- `make all` - to produce all three formats.

## Requirements:

- [Pandoc](https://pandoc.org), a universal document converter;
- [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref), filter for numbering and cross-referencing figures, tables and equations;
- [citeproc](https://github.com/jgm/citeproc), extension for bibliography generation;
- For pdf generation:
  - a LaTeX system with XeTeX engine;
  - [Liberation fonts](https://github.com/liberationfonts/liberation-fonts/);
  - [DejaVu fonts](https://dejavu-fonts.github.io/).

## Preview of html output:

https://ip-borisov-addict-79.github.io/pandoc-book-template-demo.html

CSS for HTML version is based on a style by Pascal Hertleif (https://gist.github.com/killercup/5917178).
