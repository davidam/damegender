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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.dame_sexmachine import DameSexmachine
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="display the gender")
parser.add_argument('--ml', default="nltk", choices=['nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB'])
parser.add_argument('--total', default="ine", choices=['ine', 'uscensus', 'ukcensus', 'all'])
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

if (len(sys.argv) > 1):
    s = DameSexmachine()
    if (args.ml):
        #print(s.guess("Palabra", binary=True, ml="svc"))
        if (args.ml == "nltk"):
            guess = s.guess(args.name, binary=True, ml="nltk")
        if (args.ml == "sgd"):
            guess = s.guess(args.name, binary=True, ml="sgd")
        elif (args.ml == "svc"):
            guess = s.guess(args.name, binary=True, ml="svc")
        elif (args.ml == "gaussianNB"):
            guess = s.guess(args.name, binary=True, ml="gaussianNB")
        elif (args.ml == "multinomialNB"):
            guess = s.guess(args.name, binary=True, ml="multinomialNB")
        elif (args.ml == "bernoulliNB"):
            guess = s.guess(args.name, binary=True, ml="bernoulliNB")
        if (guess == 1):
            sex = "male"
        elif (guess == 0):
            sex = "female"
        elif (guess == 2):
            sex = "unknown"
        print("%s gender is %s" % (str(args.name), sex))
    else:
        print("%s's gender is %s" % (str(args.name), s.guess(args.name)))
    if (args.total == "ine"):
        print("%s males for %s from INE.es" % (s.name_frec(args.name, dataset=args.total)['males'], args.name))
        print("%s females for %s from INE.es" % (s.name_frec(args.name, dataset=args.total)['females'], args.name))
    elif (args.total == "uscensus"):
        print("%s males for %s from US Census (2017)" % (s.name_frec(args.name, dataset=args.total)['males'], args.name))
        print("%s females for %s from US Census (2017)" % (s.name_frec(args.name, dataset=args.total)['females'], args.name))
    elif (args.total == "ukcensus"):
        print("%s males for %s from UK Census (2017)" % (s.name_frec(args.name, dataset=args.total)['males'], args.name))
        print("%s females for %s from UK Census (2017)" % (s.name_frec(args.name, dataset=args.total)['females'], args.name))
    elif (args.total == "all"):
        males1 = s.name_frec(args.name, dataset="ine")['males']
        males2 = s.name_frec(args.name, dataset="uscensus")['males']
        males3 = s.name_frec(args.name, dataset="ukcensus")['males']
        males = int(males1) + int(males2) + int(males3)
        females1 = s.name_frec(args.name, dataset="ine")['females']
        females2 = s.name_frec(args.name, dataset="uscensus")['females']
        females3 = s.name_frec(args.name, dataset="ukcensus")['females']
        females = int(females1) + int(females2) + int(females3)
        print("%s males and %s females from all census (INE + Uk census + USA census)" % (males, females))
