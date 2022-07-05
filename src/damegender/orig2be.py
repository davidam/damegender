#!/usr/bin/python
#  Copyright (C) 2022 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

import csv

total = []

dicc = {}
dicc2 = {}
path = "files/names/names_be/"
origpath = "files/names/names_be/orig/"

###### MALES

# We start collecting 2009 data for males
with open(origpath + 'TA_POP_2009_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]

with open(origpath + 'TA_POP_2010_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2011_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2012_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2013_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2014_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2015_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2016_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


with open(origpath + 'TA_POP_2017_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]

with open(origpath + 'TA_POP_2018_M.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc.keys()):
            val = dicc[row[3]]
            dicc[row[3]] = int(val) + int(row[4])
        else:
            dicc[row[3]] = row[4]


# with open(origpath + 'TA_POP_MALE_2019.txt') as csvfile:
# 
#     spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
#     for row in spamreader:
#         if (row[3] in dicc.keys()):
#             val = dicc[row[3]]
#             dicc[row[3]] = int(val) + int(row[4])
#         else:
#             dicc[row[3]] = row[4]

fo = open(path + "bemales.csv", "w")
for i in dicc.keys():
    fo.write(str(i) + ", " + str(dicc[i]) + "\n")

fo.close()


# ##### FEMALES

# We start collecting 2009 data for females
with open(origpath + 'TA_POP_2009_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]

with open(origpath + 'TA_POP_2010_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2011_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2012_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2013_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2014_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2015_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2016_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


with open(origpath + 'TA_POP_2017_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]

with open(origpath + 'TA_POP_2018_F.txt') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        if (row[3] in dicc2.keys()):
            val = dicc2[row[3]]
            dicc2[row[3]] = int(val) + int(row[4])
        else:
            dicc2[row[3]] = row[4]


# with open(origpath + 'TA_POP_FEMALE_2019.txt') as csvfile:
# 
#     spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
#     for row in spamreader:
#         if (row[3] in dicc2.keys()):
#             val = dicc2[row[3]]
#             dicc2[row[3]] = int(val) + int(row[4])
#         else:
#             dicc2[row[3]] = row[4]

fo = open(path + "befemales.csv", "w")
for i in dicc2.keys():
    fo.write(str(i) + "," + str(dicc2[i]) + "\n")

fo.close()
