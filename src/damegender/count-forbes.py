#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv
import unicodedata
import unidecode
from pprint import pprint
import re
from app.dame_gender import Gender
from app.dame_utils import DameUtils

du = DameUtils()
g = Gender()


result=""
dm = []

with open('files/forbes2020.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    aux = ""
    cnt = 0
    for row in reader:
        cnt = cnt +1
#        print(row[0])
        if (aux != row[0]):
            dm.append(row[0])
        aux = row[0]

    #print(dm)
    #print(len(dm))
    #print(cnt)

print("Perhaps you need wait some minutes. You can take a tea or coffe now")

females = 0
males = 0
unknowns = 0
for rowdm in dm:
    sex = g.guess(rowdm.upper(), binary=False)
    
    if (sex == 'female'):
        females = females + 1
    elif (sex == 'male'):
        males = males + 1
    else:
        unknowns = unknowns + 1
        
print("this forbes list is about %s people" % len(dm))        
print("forbes males: %s" % males)
print("forbes females: %s" % females)
print("forbes not classified people: %s" % unknowns)

csvfile.close()
