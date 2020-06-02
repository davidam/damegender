#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

boyscsv = "boys.csv"
girlscsv = "girls.csv"
outmales = "males.csv"
outfemales = "females.csv"

d = {}
string = ""
fo = open("outmales", "w")

def myint(s):
    if (s == "n/a"):
        x = 0
    else:
        x = int(s)
    return x

with open(boyscsv) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(sexreader, None)
    for row in sexreader:
        print(row)
        name = row[0]
        total = myint(row[1]) + myint(row[2]) + myint(row[3]) + myint(row[4]) + myint(row[5]) + myint(row[6]) + myint(row[7]) + myint(row[8]) + myint(row[9]) + myint(row[10]) + myint(row[11]) + myint(row[12]) + myint(row[13]) + myint(row[14]) + myint(row[15]) + myint(row[16]) + myint(row[17]) + myint(row[18]) + myint(row[19]) + myint(row[20]) 
        string = name + "," + str(total)
        fo.write(string+"\n")
fo.close()

fo = open("outfemales", "w")
with open(girlscsv) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(sexreader, None)
    for row in sexreader:
        print(row)
        name = row[0]
        total = myint(row[1]) + myint(row[2]) + myint(row[3]) + myint(row[4]) + myint(row[5]) + myint(row[6]) + myint(row[7]) + myint(row[8]) + myint(row[9]) + myint(row[10]) + myint(row[11]) + myint(row[12]) + myint(row[13]) + myint(row[14]) + myint(row[15]) + myint(row[16]) + myint(row[17]) + myint(row[18]) + myint(row[19]) + myint(row[20]) 
        string = name + "," + str(total)
        fo.write(string+"\n")
fo.close()
