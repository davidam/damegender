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
print(l13)

