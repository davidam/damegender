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

females2008 = "females2008.csv"
females2018 = "females2018.csv"
females2019 = "females2019.csv"
males2008 = "males2008.csv"
males2018 = "males2018.csv"
males2019 = "males2019.csv"

dicc = {}

dicc["Julia"] = {}
dicc["Julia"]["1954"] = {}
dicc["Julia"]["1954"]["female"] = 1389
dicc["Julia"]["1955"] = {}
dicc["Julia"]["1955"]["female"] = 1384
dicc["Julia"]["total"] = {}
dicc["Julia"]["total"]["female"] = 11384
#print(dicc)

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


diccfemales = {}
diccmales = {}
years = ["2008", "2018", "2019"]
l = [females2008, females2018, females2019, males2008, males2018, males2019]
#print(l)

# females

females = [females2008, females2018, females2019]

for i in females:
    if (i == "females2008.csv"):
        year = "2008"
    elif (i == "females2018.csv"):
        year = "2018"
    elif (i == "females2019.csv"):
        year = "2019"
        
    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)
        for row1 in reader1:
            diccfemales[row1[0]] = {}
        csvfile1.close()

    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)    
        for row1 in reader1:
            for y in years:
                diccfemales[row1[0]][y] = {}
        csvfile1.close()

    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)    
        for row1 in reader1:
            for y in years:
                diccfemales[row1[0]][y] = 0
        csvfile1.close()
        
for i in females:
    if (i == "females2008.csv"):
        year = "2008"
    elif (i == "females2018.csv"):
        year = "2018"
    elif (i == "females2019.csv"):
        year = "2019"
    
    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1)    
        for row1 in reader1:
            diccfemales[row1[0]][year] = row1[1]
        csvfile1.close()


print(diccfemales)
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")        
print(diccfemales.keys())

for k in diccfemales.keys():
    if not diccfemales[k]['2008']:
        diccfemales[k]['2008'] = 0
    if not diccfemales[k]['2018']:
        diccfemales[k]['2018'] = 0
    if not diccfemales[k]['2019']:
        diccfemales[k]['2019'] = 0
        
    print("int(diccfemales[k]['2008'])" + str(diccfemales[k]['2008']))
    print("int(diccfemales[k]['2018'])" + str(diccfemales[k]['2018']))
    print("int(diccfemales[k]['2019'])" + str(diccfemales[k]['2019']))
    
    total = int(diccfemales[k]['2008']) + int(diccfemales[k]['2018']) + int(diccfemales[k]['2019'])
    print(total)
    diccfemales[k]['total'] = total
        
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")        

json.dumps(diccfemales)
fo = open("females.json", "w")
fo.write("[" + str(diccfemales) + "]")
fo.close()


with open("isfemales.csv", "w") as f:
    for fem in diccfemales.keys():
        string = fem + "," + str(diccfemales[fem]['total'])
        f.write(string+"\n") 
f.close()

# # males

males = [males2008, males2018, males2019]

for i in males:
    if (i == "males2008.csv"):
        year = "2008"
    elif (i == "males2018.csv"):
        year = "2018"
    elif (i == "males2019.csv"):
        year = "2019"
        
    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)
        for row1 in reader1:
            diccmales[row1[0]] = {}
        csvfile1.close()

    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)    
        for row1 in reader1:
            for y in years:            
                diccmales[row1[0]][y] = {}
        csvfile1.close()

    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)    
        for row1 in reader1:
            for y in years:
                diccmales[row1[0]][y] = 0
        csvfile1.close()

print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")        

        
for i in males:
    if (i == "males2008.csv"):
        year = "2008"
    elif (i == "males2018.csv"):
        year = "2018"
    elif (i == "males2019.csv"):
        year = "2019"
    
    with open(i) as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',', quotechar='|')
        next(reader1, None)    
        for row1 in reader1:
            diccmales[row1[0]][year] = row1[1]
        csvfile1.close()

print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")
print("---------------------------------------------------------------------------\n")        
        
for k in diccmales.keys():
    if not diccmales[k]['2008']:
        diccmales[k]['2008'] = 0
    if not diccmales[k]['2018']:
        diccmales[k]['2018'] = 0
    if not diccmales[k]['2019']:
        diccmales[k]['2019'] = 0

    print("int(diccmales[k]['2008'])" + str(diccmales[k]['2008']))
    print("int(diccmales[k]['2018'])" + str(diccmales[k]['2018']))
    print("int(diccmales[k]['2019'])" + str(diccmales[k]['2019']))
    
    total = int(diccmales[k]['2008']) + int(diccmales[k]['2018']) + int(diccmales[k]['2019'])
    print(total)
    diccmales[k]['total'] = total
        
print(diccmales)
    
json.dumps(diccmales)
fo = open("males.json", "w")
fo.write("[" + str(diccmales) + "]")
fo.close()

with open("ismales.csv", "w") as f:
    for m in diccmales.keys():
        string = m + "," + str(diccmales[m]['total'])
        f.write(string+"\n") 
                                    
f.close()










    
