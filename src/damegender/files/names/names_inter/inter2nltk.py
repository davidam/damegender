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

with open('interall.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        try:
            #print(row[2])
            percentmales = round(float(row[2]))
            #print(nummales)
            if (percentmales > 70):
                fomales.write(str(row[0])+"\n")
            percentfemales = round(float(row[3]))
            if (percentfemales > 70):
                fofemales.write(str(row[0])+"\n")            
        except IndexError:
            pprint(row)


fomales.close()
fofemales.close()
