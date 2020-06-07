#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@libresoft>
# Maintainer: David Arroyo Menéndez <davidam@libresoft>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
# Boston, MA 02110-1301 USA,

import csv
import unicodedata
import unidecode
import re

from pprint import pprint
from app.dame_gender import Gender
from app.dame_utils import DameUtils
from ast import literal_eval
from app.dame_sexmachine import DameSexmachine

du = DameUtils()
g = Gender()
s = DameSexmachine()

with open('files/scientifics.txt') as f:
    mainlist = [list(literal_eval(line)) for line in f]

l = mainlist[0]

ll = []
for i in l:
    ll.append(i.split())


ten = ll[0:10]    
hundred = ll[0:100]
thousand = ll[0:1000]

x = 0
y = 0
males = 0
females = 0
for i in hundred:
    if (len(i[0]) == 1):
        x = x + 1
    else:
        sex = g.guess(i[0], binary=False)
        y = y +1
        if (sex == "male"):
            males = males + 1
        elif (sex == "female"):
            females = females + 1

# print("Number of scientifics with a single letter as first name: %s" % x)
# print("Number of scientifics with the first name normal: %s" % y)

print("##### Checking for 100 scientifics ##########")
print("Number of females scientifics: %s" % females)
print("Number of males scientifics: %s" % males)

males = 0
females = 0

for j in thousand:
    if (len(j[0]) == 1):
        x = x + 1
    else:
        sex = g.guess(j[0], binary=False)
        y = y +1
        if (sex == "male"):
            males = males + 1
        else:
            females = females + 1

print("##### Checking for 1000 scientifics ##########")            
print("Number of females scientifics: %s" % females)
print("Number of males scientifics: %s" % males)
            
males = 0
females = 0

for k in ll:
    if (len(k[0]) == 1):
        x = x + 1
    else:
        sex = g.guess(k[0], binary=False)
        y = y +1
        if (sex == "male"):
            males = males + 1
        else:
            females = females + 1

print("##### Checking for all scientifics ##########")                        
print("Number of females scientifics: %s" % females)
print("Number of males scientifics: %s" % males)
            
