# 1 Introduction

#### Quickstart:

- `$ make`\ --- to produce HTML;
- `$ make demo.epub`\ --- to produce EPUB;
- `$ make demo.pdf`\ --- to produce PDF;
- `$ make all`\ --- to produce all three outputs.

#### Additional requirements besides Pandoc:

- [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref), filter for numbering and cross-referencing figures, tables and equations;
- [citeproc](https://github.com/jgm/citeproc), extension for bibliography generation;
- For PDF generation:
  - a LaTeX system with XeTeX engine;
  - [Liberation fonts](https://github.com/liberationfonts/liberation-fonts/);
  - [DejaVu fonts](https://dejavu-fonts.github.io/).

## 1.1 Document metadata

All document metadata (title, author, etc.) together with style and localization are specified through the YAML file\ --- `demo.yaml`. Some options are only relevant for PDF generated via XeLaTeX backend ("`fontsize`", "`papersize`", the whole "`header-includes`" block), others have impact on the resulting document regardless of format. See comments in the file.

## 1.2 Citations

Bibliographical sources are listed in the example of bibliography database (`demo.bib`) in BibTeX format. Citations and bibliography list are produced via [citeproc](https://github.com/jgm/citeproc) extension library. The document uses American Physical Society citation style which is specified through a [CSL](https://docs.citationstyles.org/) file [american-physics-society.csl](https://www.zotero.org/styles/american-physics-society) (see "`FILTERS`" line in `settings.mk`). You may want to try some other styles listed [here](https://www.zotero.org/styles).

There are a few quirks when using a BibTeX database with citeproc due to certain limitations of CSL, see comments in `demo.bib`. Citations are produced by inserting source labels "`[@src_label]`", like this: [@SOKOLSKY201174]. Several sources can be cited with "`[@src_label1; @src_label2; @src_label3]`", see\ [@Nelson:SLAC:1985; @Weast:1981; @WMM:2020].

> **Note** that sources here are separated by "semicolon", not by "comma" like in your LaTeX!

Earlier it was possible to refer to a particular page in a source with "`[@src_tag, pp. 4]`", but now it seems to be opted out.

## 1.3 Inserting and cross-referencing figures, formulas and tables

Numbering and cross-referencing is done via [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) filter, see "`FILTERS`" line in `settings.mk`.

### 1.3.1 Figures

Figures are inserted with a standard Pandoc syntax, image scale is specified inside curly brackets together with figure label:

```markdown
![Figure caption](path-to image){ width=98% #fig:1 }
```

![(a)\ The dependency of atmospheric depth $x(h)$ according to functions by Linsley and Keilhauer. (b)\ Relative difference in atmospheric heights between Linsley and Keilhauer parametrizatons. Red (Linsley) and blue (Keilhauer) lines represent borders of atmospheric layers in two models. Fig.\ 1 from paper [@Togini:NuINT12].](images/Keilhauer-Linsley.png){ width=98% #fig:1 }

> **Note** that image scale specification must be space-separated from opening and closing brackets, though a figure label by itself does not need that.

The "`#fig:`" is a part of the figure label syntax and is mandatory. In-text reference to a figure is produced by inserting its label as "`[@fig:1]`". The result is\ --- see [@fig:1]. The "Fig.\ " part in the resulting reference (_figure prefix_) is controlled via "`figPrefix`" parameter in `demo.yaml` and is generated automatically.

### 1.3.2 Formulas

Formulas are inserted as a block of LaTeX math environment enclosed in "`$$..$$`" operator brackets:

```tex
$$
    E^2 = p^2 c^2 + m_0^2 c^4\text{.}
$$ {#eq:energy}
```

$$
    E^2 = p^2 c^2 + m_0^2 c^4\text{.}
$$ {#eq:energy}

Equation labels are specified inside curly brackets after a space from the closing "`$$`". The "`#eq:`" is a part of the equation label syntax. In-text reference to equation is produced by inserting its label as "`([-@eq:energy])`": behold the reference to equation\ ([-@eq:energy]).

> **Note** the "minus" character before "at" sign in the reference code: it suppresses insertion of _equation prefix_ ("`eqnPrefix`" which is set to "`eq.`\ " by default); i.e. without this minus the resulting reference would look like "([@eq:energy])" rather than just\ "([-@eq:energy])".

Pandoc can covert TeX-math to codes intended for several math rendering engines, most prominent of them are [MathJax](https://www.mathjax.org/) and [MathML](https://www.w3.org/TR/MathML/). Most web-browsers support both, but your average epub-reader supports only MathML. Thus, when converting to EPUB, the "`--mathml`" option is _always_ recommended. This is also the default option for HTML conversion and it can be changed to other value (see "`HTML_MATH`" line in `settings.mk`):

```console
$ make HTML_MATH=--mathjax
```

This will produce a HTML document that renders equations via MathJax.

> **Another consideration** when choosing a math rendering option: a web-page that displays MathML is completely self-contained, while MathJax by default relies heavily on external web.

### 1.3.3 Tables

A detailed description of syntaxes for tables of various types is given in\ [@Pandoc], section [8.9](https://pandoc.org/chunkedhtml-demo/8.9-tables.html). Here we use the _pipe table_ syntax:

~~~ {.md .numberLines}
| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

 : Demonstration of pipe table syntax, example
   [8.9.5](https://pandoc.org/chunkedhtml-demo/8.9-tables.html)
   by MacFarlane\ [@Pandoc]. {#tbl:table_example}
~~~

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

 : Demonstration of pipe table syntax, example
   [8.9.5](https://pandoc.org/chunkedhtml-demo/8.9-tables.html)
   by MacFarlane\ [@Pandoc].
   {#tbl:table_example}

A table can be referenced by inserting its tag: "`[@tbl:table_example]`". The "`#tbl:`" is a part of the table label syntax. The result: the beauty of a pipe table is demonstrated in [@tbl:table_example]. The "Table\ " part of the reference (_table prefix_) is produced automatically and is controlled via "`tblPrefix`" parameter in `demo.yaml`.
