#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file1", help="display the gender")
parser.add_argument("--file2", help="display the gender")
parser.add_argument('--output', default="interfemales.csv")
parser.add_argument('--verbose', default=False, action="store_true")
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()


######################################## FEMALES ######################

l = []

def csv2list(csvpath,  *args, **kwargs):
    # make a list from a csv file
    header = kwargs.get('header', False)
    delimiter = kwargs.get('delimiter', ',')
    l = []
    with open(csvpath) as csvfile:
        sexreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        if (header == True):
            next(sexreader, None)
        for row in sexreader:
            l.append(row)
    return l

li = csv2list(args.file1)
if (args.verbose):
    print(li)

lenli = len(li)
if (args.verbose):
    print(lenli)

lj = csv2list(args.file2)
if (args.verbose):
    print(lj)
lenlj = len(lj)

if (args.verbose):
    print(lenlj)

l = li + lj
if (args.verbose):
    print(l)
    print(len(l))

dicc = {}
for i in l:
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
