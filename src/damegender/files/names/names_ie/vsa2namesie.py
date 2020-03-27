#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

pathcsvfile = "vsa10_1~2p.csv"
outmalescsvfile = "names_ie_males.csv"
outfemalescsvfile = "names_ie_females.csv"
outjsonfile = "names_ie.json"


# JSON vsa10_1~2p.csv

d = {}
#string = '['
string = ""

with open(pathcsvfile) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(sexreader, None)
    for row in sexreader:
        count = row[0]
        name = row[1]
        d[name] = {}

with open(pathcsvfile) as csvfile2:
    sexreader2 = csv.reader(csvfile2, delimiter=',', quotechar='"')
    next(sexreader2, None)
    for row in sexreader2:
        count = row[0]
        name = row[1]
        year = row[2]
        if (count != '".."'):
            d[name][year] = count



# l = d.values()

# print(l)
# for i in l:
#     count = 0
#     for j in range(1998, 2019):
#         print(count)

string = json.dumps(d)
print(string)
fo = open(outjsonfile, "w")
fo.write(string)
fo.close()


#for i in l:
