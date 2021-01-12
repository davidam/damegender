#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv
import json

frpathyearsmales = "frnames-boys.csv"
# # frpathyearsmales = "frnames-boys.min.csv"
frpathyearsfemales = "frnames-girls.csv"

# # frpathyearsfemales = "frnames-girls.min.csv"
frpathyears = "nat2019.csv"

pathmalesjson = "frmales.json"
csvoutmales = "frmales.csv"
csvoutfemales = "frfemales.csv"
dicc = {}

dicc["Julia"] = {}
dicc["Julia"]["1954"] = {}
dicc["Julia"]["1954"]["female"] = 1389
dicc["Julia"]["1955"] = {}
dicc["Julia"]["1955"]["female"] = 1384
dicc["Julia"]["total"] = {}
dicc["Julia"]["total"]["female"] = 11384
#print(dicc)



with open(frpathyears) as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    next(reader, None)
    l = []
    dicc = {}
    for row1 in reader:
        dicc[row1[1]] = {}

    for j in dicc.keys():
        for i in range(1900, 2019):
            dicc[j][i] = {}
            dicc[j][i] = {}            

    for j in dicc.keys():
        for i in range(1900, 2019):
            dicc[j][i]["male"] = {}
            dicc[j][i]["female"] = {}            
            
csvfile.close()                            

# with open(frpathyears) as csvfile2:
#     reader2 = csv.reader(csvfile2, delimiter=';', quotechar='|')
#     next(reader2, None)

#     for row2 in reader2:
#         if (row2[0] == 1): # female
#             dicc[row2[1]][row2[2]]["female"] = row2[3]

#         elif (row2[0] == 2): # male            
#             dicc[row2[1]][row2[2]]["male"] = row2[3]

# csvfile2.close()

print(dicc)

# with open(frpathyears) as csvfile2:
#     reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
#     next(reader2, None)        
#     for row2 in reader2:        
#         dicc[row2[3]][row2[0]] = {}
        
#         # dicc[row1[3]][row1[0]]["male"] = {}
#         # dicc[row1[3]][row1[0]]["female"] = {}
# csvfile2.close()        
# print(dicc)

# with open(frpathyears) as csvfile3:
#     reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
#     next(reader3, None)        
#     for row3 in reader3:        
# #        dicc[row3[3]][row3[0]] = {}
#         dicc[row3[3]][row3[0]]["male"] = {}
#         dicc[row3[3]][row3[0]]["female"] = {}
# csvfile3.close()        
# print(dicc)

# with open(frpathyears) as csvfile4:
#     reader4 = csv.reader(csvfile4, delimiter=',', quotechar='|')
#     next(reader4, None)
#     for row4 in reader4:
#         if (row4[1] == 'Girls'):
#             dicc[row4[3]][row4[0]]["female"] = row4[4]
#         elif (row4[1] == 'Boys'):
#             dicc[row4[3]][row4[0]]["male"] = row4[4]

# print(dicc)
            
# print(dicc.keys())
# for i in dicc.keys():
#     males = 0
#     females = 0
#     for j in dicc[i].keys():
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

# print(dicc["Paula"]["females"])
# jsonvar = json.dumps(dicc)
# fo = open("frnames.json", "w")
# fo.write(jsonvar)
# fo.close()

# print(dicc.keys())

# file = open(csvoutmales, "w")    
# for i in dicc.keys():
#     line = str(i) + "," + str(dicc[i]["males"]) + "\n"
#     file.write(line)
# file.close()

