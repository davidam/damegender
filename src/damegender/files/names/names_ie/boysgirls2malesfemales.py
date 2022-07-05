#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidam@gmail.com>
#  Maintainer: David Arroyo Menendez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

import csv
import json

boyscsv = "boys.csv"
girlscsv = "girls.csv"
outmales = "males.csv"
outfemales = "females.csv"

d = {}
string = ""
fo = open("outmales", "w")

def myint(s):
    if (s == "n/a"):
        x = 0
    else:
        x = int(s)
    return x

with open(boyscsv) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(sexreader, None)
    for row in sexreader:
        print(row)
        name = row[0]
        total = myint(row[1]) + myint(row[2]) + myint(row[3]) + myint(row[4]) + myint(row[5]) + myint(row[6]) + myint(row[7]) + myint(row[8]) + myint(row[9]) + myint(row[10]) + myint(row[11]) + myint(row[12]) + myint(row[13]) + myint(row[14]) + myint(row[15]) + myint(row[16]) + myint(row[17]) + myint(row[18]) + myint(row[19]) + myint(row[20]) 
        string = name + "," + str(total)
        fo.write(string+"\n")
fo.close()

fo = open("outfemales", "w")
with open(girlscsv) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(sexreader, None)
    for row in sexreader:
        print(row)
        name = row[0]
        total = myint(row[1]) + myint(row[2]) + myint(row[3]) + myint(row[4]) + myint(row[5]) + myint(row[6]) + myint(row[7]) + myint(row[8]) + myint(row[9]) + myint(row[10]) + myint(row[11]) + myint(row[12]) + myint(row[13]) + myint(row[14]) + myint(row[15]) + myint(row[16]) + myint(row[17]) + myint(row[18]) + myint(row[19]) + myint(row[20]) 
        string = name + "," + str(total)
        fo.write(string+"\n")
fo.close()
