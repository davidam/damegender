#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>
# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv
import unicodedata

def drop_quotes(s):
    aux = ""
    for c in unicodedata.normalize('NFD', str(s)):
        if ((c != '"') and (c != "'")):
            aux = aux + c
    return aux

def drop_white_spaces(s):
    aux = ""
    for c in unicodedata.normalize('NFD', str(s)):
        if (c != ' '):
            aux = aux + c
    return aux

def drop_quotes(self, s):
    aux = ""
    for c in unicodedata.normalize('NFD', str(s)):
        if ((c != '"') and (c != "'")):
            aux = aux + c
    return aux

def drop_white_space(self, s):
    aux = ""
    for c in unicodedata.normalize('NFD', str(s)):
        if (c != ' '):
            aux = aux + c
    return aux

def csv2list(csvpath,  *args, **kwargs):
    # make a list from a csv file
    header = kwargs.get('header', True)
    delimiter = kwargs.get('delimiter', ',')
    noemptyfield = kwargs.get('noemptyfield', False)
    deletewhitespaces = kwargs.get('deletewhitespaces', False)
    deletequotes = kwargs.get('deletequotes', False)
    l1 = []
    with open(csvpath) as csvfile:
        sexreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        if header:
            next(sexreader, None)
        for row in sexreader:
            if (row != []):
                if ((noemptyfield == False) or (row[noemptyfield] != "")):
                    i = 0
                    while i < len(row):
                        row[i] = drop_quotes(row[i])
                        row[i] = drop_white_spaces(row[i])
                        if deletewhitespaces:
                            row[i] = drop_white_spaces(row[i])
                        if deletequotes:
                            row[i] = drop_quotes(row[i])
                        i = i + 1
                    l1.append(row)
    return l1

def lists2csvfile(listoflists, csvpath, *args, **kwargs):
    length0 = listoflists[0]
    name_position = kwargs.get('name_position', 0)
    frequency_position = kwargs.get('frequency_position', 1)
    fo = open(csvpath, "w")
    for l in listoflists:
        try:
            fo.write(str(l[int(name_position)])+","+str(l[int(frequency_position)])+"\n")
        except IndexError:
            print("The program has troubles with the array indexes")
    fo.close()
    return 1


l0 = csv2list("orig/englandandwales/1996girls.xls.csv.3", header=True)
#print(l0[5:-10])
l0 = l0[5:-10]

lists2csvfile(l0, "1996girls.csv")

l1 = csv2list("orig/englandandwales/1996boysnames.xls.csv.3", header=True, noemptyfield=2)
#print(l1[2:-1])
l1 = l1[2:-1]

lists2csvfile(l1, "1996boys.csv")

l2 = csv2list("orig/englandandwales/1997boysnames.xls.csv.6", header=True, noemptyfield=2)
#print(l2[2:-1])
l2 = l2[2:-1]

lists2csvfile(l2, "1997boys.csv")

l3 = csv2list("orig/englandandwales/1997girls.xls.csv.6", header=True, noemptyfield=2)
# print(l3[2:-1])
l3 = l3[2:-1]

lists2csvfile(l3, "1997girls.csv")

l4 = csv2list("orig/englandandwales/1998boysnames.xls.csv.6", header=True, noemptyfield=2)
l4 = l4[2:-1]

lists2csvfile(l4, "1998boys.csv")

l5 = csv2list("orig/englandandwales/1998girls.xls.csv.6", header=True, noemptyfield=2)
l5 = l5[2:-1]

lists2csvfile(l5, "1998girls.csv")

l6 = csv2list("orig/englandandwales/1999boysnames.xls.csv.6", header=True, noemptyfield=2)
l6 = l6[2:-1]

lists2csvfile(l6, "1999boys.csv")

l7 = csv2list("orig/englandandwales/1999girls.xls.csv.6", header=True, noemptyfield=2)
l7 = l7[2:-1]

lists2csvfile(l7, "1999girls.csv")

l8 = csv2list("orig/englandandwales/2000boysnames.xls.csv.6", header=True, noemptyfield=2)
l8 = l8[2:-1]

lists2csvfile(l8, "2000boys.csv")

