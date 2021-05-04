#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument('--first_name_position', required=True, type=int, choices=[0, 1, 2, 3, 4], default=0)
parser.add_argument('--dataset', default="us", choices=['at', 'au', 'be', 'ca', 'de', 'dk', 'es', 'fi', 'gb', 'ie', 'ine', 'inter', 'is', 'mx', 'nz', 'pt', 'si', 'uy', 'us', 'genderguesser'])
parser.add_argument('--outcsv', default="files/names/out.csv")
parser.add_argument('--outimg', default="files/images/csv2gender.png")
parser.add_argument('--title', default="People grouped by gender")
parser.add_argument('--noshow', dest='noshow', action='store_true')
parser.add_argument('--skip_header', dest='skip_header', action='store_true')
parser.add_argument('--delete_duplicated', dest='delete_duplicated', action='store_true')
parser.add_argument('--verbose', dest='verbose', action='store_true')
parser.add_argument('--version', action='version', version='0.3')
args = parser.parse_args()


du = DameUtils()
s = Gender()

males = 0
females = 0
unknows = 0

males_list = []
females_list = []
unknows_list = []

if (args.skip_header):
    nameslist = du.csvcolumn2list(args.path)
else:
    nameslist = du.csvcolumn2list(args.path, header=False)

l = []

for firstname in nameslist:
    firstname = du.drop_quotes(firstname)
    sex = s.guess(firstname, binary=False, dataset=args.dataset)
    if (sex == "male"):
        males_list.append(firstname)
    elif (sex == "female"):
        females_list.append(firstname)
    else:
        unknows_list.append(firstname)
    l.append([firstname, sex])

file = open(args.outcsv, "w")
for i in l:
    file.write(str(i[0])+","+str(i[1]) + "\n")

file.close()

if (args.delete_duplicated):
    males_list = du.delete_duplicated(males_list)
    females_list = du.delete_duplicated(females_list)
    unknows_list = du.delete_duplicated(unknows_list)

if (len(sys.argv) > 1):
    print("------------------------------------------------------------------------")
    print("The number of males in %s is %s" % (str(args.path), str(len(males_list))))
    if ((args.verbose) and (len(males_list) >0)):
        print("the males list:")
        for i in males_list:
           print(i)

    print("------------------------------------------------------------------------")
    print("The number of females in %s is %s" % (str(args.path), str(len(females_list))))
    if ((args.verbose) and (len(females_list) >0)):
        print("the females list:")
        for i in females_list:
           print(i)

    print("------------------------------------------------------------------------")
    print("The number of gender not recognised in %s is %s" % (str(args.path), str(len(unknows_list))))
    if ((args.verbose) and (len(unknows_list) >0)):
        print("the unknowns list:")
        for i in unknows_list:
           print(i)



import matplotlib.pyplot as plt

nmales = len(males_list)
nfemales = len(females_list)
nunknows = len(unknows_list)

data = [nmales, nfemales, nunknows]
gender = ["Males: " + str(nmales),"Females: " + str(nfemales),"Unknows: " + str(nunknows)]
plt.title(args.title)
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.axis("equal")

if (args.noshow):
    plt.savefig(args.outimg)
else:
    plt.savefig(args.outimg)
    plt.show()
