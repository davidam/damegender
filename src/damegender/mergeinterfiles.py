#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

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

# DESCRIPTION: Given two damegender csv files (column 0 with names and
# column 1 with frequencies) returns a file merging the files.


import csv
import argparse
from app.dame_utils import DameUtils
from app.dame_gender import Gender

parser = argparse.ArgumentParser()
parser.add_argument("--file1", help="display the gender")
parser.add_argument("--file2", help="display the gender")
parser.add_argument('--output', default="interfemales.csv")
parser.add_argument('--malefemale', default=False, action="store_true")
parser.add_argument('--verbose', default=False, action="store_true")
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()


# FEMALES #

ll = []

du = DameUtils()
dg = Gender()

li = du.csv2list(args.file1, header=False)
if (args.verbose):
    print(li)

lenli = len(li)
dicci = {}
for i in li:
    if i[0].upper() in dicci.keys():
        dicci[i[0].upper()] = int(dicci[i[0].upper()]) + int(i[1])
    else:
        dicci[i[0].upper()] = int(i[1])

if (args.verbose):
    print(lenli)

lj = du.csv2list(args.file2, header=False)
if (args.verbose):
    print(lj)

lenlj = len(lj)
diccj = {}
for i in lj:
    if i[0].upper() in diccj.keys():
        diccj[i[0].upper()] = int(diccj[i[0].upper()]) + int(i[1])
    else:
        diccj[i[0].upper()] = int(i[1])

if (args.verbose):
    print(lenlj)

ll = li + lj
if (args.verbose):
    print(ll)
    print(len(ll))

dicc = {}
for i in ll:
    if i[0].upper() in dicc.keys():
        dicc[i[0].upper()] = int(dicc[i[0].upper()]) + int(i[1])
    else:
        dicc[i[0].upper()] = int(i[1])

if (args.verbose):
    print(dicc)
    print(dicc.keys())
    print(dicc.values())
    print(len(dicc.keys()))

file = open(args.output, "w")
for k in dicc.keys():
    if (args.malefemale):
        frec_file1 = 0
        frec_file2 = 0
        if k in dicci:
            frec_file1 = dicci[k]
        else:
            frec_file1 = 0
        if k in diccj:
            frec_file2 = diccj[k]
        else:
            frec_file2 = 0
        if ((frec_file1 > 0) or (frec_file2 > 0)):
            percentage_file1 = (frec_file1 / (frec_file1 + frec_file2)) * 100
            percentage_file2 = (frec_file2 / (frec_file1 + frec_file2)) * 100
            line = k + "," + str(dicc[k]) + "," + str(percentage_file1)
            line = line + "," + str(percentage_file2) + "\n"
        elif ((frec_file1 == 0) and (frec_file2 == 0)):
            line = k + ",0,0,0\n"
        else:
            line = k + "," + str(dicc[k]) + "\n"
    else:
        line = k + "," + str(dicc[k]) + "\n"
    file.write(line)

file.close()
