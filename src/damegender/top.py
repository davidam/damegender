#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is Free Software; you can redistribute it and/or modify
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


from __future__ import print_function
from operator import itemgetter, attrgetter
from app.dame_gender import Gender
from app.dame_utils import DameUtils

import sys
import os
import re
import argparse
import csv
import subprocess
import tempfile


parser = argparse.ArgumentParser()
parser.add_argument("country", default="usa",
                    choices=['at', 'au', 'be', 'ca', 'ch',
                             'dk', 'de', 'es', 'fr', 'fi',
                             'gb', 'ie', 'ine', 'inter',
                             'is', 'no', 'nz', 'mx', 'pt',
                             'ru', 'se', 'si', 'uy', 'uk',
                             'us', 'usa'],
                    help="Countries with 2 letter, example, es is Spain")
# More about iso codes on https://www.iso.org/obp/ui/
parser.add_argument('--number', default=10)
parser.add_argument('--sex', default="female",
                    choices=["male", "female", "all"])
parser.add_argument('--reverse', default=False, action="store_true")
parser.add_argument('--less', default=False, action="store_true")
parser.add_argument('--position', default=False, action="store_true")
parser.add_argument('--version', action='version', version='0.3')
args = parser.parse_args()

results = []

g = Gender()
du = DameUtils()


# PAGINATION STUFF
def printc(*largs, **kwargs):
    # The code can still use the usual file argument of print()
    if 'file' not in kwargs:
        # Forces the output to go to the temp file
        kwargs['file'] = tmp_file
    print(*largs, **kwargs)


# Definition of a printc() function
# that prints to the correct output
if args.less:
    # No need to store the name in a specific variable
    tmp_file = open(tempfile.mkstemp()[1], 'w')
else:
    # Regular print
    printc = print


# MALES
def c2l(csvpath):
    l1 = []
    with open(csvpath) as csvfile:
        sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in sexreader:
            l1.append([row[0], int(row[1])])
    return l1


def getKey0str(item):
    return item[0]


def getKey1(item):
    return int(item[1])


du = DameUtils()
dicc_dataset_males = du.dicc_dataset("male")

if (args.country == "at"):
    c2lmales = du.csv2list(dicc_dataset_males["au"])
elif (args.country == "au"):
    c2lmales = du.csv2list(dicc_dataset_males["au"])
elif (args.country == "be"):
    c2lmales = du.csv2list(dicc_dataset_males["be"])
elif (args.country == "ca"):
    c2lmales = du.csv2list(dicc_dataset_males["ca"])
elif (args.country == "ch"):
    c2lmales = du.csv2list(dicc_dataset_males["ch"])
elif (args.country == "de"):
    c2lmales = du.csv2list(dicc_dataset_males["de"])
elif (args.country == "dk"):
    c2lmales = du.csv2list(dicc_dataset_males["dk"])
elif ((args.country == "es") | (args.country == "ine")):
    c2lmales = du.csv2list(dicc_dataset_males["es"])
elif (args.country == "fi"):
    c2lmales = du.csv2list(dicc_dataset_males["fi"])
elif (args.country == "fr"):
    c2lmales = du.csv2list(dicc_dataset_males["fr"])
elif (args.country == "ie"):
    c2lmales = du.csv2list(dicc_dataset_males["ie"])
elif (args.country == "inter"):
    c2lmales = du.csv2list(dicc_dataset_males["inter"])
elif (args.country == "is"):
    c2lmales = du.csv2list(dicc_dataset_males["is"])
elif (args.country == "no"):
    c2lmales = du.csv2list(dicc_dataset_males["no"])
elif (args.country == "nz"):
    c2lmales = du.csv2list(dicc_dataset_males["nz"])
elif (args.country == "mx"):
    c2lmales = du.csv2list(dicc_dataset_males["mx"])
elif (args.country == "pt"):
    c2lmales = du.csv2list(dicc_dataset_males["pt"])
elif (args.country == "ru"):
    c2lmales = du.csv2list(dicc_dataset_males["ru"])
elif (args.country == "se"):
    c2lmales = du.csv2list(dicc_dataset_males["se"])
elif (args.country == "si"):
    c2lmales = du.csv2list(dicc_dataset_males["si"])
elif (args.country == "uy"):
    c2lmales = du.csv2list(dicc_dataset_males["uy"])
elif ((args.country == "uk") or (args.country == "gb")):
    c2lmales = du.csv2list(dicc_dataset_males["gb"])
elif ((args.country == "usa") | (args.country == "us")):
    c2lmales = du.csv2list(dicc_dataset_males["us"])

if (args.reverse):
    c2lmales = sorted(c2lmales, key=getKey1)
else:
    c2lmales = sorted(c2lmales, key=getKey1, reverse=True)

# FEMALES

