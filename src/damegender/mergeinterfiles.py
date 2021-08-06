#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

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
    if (args.malefemale):
        frec_file1 = int(dg.name_frec_from_file(k, args.file1))
        frec_file2 = int(dg.name_frec_from_file(k, args.file2))
        if ((frec_file1 > 0) or (frec_file2 > 0)):
            percentage_file1 = (frec_file1 / (frec_file1 + frec_file2)) * 100
            percentage_file2 = (frec_file2 / (frec_file1 + frec_file2)) * 100
            line = k + "," + str(dicc[k]) + "," + str(percentage_file1) + "," + str(percentage_file2) + "\n"
        else:
            line = k + "," + str(dicc[k]) + "\n"        
    else:
        line = k + "," + str(dicc[k]) + "\n"        
    file.write(line)

file.close()
