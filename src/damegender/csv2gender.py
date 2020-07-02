#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument('--first_name_position', required=True, type=int, choices=[0, 1, 2, 3, 4], default=0)
# parser.add_argument('--second_name_position', type=int, default=1)
# parser.add_argument('--first_surname_position', type=int, default=2)
# parser.add_argument('--second_surname_position', type=int, default=3)
parser.add_argument('--dataset', default="us", choices=['au', 'ca', 'es', 'fi', 'ie', 'ine', 'is', 'nz', 'pt', 'uy', 'uk', 'us', 'luciahelena', 'genderguesser', 'all'])
#parser.add_argument('--sex_position', required=True, type=int, choices=[0, 1, 2, 3, 4], default=4)
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

#print(args.sex_position)

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
    sex = s.guess(firstname, binary=False, dataset=args.dataset)
    if (sex == "male"):
        males_list.append(firstname)
    elif (sex == "female"):
        females_list.append(firstname)            
    else:
        unknows_list.append(firstname)
    l.append([firstname, sex])
    
if (len(sys.argv) > 1):
    print("The number of males in %s is %s" % (str(args.path), str(len(males_list))))
    print("The number of females in %s is %s" % (str(args.path), str(len(females_list))))
    print("The number of gender not recognised in %s is %s" % (str(args.path), str(len(unknows_list))))