dicc_dataset_females = du.dicc_dataset("female")

if (args.country == "at"):
    c2lfemales = du.csv2list(dicc_dataset_females["at"])
elif (args.country == "au"):
    c2lfemales = du.csv2list(dicc_dataset_females["au"])
elif (args.country == "be"):
    c2lfemales = du.csv2list(dicc_dataset_females["be"])
elif (args.country == "ca"):
    c2lfemales = du.csv2list(dicc_dataset_females["ca"])
elif (args.country == "ch"):
    c2lfemales = du.csv2list(dicc_dataset_females["ch"])    
elif (args.country == "de"):
    c2lfemales = du.csv2list(dicc_dataset_females["de"])    
elif (args.country == "dk"):
    c2lfemales = du.csv2list(dicc_dataset_females["dk"])
elif ((args.country == "es") | (args.country == "ine")):
    c2lfemales = du.csv2list(dicc_dataset_females["es"], header=False)
elif (args.country == "fi"):
    c2lfemales = du.csv2list(dicc_dataset_females["fi"])
elif (args.country == "fr"):
    c2lfemales = du.csv2list(dicc_dataset_females["fr"])    
elif ((args.country == "gb") or (args.country == "uk")):
    c2lfemales = du.csv2list(dicc_dataset_females["gb"])
elif (args.country == "ie"):
    c2lfemales = du.csv2list(dicc_dataset_females["ie"])
elif (args.country == "inter"):
    c2lfemales = du.csv2list(dicc_dataset_females["inter"])
elif (args.country == "is"):
    c2lfemales = du.csv2list(dicc_dataset_females["is"])
elif (args.country == "no"):
    c2lfemales = du.csv2list(dicc_dataset_females["no"])
elif (args.country == "nz"):
    c2lfemales = du.csv2list(dicc_dataset_females["nz"])
elif (args.country == "mx"):
    c2lfemales = du.csv2list(dicc_dataset_females["mx"])    
elif (args.country == "pt"):
    c2lfemales = du.csv2list(dicc_dataset_females["pt"])
elif (args.country == "ru"):
    c2lfemales = du.csv2list(dicc_dataset_females["ru"])    
elif (args.country == "se"):
    c2lfemales = du.csv2list(dicc_dataset_females["se"])
elif (args.country == "si"):
    c2lfemales = du.csv2list(dicc_dataset_females["si"])
elif (args.country == "uy"):
    c2lfemales = du.csv2list(dicc_dataset_females["uy"])
elif ((args.country == "usa") | (args.country == "us")):
    c2lfemales = du.csv2list(dicc_dataset_females["us"])

if (args.reverse):
    c2lfemales = sorted(c2lfemales, key=getKey1)
else:
    c2lfemales = sorted(c2lfemales, key=getKey1, reverse=True)

n = int(args.number)

if (args.less and (args.sex == 'female')):
    n = len(c2lfemales)
elif (args.less and (args.sex == 'male')):
    n = len(c2lmales)
elif (args.less and (args.sex == 'all')):
    n = len(c2lmales) + len(c2lfemales)

if (args.sex == "male"):
    position = 1
    for i in c2lmales[0:n]:
        if args.less:
            if args.position:
                printc(str(position) + ") " + i[0] + ": " + i[1], sep='/')
            else:
                printc(i[0] + ": " + i[1], sep='/')
        else:
            if args.position:
                print(str(position) + ") " + i[0] + ": " + i[1])
            else:
                print(i[0] + ": " + i[1])
        position = position + 1

elif (args.sex == "female"):
    position = 1
    for i in c2lfemales[0:n]:
        if args.less:
            if args.position:
                printc(str(position) + ") " + i[0] + ": " + i[1], sep='/')
            else:
                printc(i[0] + ": " + i[1], sep='/')
        else:
            if args.position:
                print(str(position) + ") " + i[0] + ": " + i[1])
            else:
                print(i[0] + ": " + i[1])
        position = position + 1

elif (args.sex == "all"):

    c2l = c2lfemales + c2lmales
    if (args.reverse):
        c2l = sorted(c2l, key=getKey1)
    else:
        c2l = sorted(c2l, key=getKey1, reverse=True)

    position = 1
    for i in c2l[0:n]:
        if args.less:
            if args.position:
                printc(str(position) + ") " + i[0] + ": " + i[1], sep='/')
            else:
                printc(i[0] + ": " + i[1], sep='/')
        else:
            if args.position:
                print(str(position) + ") " + i[0] + ": " + i[1])
            else:
                print(i[0] + ": " + i[1])
        position = position + 1

# Paging of the current contents of the temp file:
if args.less:
    tmp_file.flush()  # No need to close the file: you can keep printing to it
    subprocess.call(['less', tmp_file.name])  # Simpler than a full Popen()
