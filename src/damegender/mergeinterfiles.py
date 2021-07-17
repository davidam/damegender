#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

import csv
import argparse
from app.dame_utils import DameUtils

parser = argparse.ArgumentParser()
parser.add_argument("--file1", help="display the gender")
parser.add_argument("--file2", help="display the gender")
parser.add_argument('--output', default="interfemales.csv")
parser.add_argument('--verbose', default=False, action="store_true")
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()


# FEMALES #

ll = []

du = DameUtils()

li = du.csv2list(args.file1)
if (args.verbose):
    print(li)

lenli = len(li)
if (args.verbose):
    print(lenli)

lj = du.csv2list(args.file2)
if (args.verbose):
    print(lj)
lenlj = len(lj)

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
    line = k + "," + str(dicc[k]) + "\n"
    file.write(line)

file.close()
