#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

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

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument("--outjson", default="files/names/out.json", help="json file")
parser.add_argument("--outdir", default="files/names/", help="json file")
parser.add_argument('--skip_header', dest='skip_header', action='store_true')
parser.add_argument('--multiple_files', dest='multiple_files', action='store_true')
parser.add_argument('--gender', choices=["male", "female", "all"])

args = parser.parse_args()

du = DameUtils()
s = Gender()

if (args.skip_header):
    csvlist = du.csv2list(args.path, header=True)
else:
    csvlist = du.csv2list(args.path, header=False)

if (args.gender == "all"):
    print("You must use damegender csv files such as files/names/names_be/beall.csv")
elif (args.gender == "female"):
    print("You must use damegender csv files such as files/names/names_be/befemales.csv")
elif (args.gender == "male"):
    print("You must use damegender csv files such as files/names/names_be/bemales.csv")    
# print(csvlist)

if (args.multiple_files):
    cnt = 0
    for i in csvlist:
        jsonfile = args.outdir + "/" + str(i[0].upper()) + "_" + args.gender + ".json"
        file = open(jsonfile, "w")
        try:
            varname = str(i[0].upper())
            varfrequency = str(i[1])
            if (args.gender == "all"):
                varmales = str(i[2])
                varfemales = str(i[3])
            else:
                vargender = str(args.gender)
        except IndexError:
            print("The program has troubles with the array: " + str(i))
            file.close()

        file.write('[{\n')
        file.write('"name": "' + str(i[0].upper()) + '",\n')
        file.write('"frequency": ' + str(i[1]) + ',\n')
        if (args.gender == "all"):
            file.write('"males": "' + str(i[2]) + ' %",\n')
            file.write('"females": "' + str(i[3]) + ' %"\n')            
        else:
            file.write('"gender": "' + str(args.gender) + '"\n')
        file.write('}]\n')
        file.close()
else:
    file = open(str(args.outjson), "w")
    file.write('[')
    cnt = 0
    for i in csvlist:
        try:
            varname = str(i[0].upper())
            varfrequency = str(i[1])
            if (args.gender == "all"):
                varmales = str(i[2])
                varfemales = str(i[3])
            else:
                vargender = str(args.gender)
        except IndexError:
            print("The program has troubles with the array: " + str(i))
            file.close()
        file.write('{\n')
        file.write('"name": "' + varname + '",\n')
        file.write('"frequency": ' + varfrequency + ',\n')
        if (args.gender == "all"):
            file.write('"males": "' + varmales + ' %",\n')
            file.write('"females": "' + varfemales + ' %"\n')            
        else:
            file.write('"gender": "' + vargender + '"\n')        
        cnt = cnt + 1
        if (len(csvlist) == cnt):
            file.write('}\n')
        else:
            file.write('},\n')
    file.write(']');
    file.close()
