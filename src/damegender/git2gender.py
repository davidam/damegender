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



from app.dame_sexmachine import DameSexmachine
from app.dame_perceval import DamePerceval
from app.dame_utils import DameUtils
from app.dame_gender import Gender
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Uniform Resource Link")
parser.add_argument('--directory', required=True)
parser.add_argument('--language', default="us", choices=['au', 'ca', 'es', 'fi', 'ie', 'ine', 'is', 'nz', 'pt', 'uy', 'uk', 'us'])
parser.add_argument('--show', choices=['males', 'females', 'unknowns', 'all'])
parser.add_argument('--ml', default='none', choices=['none', 'nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--version', action='version', version='0.1')
parser.add_argument('--verbose', default=False, action="store_true")
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
    l5 = dp.dicc_authors_and_commits(args.url, args.directory)
    
    
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
            
    print("The number of males sending commits is %s" % males)
    if ((args.show=='males') or (args.show=='all')):
        print("The list of males sending commits is:" % list_males)
        print(list_males)
        if (args.verbose):
            for i in l5.keys():
                identity = du.identity2name_email(i)
                if identity[0] in list_males:
                    print("%s (%s commits)" % (i, l5[i]))
                    
        
    print("The number of females sending commits is %s" % females)
    if ((args.show=='females') or (args.show=='all')):
        print("The list of females sending commits is:" % list_females)
        print(list_females)
        if (args.verbose):
            for i in l5.keys():
                identity = du.identity2name_email(i)
                if identity[0] in list_females:
                    print("%s (%s commits)" % (i, l5[i]))
        
    print("The number of people with unknown gender sending commits is %s" % unknowns)    
    if ((args.show=='unknowns') or (args.show=='all')):
        print("The list of people with unknown gender sending commits is:" % list_unknowns)
        print(list_unknowns)
        if (args.verbose):
            for i in l5.keys():
                identity = du.identity2name_email(i)
                if identity[0] in list_unknowns:
                    print("%s (%s commits)" % (i, l5[i]))

    
