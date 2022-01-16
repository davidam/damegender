fairware.pdf: 

	cd doc && pdflatex fairware.tex
	cd doc && bibtex fairware
	cd doc && pdflatex fairware
	cd doc && pdflatex fairware.tex


clean:
	cd doc && rm -f *dvi *.snm *.out *.nav *.log *.aux *.toc *.vrb *.pdf *~
