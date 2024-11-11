FONTS_DIR        =    epub.fonts

# default fonts embedded in EPUB, requires Liberation Serif:
# https://github.com/liberationfonts
TTF_REG          =    $(FONTS_DIR)/LiberationSerif-Regular.ttf
TTF_IT           =    $(FONTS_DIR)/LiberationSerif-Italic.ttf
TTF_BOLD         =    $(FONTS_DIR)/LiberationSerif-Bold.ttf
TTF_BOLD_IT      =    $(FONTS_DIR)/LiberationSerif-BoldItalic.ttf

# math fonts embedded in EPUB, requires TeX Gyre Schola:
# https://www.gust.org.pl/projects/e-foundry/tg-math
OTF_MATH         =    $(FONTS_DIR)/texgyreschola-math.otf

FONTS_ALL        =    $(TTF_REG) $(TTF_IT) $(TTF_BOLD) $(TTF_BOLD_IT) $(OTF_MATH)

# options for embedding fonts in EPUB
FONTS_EMB        =    --epub-embed-font=$(TTF_REG) \
                          --epub-embed-font=$(TTF_IT) \
                          --epub-embed-font=$(TTF_BOLD) \
                          --epub-embed-font=$(TTF_BOLD_IT) \
                          --epub-embed-font=$(OTF_MATH)

TTF              =    $(subst $(FONTS_DIR)/,,$(TTF_REG) $(TTF_IT) $(TTF_BOLD) $(TTF_BOLD_IT))
OTF              =    $(subst $(FONTS_DIR)/,,$(OTF_MATH))
