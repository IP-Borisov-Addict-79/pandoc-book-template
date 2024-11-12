FILTERS        =    --filter pandoc-crossref --citeproc --csl=$(CSL)

# provide document metadata
YAML           =    $(DOC).yaml
META           =    --metadata-file=$(YAML)

# bibliography database file
BIB            =    $(DOC).bib
BIBLIOGRAPHY   =    --bibliography=$(BIB)

# math rendering engine for HTML (other options: `--mathjax` or empty)
HTML_MATH      =    --mathml

# options for different formats
HTML_OPTS      =    -t html5 -s --css html.css \
                        --embed-resources $(HTML_MATH) \
                        --toc $(BIBLIOGRAPHY) $(FILTERS) $(META) -o $(HTML)
EPUB_OPTS      =    -t epub3 --mathml --css epub.css $(FONTS_EMB) -s \
                        --toc $(BIBLIOGRAPHY) $(FILTERS) $(META) -o $(EPUB)
PDF_OPTS       =    -t pdf --pdf-engine=xelatex \
                        --toc $(FILTERS) $(BIBLIOGRAPHY) $(META) -o $(PDF)