l9 = csv2list("orig/englandandwales/2000girls.xls.csv.6", header=True, noemptyfield=2)
l9 = l9[2:-1]

lists2csvfile(l9, "2000girls.csv")

l10 = csv2list("orig/englandandwales/2001boysnames.xls.csv.6", header=True, noemptyfield=2)
l10 = l10[2:-1]

lists2csvfile(l10, "2001boys.csv")

l11 = csv2list("orig/englandandwales/2001girls.xls.csv.6", header=True, noemptyfield=2)
l11 = l11[2:-1]

lists2csvfile(l11, "2001girls.csv")

l12 = csv2list("orig/englandandwales/2002boysnames.xls.csv.6", header=True, noemptyfield=2)
l12 = l12[2:-1]

lists2csvfile(l12, "2002boys.csv")

l13 = csv2list("orig/englandandwales/2002girls.xls.csv.6", header=True, noemptyfield=2)
l13 = l13[2:-1]

lists2csvfile(l13, "2002girls.csv")

l14 = csv2list("orig/englandandwales/2003boysnames.xls.csv.6", header=True, noemptyfield=2)
l14 = l14[2:-1]

lists2csvfile(l14, "2003boys.csv")

l15 = csv2list("orig/englandandwales/2003girls.xls.csv.6", header=True, noemptyfield=2)
l15 = l15[2:-1]

lists2csvfile(l15, "2003girls.csv")

l16 = csv2list("orig/englandandwales/2004boysnames.xls.csv.6", header=True, noemptyfield=2)
l16 = l16[2:-1]

lists2csvfile(l16, "2004boys.csv")

l17 = csv2list("orig/englandandwales/2004girls.xls.csv.6", header=True, noemptyfield=2)
l17 = l17[2:-1]

lists2csvfile(l17, "2004girls.csv")

l18 = csv2list("orig/englandandwales/2005girls.xls.csv.6", header=True, noemptyfield=2)
l18 = l18[2:-1]

lists2csvfile(l18, "2005girls.csv")

l19 = csv2list("orig/englandandwales/2005boysnames.xls.csv.6", header=True, noemptyfield=2)
l19 = l19[2:-1]

lists2csvfile(l19, "2005boys.csv")

l20 = csv2list("orig/englandandwales/2006girls.xls.csv.6", header=True, noemptyfield=2)
l20 = l20[2:-1]

lists2csvfile(l20, "2006girls.csv")

l21 = csv2list("orig/englandandwales/2006boysnames.xls.csv.6", header=True, noemptyfield=2)
l21 = l21[2:-1]

lists2csvfile(l21, "2006boys.csv")

l22 = csv2list("orig/englandandwales/2007girls.xls.csv.6", header=True, noemptyfield=2)
l22 = l22[2:-1]

lists2csvfile(l22, "2007girls.csv")

l23 = csv2list("orig/englandandwales/2007boysnames.xls.csv.6", header=True, noemptyfield=2)
l23 = l23[2:-1]

lists2csvfile(l23, "2007boys.csv")

l24 = csv2list("orig/englandandwales/2008girls.xls.csv.6", header=True, noemptyfield=2)
l24 = l24[2:-1]

lists2csvfile(l24, "2008girls.csv")

l25 = csv2list("orig/englandandwales/2008boysnames.xls.csv.6", header=True, noemptyfield=2)
l25 = l25[2:-1]

lists2csvfile(l25, "2008boys.csv")

l26 = csv2list("orig/englandandwales/2009girls.xls.csv.6", header=True, noemptyfield=2)
l26 = l26[2:-1]

lists2csvfile(l26, "2009girls.csv")

l27 = csv2list("orig/englandandwales/2009boysnames.xls.csv.6", header=True, noemptyfield=2)
l27 = l27[2:-1]

lists2csvfile(l27, "2009boys.csv")

l28 = csv2list("orig/englandandwales/2010girls.xls.csv.6", header=True, noemptyfield=2)
l28 = l28[2:-1]

lists2csvfile(l28, "2010girls.csv")

l29 = csv2list("orig/englandandwales/2010boysnames.xls.csv.6", header=True, noemptyfield=2)
l29 = l29[2:-1]

#print(l29)
lists2csvfile(l29, "2010boys.csv")
