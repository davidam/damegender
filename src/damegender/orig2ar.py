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
outmales = outpath + country  + "males.csv"
outfemales = outpath + country  + "females.csv"

origpath = outpath + "orig/"
origfile = origpath + "personas.csv"

with open(origfile) as csvfile:
#    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    sreader2 = csv.reader(csvfile, delimiter=';', quotechar='|')    
    
    diccfemales = {}
    diccmales = {}
    
    # for row in sreader:
    #     try:
    #         if (row[3] == '1'):
    #             diccfemales[row[1]] = {}
    #         elif (row[3] == '2'):
    #             diccmales[row[1]] = {}
    #     except IndexError:
    #         print("The program has troubles with the array indexes")
    
    for row in sreader2:
        try:
            if (row[3] == '1'):
                if row[1] in diccfemales.keys():
                    diccfemales[row[1]] = int(diccfemales[row[1]]) + 1
                else:
                    diccfemales[row[1]] = 1
            elif (row[3] == '2'):
                if row[1] in diccmales.keys():
                    diccmales[row[1]] = int(diccmales[row[1]]) + 1
                else:
                    diccmales[row[1]] = 1
        except IndexError:
            print("The program has troubles with the array indexes")

    filefem = open(outfemales, 'w')
    filemal = open(outmales, 'w')
            
    for i in diccfemales.keys():
        filefem.write(str(i) + "," + str(diccfemales[i]) + "\n")
    for j in diccmales.keys():
        filemal.write(str(j) + "," + str(diccmales[j]) + "\n")        

filefem.close()
filemal.close()
