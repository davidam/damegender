#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  You can share, copy and modify this software if you are a woman or you
#  are David Arroyo Menéndez and you include this note.


import csv
from pprint import pprint
fomales = open("males.txt", "w")
fofemales = open("females.txt", "w")

lmales = []
lfemales = []

with open('interall.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        try:
            #print(row[2])
            percentmales = round(float(row[2]))
            #print(nummales)
            if (percentmales > 70):
                lmales.append(str(row[0]))
            percentfemales = round(float(row[3]))
            if (percentfemales > 70):
                lfemales.append(str(row[0]))
        except IndexError:
            pprint(row)
            
l1 = sorted(lmales)
l2 = sorted(lfemales)
            
for m in l1:
    fomales.write(m+"\n")

for f in l2:
    fofemales.write(f+"\n")

fomales.close()
fofemales.close()
