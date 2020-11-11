#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.



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
unknows = 0
count = 0
for i in hundred:
    count = count +1
    if (len(i[0]) == 1):
        unknows = unknows + 1
    else:
        sex = g.guess(i[0], binary=False, dataset='es')
        if (sex == "male"):
            males = males + 1
        elif (sex == "female"):
            females = females + 1
        else:
            unknows = unknows + 1
# print("Number of scientifics with a single letter as first name: %s" % x)
# print("Number of scientifics with the first name normal: %s" % y)

print("##### Checking for 100 scientifics ##########")
print(count)
print("Number of females scientifics: %s" % females)
print("Number of males scientifics: %s" % males)
print("Number of scientifics with gender unknow: %s" % unknows)
print("In this dataset the gender unknow is due overall to use initials and not names")

males = 0
females = 0
unknows = 0
for j in thousand:
    if (len(j[0]) == 1):
        unknows = unknows + 1        
    else:
        sex = g.guess(j[0], binary=False, dataset='es')
        y = y +1
        if (sex == "male"):
            males = males + 1
        elif (sex == "female"):
            females = females + 1
        else:
            unknows = unknows + 1

print("##### Checking for 1000 scientifics ##########")            
print("Number of females scientifics: %s" % females)
print("Number of males scientifics: %s" % males)
print("Number of scientifics with gender unknow: %s" % unknows)
print("In this dataset the gender unknow is due overall to use initials and not names")
            
males = 0
females = 0
unknows = 0
for k in ll:
    if (len(k[0]) == 1):
        unknows = unknows + 1                
    else:
        sex = g.guess(k[0], binary=False, dataset='es')
        y = y +1
        if (sex == "male"):
            males = males + 1
        elif (sex == "female"):
            females = females + 1
        else:
            unknows = unknows + 1

print("##### Checking for all scientifics ##########")                        
print("Number of females scientifics: %s" % females)
print("Number of males scientifics: %s" % males)
print("Number of scientifics with gender unknow: %s" % unknows)
print("In this dataset the gender unknow is due overall to use initials and not names")

import matplotlib.pyplot as plt

data = [males, females, unknows]
gender = ["Males","Females","Unknows"]
plt.title("Scientific people grouped by gender")
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.axis("equal")
plt.savefig('files/images/scientifics_by_gender.png')
plt.show()
