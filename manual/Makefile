srcdir = .

DAMEGENDER = ${srcdir}/damegender.texi
DAMEGENDER_ES = ${srcdir}/damegender.es.texi
DAMEGENDER_PO = ${srcdir}/damegender.es.po
DAMEGENDER_POT = ${srcdir}/damegender.pot

pdf: 
	texi2pdf $(DAMEGENDER)

html:
	texi2html $(DAMEGENDER)

info:
	makeinfo $(DAMEGENDER) 

clean:
	rm damegender.aux damegender.cp damegender.cps damegender.log damegender.toc *~

