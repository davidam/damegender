#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  You can share, copy and modify this software if you are a woman or you
#  are David Arroyo Menéndez and you include this note.


import csv

fo = open("males.txt", "w")

with open('intermales.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if (int(row[1]) > 1000):
            fo.write(row[0]+"\n")

fo.close()

fo2 = open("females.txt", "w")

with open('interfemales.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if (int(row[1]) > 1000):
            fo2.write(row[0]+"\n")

fo2.close()
