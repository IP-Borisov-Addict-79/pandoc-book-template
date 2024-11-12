VIEW        =    firefox
            
DOC         =    demo
SRC         =    $(DOC).md

FIGURES     =    Keilhauer-Linsley.png
IMAGES      =    $(addprefix images/, $(FIGURES))
            
CSL_BASE    =    american-physics-society
CSL_URL     =    https://www.zotero.org/styles/$(CSL_BASE)
CSL         =    $(CSL_BASE).csl
            
PDF         =    $(DOC).pdf
HTML        =    $(DOC).html
EPUB        =    $(DOC).epub

include epub-fonts.mk
include settings.mk

$(HTML): $(SRC) $(BIB) $(YAML) $(CSL) html.css $(IMAGES)
	pandoc $(HTML_OPTS) $(SRC)

$(EPUB): $(SRC) $(BIB) $(YAML) $(CSL) epub.css $(IMAGES) $(FONTS_ALL)
	pandoc $(EPUB_OPTS) $(SRC)

$(PDF): $(SRC) $(BIB) $(YAML) $(CSL) $(IMAGES)
	pandoc $(PDF_OPTS) $(SRC)

all : $(HTML) $(EPUB) $(PDF)

preview: $(HTML)
	$(VIEW) $(HTML) 2> /dev/null &

$(CSL):
	curl -L -o $(CSL) $(CSL_URL)

$(FONTS_ALL) &: 
	$(MAKE) -C $(FONTS_DIR)

clean:
	@rm $(HTML)

clean-all:
	$(MAKE) -C $(FONTS_DIR) clean
	$(MAKE) clean
	@rm $(EPUB) $(PDF) $(CSL)

.PHONY: clean clean-all
