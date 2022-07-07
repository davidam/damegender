#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2022  David Arroyo Menéndez

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

dicc = du.init_dicc_names_and_years(origfile, 1, 1980, 2020)

with open(origfile) as csvfile3:
    reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
    next(reader3, None)
    for row3 in reader3:
        name = row3[1]
        symbols = [" ", "'", '"']
        print(name)
        name = du.drop_all_external_symbols(name, symbols)
        name = name.capitalize()
        if (row3[3] == 'Girl'):
            dicc[name][int(row3[4])]["females"] = row3[2]
        elif (row3[3] == 'Boy'):
            dicc[name][int(row3[4])]["males"] = row3[2]

for i in dicc.keys():
    males = 0
    females = 0
    for j in dicc[i].keys():
#        print(j)
        if (dicc[i][int(j)]["females"] == {}):
            num = 0
        else:
            num = dicc[i][int(j)]["females"]
        females = females + int(num)
        if (dicc[i][int(j)]["males"] == {}):
            num = 0
        else:
            num = dicc[i][int(j)]["males"]
        males = males + int(num)

    dicc[i]["females"] = females
    dicc[i]["males"] = males

# # # print(dicc["Paula"]["females"])
jsonvar = json.dumps(dicc)
fo = open("canames.json", "w")
fo.write(jsonvar)
fo.close()

# # # print(dicc.keys())

file = open(outmales, "w")

for i in dicc.keys():
    if (dicc[i]["males"] > 0):
        line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
        line = line + "," + str(dicc[i]["males"]) + "\n"
#        print(line)
        file.write(line)
file.close()

file = open(outfemales, "w")
for i in dicc.keys():
    if (dicc[i]["females"] > 0):
        line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
        line = line + "," + str(dicc[i]["females"]) + "\n"
#        print(line)
        file.write(line)
file.close()
