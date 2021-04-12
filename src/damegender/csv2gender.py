#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument('--first_name_position', required=True, type=int, choices=[0, 1, 2, 3, 4], default=0)
parser.add_argument('--dataset', default="us", choices=['at', 'au', 'be', 'ca', 'de', 'dk', 'es', 'fi', 'gb', 'ie', 'ine', 'inter', 'is', 'mx', 'nz', 'pt', 'si', 'uy', 'us', 'genderguesser'])
parser.add_argument('--output', default="files/names/out.csv")
parser.add_argument('--noshow', dest='noshow', action='store_true')
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

nameslist = du.csvcolumn2list(args.path)
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

file = open(args.output, "w")
for i in l:
    file.write(str(i[0])+","+str(i[1]) + "\n")

file.close()

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
        print("the females list")
        for i in females_list:
           print(i)

    print("------------------------------------------------------------------------")
    print("The number of gender not recognised in %s is %s" % (str(args.path), str(len(unknows_list))))
    if ((args.verbose) and (len(unknows_list) >0)):
        print("the unknowns list")
        for i in unknows_list:
           print(i)



import matplotlib.pyplot as plt

data = [len(males_list), len(females_list), len(unknows_list)]
gender = ["Males","Females","Unknows"]
plt.title("People grouped by gender")
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.axis("equal")

if (args.noshow):
    plt.savefig('files/images/csv2gender.png')
else:
    plt.savefig('files/images/csv2gender.png')
    plt.show()
