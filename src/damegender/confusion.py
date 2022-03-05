#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
#  This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

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

# DESCRIPTION: This script allows to measure confusion from a json
# file downloaded from an api system with downloadjson.py


from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_namsor import DameNamsor
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_genderize import DameGenderize
from app.dame_nameapi import DameNameapi
from app.dame_statistics import DameStatistics
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', type=str,
                    required=True, help="files/names/min.csv")
parser.add_argument('--jsondownloaded', default="",
                    help="files/names/genderapifiles_names_min.csv.json")
parser.add_argument('--api', required=True,
                    choices=['namsor', 'genderize', 'genderapi',
                             'genderguesser', 'damegender',
                             'nameapi', 'all'])
parser.add_argument('--reverse', default=False, action="store_true")
parser.add_argument('--dimensions', default="2x3",
                    choices=['1x1', '1x2', '1x3',
                             '2x1', '2x2', '2x3',
                             '3x1', '3x2', '3x3'])
args = parser.parse_args()

string1 = """
A confusion matrix C is such that C(i, j) is equal to the number
of observations known to be in group i but predicted to be in group j.
"""

string2 = """
If the classifier is nice, the diagonal is high because there are
true positives
"""

print(string1)
print(string2)

dst = DameStatistics()
dg = Gender()


if (args.api == "all"):
    if (dg.config['DEFAULT']['namsor'] == 'yes'):
        dst.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                      reverse=args.reverse, dimensions=args.dimensions,
                      api=args.api.title())

    if (dg.config['DEFAULT']['genderize'] == 'yes'):
        dst.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                      reverse=args.reverse, dimensions=args.dimensions,
                      api=args.api.title())

    if (dg.config['DEFAULT']['genderapi'] == 'yes'):
        dga = DameGenderApi()
        dga.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                      reverse=args.reverse, dimensions=args.dimensions,
                      api=args.api.title())

    dgg.print_confusion_matrix_gender(path=args.csv,
                                      dimensions=args.dimensions)

    ds = DameSexmachine()
    ds.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                 reverse=args.reverse, dimensions=args.dimensions,
                 api=args.api.title())

    if (dg.config['DEFAULT']['nameapi'] == 'yes'):
        dna = DameNameapi()
        dna.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                      reverse=args.reverse, dimensions=args.dimensions,
                      api=args.api.title())

elif (args.api == "namsor"):
    dn = DameNamsor()
    dn.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                 reverse=args.reverse, dimensions=args.dimensions,
                 api=args.api.title())

elif (args.api == "genderize"):
    dg = DameGenderize()
    dg.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                 reverse=args.reverse, dimensions=args.dimensions,
                 api=args.api.title())

elif (args.api == "genderapi"):
    dga = DameGenderApi()
    dga.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                  reverse=args.reverse, dimensions=args.dimensions,
                  api=args.api.title())

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    dgg.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                  reverse=args.reverse, dimensions=args.dimensions,
                  api=args.api.title())

elif (args.api == "damegender"):
    g = Gender()
    g.pretty_cm(path=args.csv, jsonf=args.jsondownloaded, reverse=args.reverse,
                dimensions=args.dimensions, api=args.api.title())

elif (args.api == "nameapi"):
    dna = DameNameapi()
    dna.pretty_cm(path=args.csv, jsonf=args.jsondownloaded,
                  reverse=args.reverse, dimensions=args.dimensions,
                  api=args.api.title())
