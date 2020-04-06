#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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
from app.dame_sexmachine import DameSexmachine
from app.dame_namsor import DameNamsor
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_genderize import DameGenderize
from app.dame_nameapi import DameNameapi
from app.dame_customsearch import DameCustomsearch
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', type=str, required=True, help="files/names/min.csv")
parser.add_argument('--binary', default=False, action="store_true")
parser.add_argument('--notoutput', default=False, action="store_true")
parser.add_argument('--jsonoutput', type=str, default="files/names/out.json", required=False, help="files/names/out.json")
parser.add_argument('--ml', default="nltk", choices=['nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'tree', 'mlp', 'adaboost'])
args = parser.parse_args()

ds = DameSexmachine()
if args.notoutput:
    gl = ds.gender_list(path=args.csv)
    sl = ds.guess_list(path=args.csv, binary=args.binary, ml=args.ml)
else:
    print("################### Dame Gender!!")
    gl = ds.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = ds.guess_list(path=args.csv, binary=args.binary, ml=args.ml)
    print("Guess list:  " +str(sl))

if (args.jsonoutput == ""):
    ds.csv2json(path=args.csv, l=gl, jsonf=args.csv +".gender.json")
    ds.csv2json(path=args.csv, l=sl, jsonf=args.csv +".guess.json")
else:
    ds.csv2json(path=args.csv, l=sl, jsonf=args.jsonoutput)
