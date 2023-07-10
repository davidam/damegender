uc3m.pdf: 

	latex uc3m.tex
	bibtex uc3m
	latex uc3m
	pdflatex uc3m.tex

uc3m.es.pdf: 

	latex uc3m.es.tex
	bibtex uc3m.es
	latex uc3m.es
	pdflatex uc3m.es.tex


clean:
	rm -f *dvi *.snm *.out *.nav *.log *.aux *.toc *.vrb *.pdf *.bbl *~
