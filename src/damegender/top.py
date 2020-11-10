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



from __future__ import print_function
from operator import itemgetter, attrgetter
from app.dame_gender import Gender
from app.dame_utils import DameUtils

import sys
import os
import re
import argparse
import csv
import subprocess, tempfile


parser = argparse.ArgumentParser()
parser.add_argument("country", default="usa", choices=['all', 'au', 'ca', 'es', 'fi', 'ie', 'ine', 'is', 'nz', 'pt', 'uy', 'uk', 'us', 'usa'], help="Countries with 2 letter, example, es is Spain")
parser.add_argument('--number', default=10)
parser.add_argument('--sex', default="female", choices=["male", "female", "all"])
parser.add_argument('--reverse', default=False, action="store_true")
parser.add_argument('--less', default=False, action="store_true")
parser.add_argument('--position', default=False, action="store_true")
#parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

results = []

g = Gender()
du = DameUtils()

# PAGINATION STUFF

#page = True  # For tests

# Definition of a printc() function that prints to the correct output
if args.less:
    tmp_file = open(tempfile.mkstemp()[1], 'w')  # No need to store the name in a specific variable
    def printc(*largs, **kwargs):
        if 'file' not in kwargs:  # The code can still use the usual file argument of print()
            kwargs['file'] = tmp_file  # Forces the output to go to the temp file
        print(*largs, **kwargs)
else:
    printc = print  # Regular print




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
    c2lmales = du.csv2list("files/names/names_fi/fimales.csv", header=True)
elif (args.country == "ie"):
    c2lmales = du.csv2list("files/names/names_ie/iemales.csv")
elif (args.country == "is"):
    c2lmales = du.csv2list("files/names/names_is/ismales.csv")
elif (args.country == "nz"):
    c2lmales = du.csv2list("files/names/names_nz/nzmales.csv")
elif (args.country == "pt"):
    c2lmales = du.csv2list("files/names/names_pt/ptmales.csv")
elif (args.country == "uy"):
    c2lmales = du.csv2list("files/names/names_uy/uymasculinos.csv", header=True)
elif (args.country == "uk"):
    c2lmales = du.csv2list("files/names/names_uk/ukmales.csv", header=True)
elif ((args.country == "usa") | (args.country == "us")):
    c2lmales = du.csv2list("files/names/names_us/usmales.csv", header=True)
elif (args.country == "all"):
    c2lmales = du.csv2list("files/names/names_au/baby-names-1944-2013/aufemales.csv")
    c2lmales = c2lmales + du.csv2list("files/names/names_ca/cafemales.csv")
    c2lmales = c2lmales + du.csv2list("files/names/names_es/esfemeninos.csv", header=True)
    c2lmales = c2lmales + du.csv2list("files/names/names_fi/fifemales.csv", header=True)
    c2lmales = c2lmales + du.csv2list("files/names/names_ie/iefemales.csv")
    c2lmales = c2lmales + du.csv2list("files/names/names_is/isfemales.csv")
    c2lmales = c2lmales + du.csv2list("files/names/names_nz/nzfemales.csv")
    c2lmales = c2lmales + du.csv2list("files/names/names_pt/ptfemales.csv")
    c2lmales = c2lmales + du.csv2list("files/names/names_uy/uyfemeninos.csv", header=True)
    c2lmales = c2lmales + du.csv2list("files/names/names_uk/ukfemales.csv", header=True)
    c2lmales = c2lmales + du.csv2list("files/names/names_us/usfemales.csv", header=True)

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
    c2lfemales = du.csv2list("files/names/names_fi/fifemales.csv", header=True)
elif (args.country == "ie"):
    c2lfemales = du.csv2list("files/names/names_ie/iefemales.csv")
elif (args.country == "is"):
    c2lfemales = du.csv2list("files/names/names_is/isfemales.csv")
elif (args.country == "nz"):
    c2lfemales = du.csv2list("files/names/names_nz/nzfemales.csv")
elif (args.country == "pt"):
    c2lfemales = du.csv2list("files/names/names_pt/ptfemales.csv")
elif (args.country == "uy"):
    c2lfemales = du.csv2list("files/names/names_uy/uyfemeninos.csv", header=True)
elif (args.country == "uk"):
    c2lfemales = du.csv2list("files/names/names_uk/ukfemales.csv", header=True)
elif ((args.country == "usa") | (args.country == "us")):
    c2lfemales = du.csv2list("files/names/names_us/usfemales.csv", header=True)
elif (args.country == "all"):
    c2lfemales = du.csv2list("files/names/names_au/baby-names-1944-2013/aufemales.csv")
    c2lfemales = c2lfemales + du.csv2list("files/names/names_ca/cafemales.csv")
    c2lfemales = c2lfemales + du.csv2list("files/names/names_es/esfemeninos.csv", header=True)
    c2lfemales = c2lfemales + du.csv2list("files/names/names_fi/fifemales.csv", header=True)
    c2lfemales = c2lfemales + du.csv2list("files/names/names_ie/iefemales.csv")
    c2lfemales = c2lfemales + du.csv2list("files/names/names_is/isfemales.csv")
    c2lfemales = c2lfemales + du.csv2list("files/names/names_nz/nzfemales.csv")
    c2lfemales = c2lfemales + du.csv2list("files/names/names_pt/ptfemales.csv")
    c2lfemales = c2lfemales + du.csv2list("files/names/names_uy/uyfemeninos.csv", header=True)
    c2lfemales = c2lfemales + du.csv2list("files/names/names_uk/ukfemales.csv", header=True)
    c2lfemales = c2lfemales + du.csv2list("files/names/names_us/usfemales.csv", header=True)
    c2lfemales = sorted(c2lfemales, key=getKey1)
    
if (args.reverse):    
    c2lfemales = sorted(c2lfemales, key=getKey1)
else:
    c2lfemales = sorted(c2lfemales, key=getKey1, reverse=True)

n = int(args.number)    

if (args.less and (args.sex=='female')):
    n = len(c2lfemales)
elif (args.less and (args.sex=='male')):    
    n = len(c2lmales)    
elif (args.less and (args.sex=='all')):
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
