
all: damegender.pdf

damegender.dvi:
	latex damegender.tex

damegender.pdf: damegender.dvi

	pdflatex damegender.dvi

damegender.png: damegender.pdf
	convert -density 300 damegender.pdf -quality 90 damegender.png

clean:
	rm -f damegender.dvi damegender.ps damegender.blg damegender.bbl *.png *.snm *.out *.nav *.log *.aux *.toc *.vrb *.pdf *~
