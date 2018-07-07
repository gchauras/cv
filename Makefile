RM		:= rm -rf
MV		:= mv -f
MKDIR	:= mkdir -p

LATEX	:= xelatex

DOC		:= GauravChaurasiaCV
STY		:= fontawesome.sty
FONTS	:= $(wildcard fonts/*.ttf)
FONTS	+= $(wildcard fonts/*.otf)
BUILDIR	:= build

all: $(DOC).pdf

${DOC}.tex: cv.yml generate.py
	python3 generate.py cv.yml ${DOC}.tex 0

$(BUILDIR)/$(DOC).pdf: $(DOC).tex $(STY) $(FONTS)
	$(MKDIR) $(BUILDIR)
	$(LATEX) -output-directory=$(BUILDIR) $(DOC)
	$(LATEX) -output-directory=$(BUILDIR) $(DOC)

$(DOC).pdf: $(BUILDIR)/$(DOC).pdf
	$(MV) $(BUILDIR)/$(DOC).pdf .

clean:
	$(RM) $(BUILDIR) ${DOC}.tex $(DOC).pdf
