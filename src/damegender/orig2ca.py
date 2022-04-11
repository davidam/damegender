#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# This script allows transform the orig files retrieved and processed
# with download.sh in files/names/names_country to damegender csv files,
# such as, countrymales.csv, countryfemales.csv, countrysurnames.csv


import csv
import json
import re
from app.dame_utils import DameUtils

country = "ca"

results = []

du = DameUtils()
outpath = "files/names/names_" + country + "/"
outmales = outpath + country  + "males.csv"
outfemales = outpath + country  + "females.csv"

origpath = outpath + "orig/"
origfile = origpath + "baby-names-frequency.csv"
    
with open(origfile) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)
    l = []
    dicc = {}
    for row1 in reader:
        # this for is only to set the dicc
        print(row1)
        dicc[row1[1]] = {}
print(dicc)
csvfile.close()

with open(origfile) as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
    next(reader2, None)
    for row2 in reader2:
        dicc[row2[1]][row2[4]] = {}
        dicc[row2[1]][row2[4]]["male"] = {}
        dicc[row2[1]][row2[4]]["female"] = {}
csvfile2.close()
print(dicc)

with open(origfile) as csvfile3:
    reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
    next(reader3, None)
    for row3 in reader3:
        print(row3)
        if (row3[3] == 'Girl'):
            dicc[row3[1]][row3[4]]["female"] = row3[2]
        elif (row3[3] == 'Boy'):
            dicc[row3[1]][row3[4]]["male"] = row3[2]
print(dicc)

for i in dicc.keys():
    males = 0
    females = 0
    for j in dicc[i].keys():
        if (dicc[i][j]["female"] == {}):
            num = 0
        else:
            num = dicc[i][j]["female"]
        females = females + int(num)
        if (dicc[i][j]["male"] == {}):
            num = 0
        else:
            num = dicc[i][j]["male"]
        males = males + int(num)

    dicc[i]["females"] = females
    dicc[i]["males"] = males

# # print(dicc["Paula"]["females"])
jsonvar = json.dumps(dicc)
fo = open("canames.json", "w")
fo.write(jsonvar)
fo.close()

# # print(dicc.keys())

file = open(outmales, "w")

for i in dicc.keys():
    if (dicc[i]["males"] > 0):
        line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
        line = line + "," + str(dicc[i]["males"]) + "\n"
        print(line)
        file.write(line)
file.close()

file = open(outfemales, "w")
for i in dicc.keys():
    if (dicc[i]["females"] > 0):
        line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
        line = line + "," + str(dicc[i]["females"]) + "\n"
        print(line)
        file.write(line)
file.close()
