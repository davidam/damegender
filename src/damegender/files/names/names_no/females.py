#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
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

with codecs.open('Personer_20211003-224940.csv', 'r', encoding='utf8') as file:
    input = csv.reader(file, delimiter=";", quotechar='|')
    list = []
    count = 0
    for row in input:
        if (count > 1):
            list.append([row[0], row[-1]])
        count = count + 1
        print(count)
#print(list)

femalesoutput = "nofemales.csv"

with open(femalesoutput, 'w', encoding='utf8') as fo:
    count = 0
    for i in list:
        if (count > 0):
            name = str(i[0].replace('"', ''))
            freq = str(i[1].replace('"', ''))
            freq = re.sub(r'(\.)', r'0', freq)
            if (name != ""):
                fo.write(name + "," + freq + "\n")
        count = count +1
    fo.close()
