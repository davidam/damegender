#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,


import codecs
import csv
import re

with codecs.open('turkish.males.orig.csv', 'r', encoding='utf8') as file:
    input = csv.reader(file, delimiter=";", quotechar='|')
    # creating a list where save name and frequencies
    l0 = []
    count = 0
    for row in input:
        print(count)        
        print(row)
        # we need skip the first rows
        if (count > 3):
            count2 = 0
            # creating a list with all frequencies
            # (all years)
            l1 = row[1:len(row)]
            # now sum all years in count2
            print(l1)
            for i in l1:
                if (i == ""):
                    i = 0
                print(i)
                count2 = int(count2) + int(i)  
            l0.append([row[0], count2])
        print(l0)
        count = count + 1
l2 = l0[0:-4]

malesoutput = "trmales.csv"

# now we write name and freq in the file from the list
with open(malesoutput, 'w', encoding='utf8') as fo:
    count = 1
    for i in l2:
        if (count > 0):
            name = str(i[0])
            freq = str(i[1])
            if (freq == ""):
                freq = "0"
            if (name != ""):
                fo.write(name + "," + freq + "\n")
        count = count +1
    fo.close()
