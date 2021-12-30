#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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


from app.dame_perceval import DamePerceval
from app.dame_utils import DameUtils
from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
import sys
import argparse
import datetime
from datetime import timedelta

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Launchpad name")
parser.add_argument('--language', default="us",
                    choices=['au', 'ca', 'es', 'fi', 'ie',
                             'ine', 'is', 'nz', 'pt',
                             'uy', 'uk', 'us'])
parser.add_argument('--show', choices=['males', 'females', 'unknowns', 'all'])
parser.add_argument('--ml', default='none',
                    choices=['none', 'nltk', 'svc', 'sgd', 'gaussianNB',
                             'multinomialNB', 'bernoulliNB', 'forest',
                             'tree', 'mlp'])
parser.add_argument('--version', action='version', version='0.3')
args = parser.parse_args()

g = DameSexmachine()


print("Accessing to Launchpad, please, be patient.")

males = 0
females = 0
unknowns = 0

if (len(sys.argv) > 1):
    dp = DamePerceval()
    d = datetime.datetime.now() - timedelta(hours=12)
    l1 = dp.list_launchpad("ubuntu", d)
    print(l1)
    list_females = []
    list_males = []
    list_unknowns = []
    for fullname in l1:
        vector = fullname.split()
        name = vector[0]
        if (args.ml == 'none'):
            sm = g.guess(name, binary=True, dataset=args.language)
        else:
            sm = g.guess(name, binary=True, dataset=args.language, ml=args.ml)
        if (sm == 0):
            females = females + 1
            list_females.append(fullname)
        elif (sm == 1):
            males = males + 1
            list_males.append(fullname)
        else:
            unknowns = unknowns + 1
            list_unknowns.append(fullname)

    print("The number of males using launchpad is %s" % males)
    if ((args.show == 'males') or (args.show == 'all')):
        print("The list of males using launchpad is:" % list_males)
        print(list_males)

    print("The number of females using launchpad is %s" % females)
    if ((args.show == 'females') or (args.show == 'all')):
        print("The list of females using launchpad is:" % list_females)
        print(list_females)
        
    print("The number of unknowns using launchpad is %s" % unknowns)
    if ((args.show == 'unknowns') or (args.show == 'all')):
        print("The list of unknowns using launchpad is:" % list_unknowns)
        print(list_unknowns)
        
