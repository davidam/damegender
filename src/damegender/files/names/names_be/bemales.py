#!/usr/bin/python
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv

total = []

dicc = {}

# We start collecting 2009 data for females
with open('TA_POP_2009_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]
        # total = total + dicc
        # print("name: %s" % row[3])        
        # print("number: %s" % row[4])
        # print(dicc)

with open('TA_POP_2010_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2011_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]
            

with open('TA_POP_2012_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2013_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2014_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2015_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2016_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2017_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]
            
with open('TA_POP_2018_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open('TA_POP_2019_M.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]
            
fo = open("bemales.csv", "w")
for i in dicc.keys():
    fo.write(str(i) + ", " + str(dicc[i]) + "\n")

fo.close()    
