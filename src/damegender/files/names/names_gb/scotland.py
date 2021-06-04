#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  You can share, copy and modify this software if you are a woman or you
#  are David Arroyo Menéndez and you include this note.

import csv

diccmales = {}
diccfemales = {}

with open('scotland.orig.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)

    for row in reader:
        if (row[1] == 'B'):
            if row[2] in diccmales.keys():
                diccmales[row[2]] = diccmales[row[2]] + int(row[3])
            else:
                diccmales[row[2]] = int(row[3])
        elif (row[1] == 'G'):
            if row[2] in diccfemales.keys():
                diccfemales[row[2]] = int(diccfemales[row[2]]) + int(row[3])
            else:
                diccfemales[row[2]] = int(row[3])

fomales = open("scotland.males.csv", "w")

for i in diccmales.keys():
    fomales.write(i + "," + str(diccmales[i]) + "\n")

fomales.close()

fofemales = open("scotland.females.csv", "w")

for i in diccfemales.keys():
    fofemales.write(i + "," + str(diccfemales[i]) + "\n")

fofemales.close()
