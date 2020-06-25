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

from app.dame_sexmachine import DameSexmachine
from app.dame_perceval import DamePerceval
from app.dame_utils import DameUtils
from app.dame_gender import Gender
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Uniform Resource Link")
parser.add_argument('--directory')
parser.add_argument('--show', choices=['males', 'females', 'unknowns', 'all'])
parser.add_argument('--ml', default='none', choices=['none', 'nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

if (len(sys.argv) > 1):
    if (args.ml == 'none'):
        g = Gender()
        print("You are not using ml the process is not very slow, but perhaps you are not finding good results")
    else:
        g = DameSexmachine()
    du = DameUtils()
    dp = DamePerceval()
    l1 = dp.list_committers(args.url, args.directory, mail=True)
    l2 = du.delete_duplicated(l1)
    l4 = du.delete_duplicated_identities(l2)    
    
    females = 0
    males = 0
    unknowns = 0

    list_females = []
    list_males = []
    list_unknowns = []            
    
    for row in l4:
        vector = du.identity2name_email(row)
        fullname = vector[0]
        vector2 = fullname.split()
        name = vector2[0]
        if (args.ml == 'none'):
            sm = g.guess(name, binary=True, dataset='usa')
        else:
            sm = g.guess(name, binary=True, dataset='usa', ml=args.ml)
        if (sm == 0):
            females = females + 1
            list_females.append(fullname)
        elif (sm == 1):
            males = males + 1
            list_males.append(fullname)            
        else:
            unknowns = unknowns + 1
            list_unknowns.append(fullname)
            
    print("The number of males sending commits is %s" % males)
    if ((args.show=='males') or (args.show=='all')):
        print("The list of males sending mails is:" % list_males)
        print(list_males)
    
    print("The number of females sending commits is %s" % females)
    if ((args.show=='females') or (args.show=='all')):
        print("The list of females sending mails is:" % list_females)
        print(list_females)
    
    print("The number of people with unknown gender sending commits is %s" % unknowns)    
    if ((args.show=='unknowns') or (args.show=='all')):
        print("The list of people with unknown gender sending mails is:" % list_unknowns)
        print(list_unknowns)

    
