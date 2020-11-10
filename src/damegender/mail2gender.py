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
from app.dame_gender import Gender
from app.dame_perceval import DamePerceval
from app.dame_utils import DameUtils
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Uniform Resource Link")
parser.add_argument('--directory')
parser.add_argument('--show', choices=['males', 'females', 'unknows', 'all'])
parser.add_argument('--ml', default='none', choices=['none', 'nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--verbose', default=False, action="store_true")
parser.add_argument('--version', action='version', version='0.1')

args = parser.parse_args()

if (len(sys.argv) > 1):
    if (args.ml == 'none'):
        s = Gender()
        print("You are not using ml the process is not very slow, but perhaps you are not finding good results")
    else:
        s = DameSexmachine()

    gg = DamePerceval()
    du = DameUtils()
    l = gg.list_mailers(args.url)
    # print(l)
    # print("----------------------------------------------------------------------------------------------------")
    l2 = du.delete_duplicated(l)
    # print(l2)
    # print("----------------------------------------------------------------------------------------------------")    
    l4 = du.delete_duplicated_identities(l2)    
    # print(l4)
    # print("----------------------------------------------------------------------------------------------------")
    l5 = gg.dicc_authors_and_mails(args.url)
    females = 0
    males = 0
    unknows = 0

    list_females = []
    list_males = []
    list_unknows = []            
    for g in l4:
        vector = g.split()
        firstname = du.drop_quotes(vector[0])
#        print(firstname)
        sm = s.guess(firstname, binary=True)
#        print(sm)
        if (sm == 0):
            list_females.append(g)
        elif (sm == 1):
            list_males.append(g)            
        else:
            list_unknows.append(g)

    print("The number of males sending mails is %s" % len(list_males))
    if ((args.show=='males') or (args.show=='all')):
        print("The list of males sending mails is:")
        print(list_males)
        if (args.verbose):
            for i in l5.keys():
                identity = du.identity2name_email(i)
                if identity[0] in list_males:
                    print("%s (%s messages)" % (i, l5[i]))
        
    print("The number of females sending mails is %s" % len(list_females))
    if ((args.show=='females') or (args.show=='all')):
        print("The list of females sending mails is:")
        print(list_females)
        if (args.verbose):
            for i in l5.keys():
                identity = du.identity2name_email(i)
                if identity[0] in list_females:
                    print("%s (%s messages)" % (i, l5[i]))
        
    print("The number of people with unknown gender sending mails is %s" % len(list_unknows))
    if ((args.show=='unknows') or (args.show == 'all')):
        print("The list of people with unknown gender sending mails is ")
        print(list_unknows)
        if (args.verbose):
            for i in l5.keys():
                identity = du.identity2name_email(i)
                if identity[0] in list_unknows:
                    print("%s (%s messages)" % (i, l5[i]))
