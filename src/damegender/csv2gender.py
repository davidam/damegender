#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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

# DESCRIPTION: Given a csv file with a column of names returns a files
# with a new column with gender for each name


from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument('--first_name_position', required=True,
                    type=int, choices=[0, 1, 2, 3, 4], default=0)
# What is the position of the first name in the csv?
parser.add_argument('--surname_position', required=False,
                    type=int, choices=[0, 1, 2, 3, 4], default=-99999)
# What is the position of the surname in the csv?
parser.add_argument('--delimiter_csv', required=False,
                    type=str, default=",")
# Is the csv separated by commas?
parser.add_argument('--dataset', default="us",
                    choices=['ar', 'at', 'au', 'be', 'ca', 'ch', 'cn', 'de',
                             'dk', 'es', 'fi', 'fr', 'gb', 'ie', 'ine',
                             'inter', 'is', 'mx', 'no', 'nz', 'pt',
                             'ru', 'ru_en', 'ru_ru', 'se', 'si', 'uy',
                             'us', 'genderguesser'])
parser.add_argument('--outcsv', default="files/names/out.csv")
parser.add_argument('--outjson', default="files/names/out.json")
parser.add_argument('--outimg', default="files/images/csv2gender.png")
parser.add_argument('--title', default="People grouped by gender")
# display a title for the matplotlib graph
parser.add_argument('--noshow', dest='noshow', action='store_true')
# no show the graph deployed with matplotlib
parser.add_argument('--skip_header', dest='skip_header', action='store_true')
# the first row in the csv file is excluded
parser.add_argument('--guess_with_first_name_strict',
                    dest='guess_with_first_name_strict',
                    action='store_true')
# only the first word in the first name is used to guess the gender
# it can be valid in dataset with names in english, spanish and other languages
parser.add_argument('--delete_duplicated', dest='delete_duplicated',
                    action='store_true')
parser.add_argument('--respect_accents', dest='respect_accents',
                    action='store_true')
parser.add_argument('--force_whitespaces', dest='force_whitespaces',
                    action='store_true')
parser.add_argument('--verbose', dest='verbose', action='store_true')
parser.add_argument('--version', action='version', version='0.4')
args = parser.parse_args()


first_name_position = int(args.first_name_position)
surname_position = int(args.surname_position)
du = DameUtils()
s = Gender()

males = 0
females = 0
unknows = 0

males_list = []
females_list = []
unknows_list = []

# warnings
if (first_name_position == surname_position):
    print("WARNING:")
    print("First name and surname has the same position")
    print("First name: %s" % int(args.first_name_position))
    print("Surname: %s" % int(args.surname_position))
    print("It's not being generated the surname field in the output")


if (args.skip_header):
    csvrowlist = du.csv2list(args.path, quotechar=args.delimiter_csv)
else:
    csvrowlist = du.csv2list(args.path,
                             quotechar=args.delimiter_csv,
                             header=False)

l1 = []
for i in csvrowlist:
    if (len(i) > 1) and isinstance(i, list):
        ii = i
    elif (len(i) == 1) and isinstance(i, list):
        ii = i[0].split(args.delimiter_csv)
    try:
        original_first_name_string = ii[first_name_position]
        first_name_string = original_first_name_string
        first_name_string = first_name_string.upper()
        if (args.guess_with_first_name_strict):
            l2 = str(first_name_string).split(" ")
            first_name_string = l2[0]
        first_name_string = du.drop_quotes(first_name_string)
        first_name_string = first_name_string.encode('utf-8')
        surname_string = ""
        if (surname_position != -99999):
            surname_string = du.drop_quotes(ii[surname_position])
            surname_string = surname_string.encode('utf-8')
        if (args.respect_accents):
            sex = s.guess(
                first_name_string.decode('utf-8'),
                binary=False,
                drop_accents=False,
                force_whitespaces=args.force_whitespaces,
                dataset=args.dataset)
        else:
            sex = s.guess(
                first_name_string.decode('utf-8'),
                binary=False,
                force_whitespaces=args.force_whitespaces,
                dataset=args.dataset)
        if (sex == "male"):
            males_list.append(first_name_string)
        elif (sex == "female"):
            females_list.append(first_name_string)
        else:
            unknows_list.append(first_name_string)
        l1.append([original_first_name_string, sex, surname_string])

    except IndexError:
        print("Troubles with row ... %s " % i)
        print(ii)

file = open(args.outcsv, "w")
for i in l1:
    file.write(str(i[0]) + "," + str(i[1]) + "\n")

file.close()

file = open(args.outjson, "w")
file.write("[")
for i in l1:
    if (l1[0] == i):
        file.write("{\n")
    file.write('"name": "' + str(i[0]) + '",\n')
    bool1 = (int(args.first_name_position) != int(args.surname_position))
    bool2 = (args.surname_position != -99999)
    if bool1 and bool2:
        file.write('"surname": "' + surname_string.decode('utf-8') + '",\n')
    file.write('"gender": "' + str(i[1]) + '"\n')
    if (l1[-1] == i):
        file.write("}\n")
    else:
        file.write("}, {\n")
file.write("]\n")

file.close()


if (args.delete_duplicated):
    males_list = du.delete_duplicated(males_list)
    females_list = du.delete_duplicated(females_list)
    unknows_list = du.delete_duplicated(unknows_list)

if (len(sys.argv) > 1):
    print("---------------------------------------------------------------")
    print("The number of males in %s is %s" %
          (str(args.path), str(len(males_list))))
    if ((args.verbose) and (len(males_list) > 0)):
        print("the males list:")
        for i in males_list:
            print(i.decode('utf8'))

    print("---------------------------------------------------------------")
    print("The number of females in %s is %s" %
          (str(args.path), str(len(females_list))))
    if ((args.verbose) and (len(females_list) > 0)):
        print("the females list:")
        for i in females_list:
            print(i.decode('utf8'))

    print("---------------------------------------------------------------")
    print("The number of gender not recognised in %s is %s" %
          (str(args.path), str(len(unknows_list))))
    if ((args.verbose) and (len(unknows_list) > 0)):
        print("the unknowns list:")
        for i in unknows_list:
            print(i.decode('utf8'))


nmales = len(males_list)
nfemales = len(females_list)
nunknows = len(unknows_list)

data = [nmales, nfemales, nunknows]
gender = ["Males: " + str(nmales),
          "Females: " + str(nfemales),
          "Unknows: " + str(nunknows)]
plt.title(args.title)
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.axis("equal")

if (args.noshow):
    plt.savefig(args.outimg)
else:
    plt.savefig(args.outimg)
    plt.show()
