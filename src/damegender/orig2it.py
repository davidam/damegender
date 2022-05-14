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

country = "it"

# for i in range(2008,2018):
#     print(i)

    
results = []

du = DameUtils()

outpath = "files/names/names_" + country + "/"
origpath = outpath + "orig/"

l1 = []
for i in range(2008, 2018):
    l1.append(origpath + str(i) + ".csv")

#print(l1)             
input2008 = origpath + "2008.csv"
input2009 = origpath + "2009.csv"
input2010 = origpath + "2010.csv"
input2011 = origpath + "2011.csv"
input2012 = origpath + "2012.csv"
input2013 = origpath + "2013.csv"
input2014 = origpath + "2014.csv"
input2015 = origpath + "2015.csv"
input2016 = origpath + "2016.csv"
input2017 = origpath + "2017.csv"
input2018 = origpath + "2018.csv"

outmales = outpath + country + "males.csv"
outfemales = outpath + country + "females.csv"

origfile = origpath + "baby-names-frequency.csv"

for i in l1:
    l2 = []
    males = {}
    females = {}
    with open(i) as csvfile:
#        print(i)
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)
        males = {}
        females = {}    
        for row in reader:
        # this for is only to set the dicc about names
            name_male = row[1]
            name_male = name_male.capitalize()
            name_female = row[6]
            name_female = name_female.capitalize()
            if (not(name_male in males.keys()) and (name_male != "")):
                males[name_male] = row[2]
            elif (name_male in males.keys()):
                males[name_male] = males[name_male] + row[2]
            if (not(name_female in females.keys()) and (name_female != "")):
                females[name_female] = row[7]
            elif (name_female in females.keys()):
                females[name_female] = females[name_female] + row[7]
    csvfile.close()
#    print(males)
#    print(females)
    # l2.append(males)
    # l2.append(females)

    
# n = len(l2)
# i = 0
# while (i < n):
#     if 
# print(l2[0])
# print(l2[1])
# print(females)


# with open(origfile) as csvfile2:
#     reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
#     next(reader2, None)
#     for row2 in reader2:
#         # this for is only to set the dicc about years and gender
#         name = du.drop_external_quotes(du.drop_white_space_around(row2[1]))
#         name = name.capitalize()
#         if (name != ""):
#             dicc[name][row2[4]] = {}
#             dicc[name][row2[4]]["male"] = {}
#             dicc[name][row2[4]]["female"] = {}
# csvfile2.close()

# with open(origfile) as csvfile3:
#     reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
#     next(reader3, None)
#     for row3 in reader3:
#         name = du.drop_external_quotes(du.drop_white_space_around(row3[1]))
#         name = name.capitalize()
#         if (row3[3] == 'Girl'):
#             dicc[name][row3[4]]["female"] = row3[2]
#         elif (row3[3] == 'Boy'):
#             dicc[name][row3[4]]["male"] = row3[2]

# for i in dicc.keys():
#     males = 0
#     females = 0
#     for j in dicc[i].keys():
# #        print(j)
#         if (dicc[i][j]["female"] == {}):
#             num = 0
#         else:
#             num = dicc[i][j]["female"]
#         females = females + int(num)
#         if (dicc[i][j]["male"] == {}):
#             num = 0
#         else:
#             num = dicc[i][j]["male"]
#         males = males + int(num)

#     dicc[i]["females"] = females
#     dicc[i]["males"] = males

# # # # print(dicc["Paula"]["females"])
# jsonvar = json.dumps(dicc)
# fo = open("canames.json", "w")
# fo.write(jsonvar)
# fo.close()

# # # # print(dicc.keys())

# file = open(outmales, "w")

# for i in dicc.keys():
#     if (dicc[i]["males"] > 0):
#         line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
#         line = line + "," + str(dicc[i]["males"]) + "\n"
# #        print(line)
#         file.write(line)
# file.close()

file = open(outfemales, "w")
for i in females.keys():
    if (int(females[i]) > 0):
        line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
        line = line + "," + str(females[i]) + "\n"
        file.write(line)
file.close()

file = open(outmales, "w")
for i in males.keys():
    if (int(males[i]) > 0):
        line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
        line = line + "," + str(males[i]) + "\n"
        file.write(line)
file.close()
