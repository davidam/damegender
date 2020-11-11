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



from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument('--first_name_position', required=True, type=int, choices=[0, 1, 2, 3, 4], default=0)
parser.add_argument('--dataset', default="us", choices=['au', 'ca', 'es', 'fi', 'ie', 'ine', 'is', 'nz', 'pt', 'uy', 'uk', 'us', 'luciahelena', 'genderguesser'])
parser.add_argument('--output', default="files/names/out.csv")
parser.add_argument('--noshow', dest='noshow', action='store_true')
parser.add_argument('--version', action='version', version='0.1')
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
    
if (len(sys.argv) > 1):
    print("The number of males in %s is %s" % (str(args.path), str(len(males_list))))
    print("The number of females in %s is %s" % (str(args.path), str(len(females_list))))
    print("The number of gender not recognised in %s is %s" % (str(args.path), str(len(unknows_list))))


    
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
