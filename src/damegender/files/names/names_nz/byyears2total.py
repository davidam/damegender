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

import csv
import json

nzpathyearsmales = "nznames-boys.csv"
nzpathyearsmales = "nznames-boys.min.csv"
nzpathyearsfemales = "nznames-girls.csv"
nzpathyearsfemales = "nznames-girls.min.csv"
nzpathyears = "nznames.csv"
pathmalesjson = "nzmales.json"
dicc = {}

# dicc["Julia"] = {}
# dicc["Julia"]["1954"] = {}
# dicc["Julia"]["1954"]["female"] = 1389
# dicc["Julia"]["1955"] = {}
# dicc["Julia"]["1955"]["female"] = 1384
# dicc["Julia"]["total"] = {}
# dicc["Julia"]["total"]["female"] = 11384
# print(dicc)


with open(nzpathyears) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)
    l = []
    dicc = {}
    for row in reader:
        # this for is only to set the dicc
        print(row)
        dicc[row[3]] = {}
        dicc[row[3]][row[0]] = {}
        dicc[row[3]][row[0]]["male"] = {}
        dicc[row[3]][row[0]]["female"] = {}
        if (row[1] == 'Girls'):
            dicc[row[3]][row[0]]["female"] = row[4]
        elif (row[1] == 'Boys'):
            dicc[row[3]][row[0]]["male"] = row[4]

print(dicc.keys())
print(dicc)
csvfile.close()

# with open(nzpathyearsmales) as csvfile2:
#     reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
#     next(reader2, None)
#     l = []
#     dicc = {}
#     for row in reader2:
#         # this for is only to set the dicc
#         print(row)
#         dicc[row[3]][row[0]]["male"] = row[2]




    #     dicc[row2[3]][row2[0]]["female"] = row2[2]
    # print(dicc2)
    # j = json.dumps(dicc)

#        dicc[row[1]][row[0 ]]["male"] = row[2]
#    j = json.dumps(dicc)
    #print(j)
#        l.append(zip(row[1], []))
#    print(l)
