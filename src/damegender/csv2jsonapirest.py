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

# DESCRIPTION: Given a csv file in the damegender format (column 0
# with names and column 1 with frequencies) returns one or multiple
# json files

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import argparse
import re

parser = argparse.ArgumentParser()
# Path is the path with the csv file of names.
# For example, files/names/names_fi/fifemales.csv
parser.add_argument("path", help="csv file")
# The path and name file where the json file is stored
parser.add_argument("--outjson",
                    default="files/names/out.json",
                    help="json file")
# The path and directory name file where the json files is stored
parser.add_argument("--outdir",
                    default="files/names/",
                    help="json file")
# You can decide include or not the csv header in the operation
parser.add_argument('--skip_header',
                    dest='skip_header',
                    action='store_true')
# By default split the csv with 1 name per json file
parser.add_argument('--names_by_multiple_files', default=1)
parser.add_argument('--gender',
                    required=True,
                    choices=["male", "female", "all"])

args = parser.parse_args()

du = DameUtils()
s = Gender()

if (args.skip_header):
    csvlist = du.csv2list(args.path, header=True)
else:
    csvlist = du.csv2list(args.path, header=False)

if (args.gender == "all"):
    str1 = "You must use damegender csv files "
    str1 = str1 + "such as files/names/names_be/beall.csv"
    print(str1)
elif (args.gender == "female"):
    str2 = "You must use damegender csv files "
    str2 = str2 + "such as files/names/names_be/befemales.csv"
    print(str2)
elif (args.gender == "male"):
    str3 = "You must use damegender csv files "
    str3 = str3 + "such as files/names/names_be/bemales.csv"
    print(str3)
# print(csvlist)

if (int(args.names_by_multiple_files) == 1):
    for i in csvlist:
        name = str(i[0].upper())
        name = du.white_space_inside_by(name, "_")
        name = re.sub(r'\-', r'_', name)
        name = re.sub(r'\/', r'', name)
        jsonfile = args.outdir + "/" + name
        jsonfile = jsonfile + "_" + args.gender + ".json"
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
elif (int(args.names_by_multiple_files) > 1):
    cnt1 = 0
    n = len(csvlist)
    print(n)
    while (cnt1 < n):
        cnt2 = 0
        jsonfile = args.outdir + "/" + str(cnt1) + "_" + args.gender + ".json"
        file = open(jsonfile, "w")
        file.write('[{\n')
        while (cnt2 < int(args.names_by_multiple_files)):
            try:
                i = cnt1 + cnt2
                varname = str(csvlist[i][0].upper())
                print(varname)
                varfrequency = str(csvlist[i][1])
                print(varfrequency)
                if (args.gender == "all"):
                    varmales = str(csvlist[i][2])
                    print(varmales)
                    varfemales = str(csvlist[i][3])
                    print(varfemales)
                else:
                    vargender = str(args.gender)
                    print(vargender)
            except IndexError:
                print("The program has troubles with the array: " + str(i))
            file.write('[\n')
            file.write('"name": "' + varname + '",\n')
            file.write('"frequency": ' + varfrequency + ',\n')
            file.write('"gender": "' + vargender + '"\n')
            if (cnt2 == (int(args.names_by_multiple_files) - 1)):
                file.write(']\n')
            else:
                file.write('],\n')
            cnt2 = cnt2 + 1
        file.write('}]\n')
        file.close()
        cnt2 = 0
        cnt1 = cnt1 + 1

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
    file.write(']')
    file.close()
