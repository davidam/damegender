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
import argparse

from app.dame_gender import Gender
from app.dame_utils import DameUtils

parser = argparse.ArgumentParser()
parser.add_argument('--show', choices=['males', 'females', 'unknowns', 'all'])
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

du = DameUtils()
g = Gender()


result=""
dm = []

with open('files/linux-maintainers.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    aux = ""
    cnt = 0
    for row in reader:
        cnt = cnt +1
#        print(row[0])
        if (aux != row[0]):
            dm.append(row[0])
        aux = row[0]

print("Perhaps you need wait some minutes. You can take a tea or coffe now")

females = 0
males = 0
unknowns = 0

list_males = []
list_females = []
list_unknowns = []
for rowdm in dm:
    listfullname = rowdm.split()
    name = listfullname[0]
    sex = g.guess(name.upper(), binary=False)
    
    if (sex == 'female'):
        females = females + 1
        list_females.append(name)
    elif (sex == 'male'):
        males = males + 1
        list_males.append(name)        
    else:
        unknowns = unknowns + 1
        list_unknowns.append(name)
        
print("this kernel maintainers list is about %s people" % len(dm))        
print("kernel maintainers males: %s" % males)
print("kernel maintainers females: %s" % females)
print("kernel maintainers not classified: %s" % unknowns)

if ((args.show=='males') or (args.show=='all')):
    print("The list of kernel maintainers males:" % list_males)
    print(list_males)
    
if ((args.show=='females') or (args.show=='all')):
    print("The list of kernel maintainers females:" % list_females)
    print(list_females)
    
if ((args.show=='unknowns') or (args.show=='all')):
    print("The list of people with unknown gender as kernel maintainers:" % list_unknowns)
    print(list_unknowns)

csvfile.close()
