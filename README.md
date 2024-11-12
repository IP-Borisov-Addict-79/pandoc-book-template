# Template for generating books using Pandoc

## Quickstart:

- `$ make` - to produce HTML;
- `$ make demo.epub` - to produce EPUB;
- `$ make demo.pdf` - to produce PDF;
- `$ make all` - to produce all three formats.

The main source file is `demo.md`, `demo.yaml` contains document metadata, `demo.bib` is bibliography database. For details see the [compiled HTML version](https://ip-borisov-addict-79.github.io/projects/pandoc-book-template/demo.html).

## Requirements:

- [Pandoc](https://pandoc.org), a universal document converter;
- [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref), filter for numbering and cross-referencing figures, tables and equations;
- [citeproc](https://github.com/jgm/citeproc), extension for bibliography generation;
- For PDF generation:
  - a LaTeX system with XeTeX engine;
  - [Liberation fonts](https://github.com/liberationfonts/liberation-fonts/);
  - [DejaVu fonts](https://dejavu-fonts.github.io/).

## Preview of compiled documents:

- HTML: https://ip-borisov-addict-79.github.io/projects/pandoc-book-template/demo.html
- EPUB: https://drive.google.com/file/d/1A06WWMxGW86kzrSLesJWhvZiabnTkR1C/
- PDF: https://drive.google.com/file/d/1W1u9LjO5ZLfivO7hBe-SfokRjqe5U_E7/

CSS for HTML version is based on a style by Pascal Hertleif (https://gist.github.com/killercup/5917178).
