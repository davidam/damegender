#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com> 
# Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv

def csv2list(csvpath,  *args, **kwargs):
    # make a list from a csv file
    header = kwargs.get('header', True)
    delimiter = kwargs.get('delimiter', ',')
    noemptyfield = kwargs.get('noemptyfield', False)    
    l1 = []
    with open(csvpath) as csvfile:
        sexreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        if header:
            next(sexreader, None)
        for row in sexreader:
            if (row != []):
                if ((noemptyfield == False) or (row[noemptyfield] != "")):
                    l1.append(row)
    return l1

l0 = csv2list("orig/englandandwales/1996girls.xls.csv.3", header=True)
#print(l0[5:-10])
l0 = l0[5:-10]

l1 = csv2list("orig/englandandwales/1996boysnames.xls.csv.3", header=True, noemptyfield=2)
#print(l1[2:-1])
l1 = l1[2:-1]

l2 = csv2list("orig/englandandwales/1997boysnames.xls.csv.6", header=True, noemptyfield=2)
#print(l2[2:-1])
l2 = l2[2:-1]

l3 = csv2list("orig/englandandwales/1997girls.xls.csv.6", header=True, noemptyfield=2)
# print(l3[2:-1])
l3 = l3[2:-1]

l4 = csv2list("orig/englandandwales/1998boysnames.xls.csv.6", header=True, noemptyfield=2)
l4 = l4[2:-1]

l5 = csv2list("orig/englandandwales/1998girls.xls.csv.6", header=True, noemptyfield=2)
l5 = l5[2:-1]

l6 = csv2list("orig/englandandwales/1999boysnames.xls.csv.6", header=True, noemptyfield=2)
l6 = l6[2:-1]

l7 = csv2list("orig/englandandwales/1999girls.xls.csv.6", header=True, noemptyfield=2)
l7 = l7[2:-1]

l8 = csv2list("orig/englandandwales/2000boysnames.xls.csv.6", header=True, noemptyfield=2)
l8 = l8[2:-1]

l9 = csv2list("orig/englandandwales/2000girls.xls.csv.6", header=True, noemptyfield=2)
l9 = l9[2:-1]

l10 = csv2list("orig/englandandwales/2001boysnames.xls.csv.6", header=True, noemptyfield=2)
l10 = l10[2:-1]

l11 = csv2list("orig/englandandwales/2001girls.xls.csv.6", header=True, noemptyfield=2)
l11 = l11[2:-1]

l12 = csv2list("orig/englandandwales/2002boysnames.xls.csv.6", header=True, noemptyfield=2)
l12 = l12[2:-1]

l13 = csv2list("orig/englandandwales/2002girls.xls.csv.6", header=True, noemptyfield=2)
l13 = l13[2:-1]

l14 = csv2list("orig/englandandwales/2003boysnames.xls.csv.6", header=True, noemptyfield=2)
l14 = l14[2:-1]

l15 = csv2list("orig/englandandwales/2003girls.xls.csv.6", header=True, noemptyfield=2)
l15 = l15[2:-1]

l16 = csv2list("orig/englandandwales/2004boysnames.xls.csv.6", header=True, noemptyfield=2)
l16 = l16[2:-1]

l17 = csv2list("orig/englandandwales/2004girls.xls.csv.6", header=True, noemptyfield=2)
l17 = l17[2:-1]

l18 = csv2list("orig/englandandwales/2005girls.xls.csv.6", header=True, noemptyfield=2)
l18 = l18[2:-1]

l19 = csv2list("orig/englandandwales/2005boysnames.xls.csv.6", header=True, noemptyfield=2)
l19 = l19[2:-1]

l20 = csv2list("orig/englandandwales/2006girls.xls.csv.6", header=True, noemptyfield=2)
l20 = l20[2:-1]

l21 = csv2list("orig/englandandwales/2006boysnames.xls.csv.6", header=True, noemptyfield=2)
l21 = l21[2:-1]

l22 = csv2list("orig/englandandwales/2007girls.xls.csv.6", header=True, noemptyfield=2)
l22 = l22[2:-1]

l23 = csv2list("orig/englandandwales/2007boysnames.xls.csv.6", header=True, noemptyfield=2)
l23 = l23[2:-1]

l24 = csv2list("orig/englandandwales/2008girls.xls.csv.6", header=True, noemptyfield=2)
l24 = l24[2:-1]

l25 = csv2list("orig/englandandwales/2008boysnames.xls.csv.6", header=True, noemptyfield=2)
l25 = l25[2:-1]

l26 = csv2list("orig/englandandwales/2009girls.xls.csv.6", header=True, noemptyfield=2)
l26 = l26[2:-1]

l27 = csv2list("orig/englandandwales/2009boysnames.xls.csv.6", header=True, noemptyfield=2)
l27 = l27[2:-1]

l28 = csv2list("orig/englandandwales/2010girls.xls.csv.6", header=True, noemptyfield=2)
l28 = l28[2:-1]

l29 = csv2list("orig/englandandwales/2010boysnames.xls.csv.6", header=True, noemptyfield=2)
l29 = l29[2:-1]




