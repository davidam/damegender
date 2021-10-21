#!/usr/bin/python
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv

total = []

diccfemales = {}
diccmales = {}

def natural(x):
    try:
        num = int(x)
    except ValueError:
        num = 0
    if (num < 1):
        num = 0
    return num


with open('babyvornamenfemales.csv') as csvfilef:
    next(csvfilef) # skipping the header row, first row
    next(csvfilef)
    next(csvfilef)     
    sexreader = csv.reader(csvfilef, delimiter=',', quotechar='|')
    fofemales = open("atfemales.csv", "w")    
    for row in sexreader:
        if not(("Gesamtzahl Personen (Männer)" in row[0]) or ("Gesamtzahl Personen (Frauen)" in row[0])):        
            val = natural(row[2]) + natural(row[4]) + natural(row[6]) + natural(row[8]) + natural(row[10]) + natural(row[12]) + natural(row[14]) + natural(row[16]) + natural(row[18]) + natural(row[20])
            print(val)
            fofemales.write(str(row[0]) + "," + str(val) + "\n")
fofemales.close()

with open('babyvornamenmales.csv') as csvfilem:
    next(csvfilem) # skipping the header row, first row
    next(csvfilem)
    next(csvfilem)         
    sexreader = csv.reader(csvfilem, delimiter=',', quotechar='|')
    fomales = open("atmales.csv", "w")        
    for row in sexreader:
        if not(("Gesamtzahl Personen (Männer)" in row[0]) or ("Gesamtzahl Personen (Frauen)" in row[0])):
            val = natural(row[2]) + natural(row[4]) + natural(row[6]) + natural(row[8]) + natural(row[10]) + natural(row[12]) + natural(row[14]) + natural(row[16]) + natural(row[18]) + natural(row[20])
            print(val)
            fomales.write(str(row[0]) + "," + str(val) + "\n")
fomales.close()
