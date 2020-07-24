# $Id: Makefile 4229 2006-06-21 22:20:33Z jjamor $

all: damegender.pdf

damegender.dvi:
	latex damegender.tex

damegender.pdf: damegender.dvi

	dvipdf damegender.dvi

clean:
	rm -f damegender.dvi damegender.ps damegender.blg damegender.bbl *.snm *.out *.nav *.log *.aux *.toc *.vrb *.pdf *~
