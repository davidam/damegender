#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv

with open('gender_firstnames_ITA.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    file0 = open('gender_firstnames_ITA.onlygender.csv','w') 
    for row in spamreader:
        print(row)
        print(row[2])
        print(row[3])        
        if (int(row[2]) > int(row[3])):
            file0.write(row[0]+','+'male\n')
        elif (int(row[2]) == int(row[3])):
            file0.write(row[0]+','+'unknown\n')
        elif (int(row[2]) < int(row[3])):
            file0.write(row[0]+','+'female\n')            

# Cerramos el archivo fichero.txt
file0.close()


with open('gender_firstnames_ITA.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    file1 = open('gender_firstnames_ITA.males.csv','w')
    file2 = open('gender_firstnames_ITA.females.csv','w')
    file3 = open('gender_firstnames_ITA.all.csv','w')     
    for row in spamreader:
        file1.write(row[0]+','+row[2]+'\n')
        file2.write(row[0]+','+row[3]+'\n')        
        total = int(row[2]) + int(row[3])
        males_percentage = (int(row[2]) / total) * 100
        females_percentage = (int(row[3]) / total) * 100        
        file3.write(row[0]+','+ str(males_percentage) + ',' + str(females_percentage) + '\n')        

# Cerramos el archivo fichero.txt

file1.close()
file2.close()
file3.close()
