#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

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

    # print(list_females)
    # print(list_males)
    # print(list_unknows)            
    print("The number of males sending mails is %s" % len(list_males))
    if ((args.show=='males') or (args.show=='all')):
        print("The list of males sending mails is:")
        print(list_males)
        
    print("The number of females sending mails is %s" % len(list_females))
    if ((args.show=='females') or (args.show=='all')):
        print("The list of females sending mails is:")
        print(list_females)

    print("The number of people with unknown gender sending mails is %s" % len(list_unknows))
    if (args.show=='unknows'):
        print("The list of people with unknown gender sending mails is ")
        print(list_unknows)

    
