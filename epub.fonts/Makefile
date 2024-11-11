include ../epub-fonts.mk

OTF_URL = https://ctan.org/tex-archive/fonts/tex-gyre-math/opentype/$(OTF)

all: $(TTF) $(OTF)

$(TTF) &: fetch-liberation-serif-ttf.py
	@python3 fetch-liberation-serif-ttf.py

$(OTF):
	@curl -L -o $(OTF) $(OTF_URL)

clean:
	@rm -f *.ttf *.otf
	@rm -fr liberation-fonts-ttf-*

.PHONY: clean
