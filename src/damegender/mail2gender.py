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
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Uniform Resource Link")
parser.add_argument('--directory')
parser.add_argument('--show', choices=['males', 'females', 'unknowns', 'all'])
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()
if (len(sys.argv) > 1):
    s = DameSexmachine()
    gg = DamePerceval()
    du = DameUtils()
    l = gg.list_mailers(args.url)
    l2 = du.delete_duplicated(l)
    l4 = du.delete_duplicated_identities(l2)    
    
    females = 0
    males = 0
    unknowns = 0

    list_females = []
    list_males = []
    list_unknowns = []            
    for g in l4:
        sm = s.guess(g, binary=True)
        if (sm == 0):
            females = females + 1
            list_females.append(g)
        elif (sm == 1):
            males = males + 1
            list_males.append(g)            
        else:
            unknowns = unknowns + 1
            list_unknowns.append(g)
            
    print("The number of males sending mails is %s" % males)
    if ((args.show=='males') or (args.show=='all')):
        print("The list of males sending mails is:" % list_males)
        print(list_males)
        
    print("The number of females sending mails is %s" % females)
    if ((args.show=='females') or (args.show=='all')):
        print("The list of females sending mails is:" % list_females)
        print(list_females)

    print("The number of people with unknown gender sending mails is %s" % unknowns)            
    if (args.show=='unknowns'):
        print("The list of people with unknown gender sending mails is ")
        print(list_unknowns)

    
