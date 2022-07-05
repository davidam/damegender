#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidam@gmail.com>
#  Maintainer: David Arroyo Menendez <davidam@gmail.com>
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
from app.dame_utils import DameUtils

du = DameUtils()

country = "ar"
outpath = "files/names/names_" + country + "/"
outmales = outpath + country + "males.csv"
outfemales = outpath + country + "females.csv"
outsurnames = outpath + country + "surnames.csv"

origpath = outpath + "orig/"
origfile = origpath + "personas.csv"


print("Processing Argentina names ....")

with open(origfile) as csvfile:
    sreader2 = csv.reader(csvfile, delimiter=';', quotechar='|')
    diccfemales = {}
    diccmales = {}
    for row in sreader2:
        try:
            gender = str(row[3])
            name = str(row[1])
        except IndexError:
            print("The program has troubles with the array indexes")
        if (gender == '1'):
            if name in diccfemales.keys():
                diccfemales[name] = int(diccfemales[name]) + 1
            else:
                diccfemales[name] = 1
        elif (gender == '2'):
            if name in diccmales.keys():
                diccmales[name] = int(diccmales[name]) + 1
            else:
                diccmales[name] = 1
    filefem = open(outfemales, 'w')
    filemal = open(outmales, 'w')

    for i in diccfemales.keys():
        str1 = str(i) + ","
        str1 = str1 + str(diccfemales[i]) + "\n"
        filefem.write(str1)
    for j in diccmales.keys():
        str2 = str(j) + ","
        str2 = str2 + str(diccmales[j]) + "\n"
        filemal.write(str2)

filefem.close()
filemal.close()

print("Processing Argentina surnames ....")

with open('origfile') as csvfile:
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    next(sreader, None)
    filesurnames = open(outsurnames,'w')
    diccsurnames = {}
    for row in sreader:
        if row[2] in diccsurnames.keys():
                diccsurnames[row[2]] = diccsurnames[row[2]] + 1
        else:
                diccsurnames[row[2]] = 1
        
    for i in diccsurnames.keys():
        filesurnames.write(str(i)+","+str(diccsurnames[i])+"\n")
    
filesurnames.close()

