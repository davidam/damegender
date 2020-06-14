#!/usr/bin/python3
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

from operator import itemgetter, attrgetter
from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import os
import re
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("country", default="usa", choices=['au', 'ca', 'es', 'fi', 'ie', 'ine', 'is', 'nz', 'pt', 'uy', 'uk', 'us', 'usa'], help="Countries with 2 letter, example, es is Spain")
parser.add_argument('--number', default=10)
parser.add_argument('--sex', default="female", choices=["male", "female", "all"])
parser.add_argument('--reverse', default=False, action="store_true")
#parser.add_argument('--less', default=False, action="store_less")
#parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

results = []

g = Gender()
du = DameUtils()

# MALES
def c2l(csvpath):
    l = []
    with open(csvpath) as csvfile:
        sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in sexreader:
            l.append([row[0], int(row[1])])
    return l

#c2l = c2l("files/names/names_au/baby-names-1944-2013/aumales.csv")

def getKey0str(item):
    return item[0]

def getKey1(item):
    return int(item[1])


if (args.country == "au"):
    c2lmales = du.csv2list("files/names/names_au/baby-names-1944-2013/aumales.csv")
elif (args.country == "ca"):
    c2lmales = du.csv2list("files/names/names_ca/camales.csv")
elif ((args.country == "es") | (args.country == "ine")):
    c2lmales = du.csv2list("files/names/names_es/esmasculinos.csv", header=True)
elif (args.country == "fi"):
    c2lmales = du.csv2list("files/names/names_fi/fimales.csv")
elif (args.country == "ie"):
    c2lmales = du.csv2list("files/names/names_ie/iemales.csv")
elif (args.country == "is"):
    c2lmales = du.csv2list("files/names/names_is/ismales.csv")
elif (args.country == "nz"):
    c2lmales = du.csv2list("files/names/names_nz/nzmales.csv")
elif (args.country == "pt"):
    c2lmales = du.csv2list("files/names/names_pt/ptmales.csv")
elif (args.country == "uy"):
    c2lmales = du.csv2list("files/names/names_uy/uymales.csv")
elif (args.country == "uk"):
    c2lmales = du.csv2list("files/names/names_uk/ukmales.csv")
elif ((args.country == "usa") | (args.country == "usa")):
    c2lmales = du.csv2list("files/names/names_us/usmales.csv")

if (args.reverse):    
    c2lmales = sorted(c2lmales, key=getKey1)
else:
    c2lmales = sorted(c2lmales, key=getKey1, reverse=True)
# FEMALES

if (args.country == "au"):
    c2lfemales = du.csv2list("files/names/names_au/baby-names-1944-2013/aufemales.csv")
elif (args.country == "ca"):
    c2lfemales = du.csv2list("files/names/names_ca/cafemales.csv")
elif ((args.country == "es") | (args.country == "ine")):
    c2lfemales = du.csv2list("files/names/names_es/esfemeninos.csv", header=True)
elif (args.country == "fi"):
    c2lfemales = du.csv2list("files/names/names_fi/fifemales.csv")
elif (args.country == "ie"):
    c2lfemales = du.csv2list("files/names/names_ie/iefemales.csv")
elif (args.country == "is"):
    c2lfemales = du.csv2list("files/names/names_is/isfemales.csv")
elif (args.country == "nz"):
    c2lfemales = du.csv2list("files/names/names_nz/nzfemales.csv")
elif (args.country == "pt"):
    c2lfemales = du.csv2list("files/names/names_pt/ptfemales.csv")
elif (args.country == "uy"):
    c2lfemales = du.csv2list("files/names/names_uy/uyfemales.csv")
elif (args.country == "uk"):
    c2lfemales = du.csv2list("files/names/names_uk/ukfemales.csv")
elif ((args.country == "usa") | (args.country == "usa")):
    c2lfemales = du.csv2list("files/names/names_us/usfemales.csv")

if (args.reverse):    
    c2lfemales = sorted(c2lfemales, key=getKey1)
else:
    c2lfemales = sorted(c2lfemales, key=getKey1, reverse=True)
    
n = int(args.number)
if (args.sex == "male"):

    for i in c2lmales[0:n]:
        print(i[0] + ": " + i[1])

elif (args.sex == "female"):        

    for i in c2lfemales[0:n]:
        print(i[0] + ": " + i[1])

elif (args.sex == "all"):

    c2l = c2lfemales + c2lmales
    if (args.reverse):
        c2l = sorted(c2l, key=getKey1)
    else:
        c2l = sorted(c2l, key=getKey1, reverse=True)
    n = args.number
    for i in c2l[0:n]:
        print(i[0] + ": " + i[1])
    

