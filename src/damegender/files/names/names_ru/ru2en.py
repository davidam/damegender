
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
# along with Damegender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv
from transliterate import translit, get_available_language_codes

print("You must install transliterate to execute this script")
print("Try with:")
print("$ pip3 install transliterate")

with open('rufemales.csv') as csvfile:
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fo = open("rufemales.en.csv", "w")
    for row in sreader:
        print(translit(row[0], 'ru', reversed=True))
        fo.write(translit(row[0], 'ru', reversed=True) + ',' + row[1] + "\n")
    fo.close()

with open('rumales.csv') as csvfile:
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fo = open("rumales.en.csv", "w")
    for row in sreader:
        print(translit(row[0], 'ru', reversed=True))
        fo.write(translit(row[0], 'ru', reversed=True) + ',' + row[1] + "\n")
    fo.close()

