#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# This file was previously located in files/names/names_se/write.py
# You can check the history in this location

import csv

def row2number(x):
    if (x == "-"):
        return 0
    else:
        return int(x)
    
path = "files/names/names_se/"
origpath = path + "orig/"

femalesinput = origpath + "girls.csv.0"
femalesoutput = path + "sefemales.csv"

print(femalesinput)
input = csv.reader(open(femalesinput, 'r'), delimiter=",", quotechar='|')
fo = open(femalesoutput, "w")

for cnt, row in enumerate(input):
    if (cnt >= 9):
        acum = 0
        for i in range(1, 24):
            acum = acum + row2number(row[i])
        fo.write(row[0] + "," + str(acum) + "\n")

fo.close()    

malesinput = origpath + "boys.csv.0"
malesoutput = path + "semales.csv"

input = csv.reader(open(malesinput, 'r'), delimiter=",", quotechar='|')
fo = open(malesoutput, "w")

for cnt, row in enumerate(input):
    if (cnt >= 9):
        acum = 0
        for i in range(1, 24):
            acum = acum + row2number(row[i])
        fo.write(row[0] + "," + str(acum) + "\n")

fo.close()

