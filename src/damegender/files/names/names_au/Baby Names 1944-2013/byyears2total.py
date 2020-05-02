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
import unidecode
import unicodedata

pathyearsmales = "male_cy1944_top.csv"
# # nzpathyearsmales = "nznames-boys.min.csv"
pathyearsfemales = "female_cy1944_top.csv"
# # nzpathyearsfemales = "nznames-girls.min.csv"
#pathyears = "nznames.csv"
pathmalesjson = "aumales.json"
csvoutmales = "aumales.csv"
csvoutfemales = "aufemales.csv"
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

def drop_quotes(s):
    aux = ""
    for c in unicodedata.normalize('NFD', str(s)):
        if ((c != '"') and (c != "'")):
            aux = aux + c
    return aux

with open(pathyearsfemales) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)
    l = []
    diccfemales = {}
    for row1 in reader:
        # this for is only to set the diccfemales
        diccfemales[drop_quotes(row1[0])] = {}

#print(diccfemales)
csvfile.close()

diccfemales = {}
diccmales = {}
for i in range(1944, 2013):

    pathyearsmales = "male_cy" + str(i) + "_top.csv"
    pathyearsfemales = "female_cy" + str(i) + "_top.csv"

    # Se inicializan los nombres de todos los ficheros
    with open(pathyearsfemales) as csvfilef:
        reader = csv.reader(csvfilef, delimiter=',', quotechar='|')
        next(reader, None)
        l = []
        for row1 in reader:
            # this for is only to set the diccfemales
            diccfemales[drop_quotes(row1[0])] = {}
        csvfilef.close()

    with open(pathyearsmales) as csvfilem:
        reader = csv.reader(csvfilem, delimiter=',', quotechar='|')
        next(reader, None)
        l = []
        for row1 in reader:
            # this for is only to set the diccmales
            diccmales[drop_quotes(row1[0])] = {}
        csvfilem.close()

print("--------------------------------------------------------------------------")                
print("----------------------------- FEMALES ------------------------------------")        
print(diccfemales)
print(len(diccfemales))
print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")                


print("--------------------------------------------------------------------------")                
print("----------------------------- MALES --------------------------------------")        
print(diccmales)
print(len(diccmales))
print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")                


for i in diccmales.keys():
    for j in range(1944, 2013):
        diccmales[i][j] = {}

for i in diccfemales.keys():
    for j in range(1944, 2013):
        diccfemales[i][j] = {}

        

for i in range(1944, 2013):

    pathyearsmales = "male_cy" + str(i) + "_top.csv"
    pathyearsfemales = "female_cy" + str(i) + "_top.csv"

    with open(pathyearsfemales) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)
        for row1 in reader1:
            diccfemales[drop_quotes(row1[0])][i] = drop_quotes(row1[1])
    csvfile1.close()        
    
    with open(pathyearsmales) as csvfile2:
        reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
        next(reader2, None)
        for row2 in reader2:
            diccmales[drop_quotes(row2[0])][i] = drop_quotes(row2[1])
    csvfile2.close()
    
#print(diccmales)
#print(diccfemales)

for i in diccmales.keys():
    total = 0
    for j in range(1944, 2013):
        if (diccmales[i][j] =={}):
            diccmales[i][j] = 0

for i in diccfemales.keys():
    total = 0
    for j in range(1944, 2013):
        if (diccfemales[i][j] =={}):
            diccfemales[i][j] = 0
            
jsonf = json.dumps(diccfemales)
fo = open("aufemales.json", "w")
fo.write(jsonf)
# Cerramos el archivo fichero.txt
fo.close()

jsonm = json.dumps(diccmales)
fo = open("aumales.json", "w")
fo.write(jsonm)
# Cerramos el archivo fichero.txt
fo.close()

string = ""

aumalesf = open("aumales.csv", "w")

   
for i in diccmales.keys():
    count = 0
    total = 0
    for j in range(1944, 2013):
        try: 
            total = total + int(diccmales[i][j])
        except ValueError:
            pass
    string = str(i) + "," + str(total) + "\n"        
    aumalesf.write(string)
    count = count + 1

aufemalesf = open("aufemales.csv", "w")

for i in diccfemales.keys():
    total = 0
    for j in range(1944, 2013):
        total = total + int(diccfemales[i][j])
    string = str(i) + "," + str(total) + "\n"        
    aufemalesf.write(string)


