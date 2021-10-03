#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

def row2number(x):
    if (x == "-"):
        return 0
    else:
        return int(x)

femalesinput = "be0001namntab11-2020.csv"
femalesoutput = "sefemales.csv"
input = csv.reader(open(femalesinput, 'r'), delimiter=",", quotechar='|')
fo = open(femalesoutput, "w")

for cnt, row in enumerate(input):
    if (cnt >= 9):
        acum = 0
        for i in range(1, 24):
            acum = acum + row2number(row[i])
        fo.write(row[0] + "," + str(acum) + "\n")

fo.close()    


malesinput = "be0001namntab12-2020.csv"
malesoutput = "semales.csv"
input = csv.reader(open(malesinput, 'r'), delimiter=",", quotechar='|')
fo = open(malesoutput, "w")

for cnt, row in enumerate(input):
    if (cnt >= 9):
        acum = 0
        for i in range(1, 24):
            acum = acum + row2number(row[i])
        fo.write(row[0] + "," + str(acum) + "\n")

fo.close()

