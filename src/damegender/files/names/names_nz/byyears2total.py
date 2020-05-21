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
# # nzpathyearsmales = "nznames-boys.min.csv"
nzpathyearsfemales = "nznames-girls.csv"
# # nzpathyearsfemales = "nznames-girls.min.csv"
nzpathyears = "nznames.csv"
pathmalesjson = "nzmales.json"
csvoutmales = "nzmales.csv"
csvoutfemales = "nzfemales.csv"
dicc = {}

dicc["Julia"] = {}
dicc["Julia"]["1954"] = {}
dicc["Julia"]["1954"]["female"] = 1389
dicc["Julia"]["1955"] = {}
dicc["Julia"]["1955"]["female"] = 1384
dicc["Julia"]["total"] = {}
dicc["Julia"]["total"]["female"] = 11384
print(dicc)

def delete_duplicated(l):
    if (len(l) == 0):
        return l
    else:
        rest = []
        for i in l:
            if (i != l[0]):
                rest = rest + [i]
    return [l[0]] + delete_duplicated(rest)


with open(nzpathyears) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)
    l = []
    dicc = {}
    for row1 in reader:
        # this for is only to set the dicc
#        print(row)
        dicc[row1[3]] = {}
print(dicc)
csvfile.close()                
with open(nzpathyears) as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
    next(reader2, None)        
    for row2 in reader2:        
        dicc[row2[3]][row2[0]] = {}
        # dicc[row1[3]][row1[0]]["male"] = {}
        # dicc[row1[3]][row1[0]]["female"] = {}
csvfile2.close()        
print(dicc)

with open(nzpathyears) as csvfile3:
    reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
    next(reader3, None)        
    for row3 in reader3:        
#        dicc[row3[3]][row3[0]] = {}
        dicc[row3[3]][row3[0]]["male"] = {}
        dicc[row3[3]][row3[0]]["female"] = {}
csvfile3.close()        
print(dicc)

with open(nzpathyears) as csvfile4:
    reader4 = csv.reader(csvfile4, delimiter=',', quotechar='|')
    next(reader4, None)
    for row4 in reader4:
        if (row4[1] == 'Girls'):
            dicc[row4[3]][row4[0]]["female"] = row4[4]
        elif (row4[1] == 'Boys'):
            dicc[row4[3]][row4[0]]["male"] = row4[4]

print(dicc)
            
print(dicc.keys())
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

print(dicc["Paula"]["females"])
jsonvar = json.dumps(dicc)
fo = open("nznames.json", "w")
fo.write(jsonvar)
fo.close()

print(dicc.keys())

file = open(csvoutmales, "w")    
for i in dicc.keys():
    line = str(i) + "," + str(dicc[i]["males"]) + "\n"
    file.write(line)
file.close()

file = open(csvoutfemales, "w")    
for i in dicc.keys():
    line = str(i) + "," + str(dicc[i]["females"]) + "\n"
    file.write(line)
file.close()

# file = open(csvoutfemales, "w")    
# for i in dicc.keys():
#     for j in dicc[i].keys():
#         # print("inside")
#         # print(i)
#         # print(dicc[i]["females"])        
#         line = str(i) + "," + str(dicc[i]["females"]) + "\n"
#         file.write(line)
# file.close()
    


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
