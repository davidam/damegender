#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is Free Software; you can redistribute it and/or modify
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

# DESCRIPTION: Given a substring such as a letter returns names of a
# dataset.

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import sys
import os
import re
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("chars", help="display the gender")
parser.add_argument('--total', default="us",
                    choices=['ar', 'at', 'au', 'be', 'ca', 'ch', 'cn',
                             'de', 'dk', 'es', 'fi', 'fr', 'gb',
                             'ie', 'ine', 'inter', 'is', 'no',
                             'nz', 'mx', 'pt', 'ru', 'ru_ru',
                             'ru_en', 'se', 'si', 'us', 'uy'])
parser.add_argument('--gender', default="female", choices=['male', 'female'])
parser.add_argument('--version', action='version', version='0.4')
args = parser.parse_args()

g = Gender()

du = DameUtils()
dicc = du.dicc_dataset(args.gender)
path = dicc[args.total]

if (args.total == "cn"):
    print("Be careful")
    print("you must use Chinese characters and supported encoding")
elif ((args.total == "ru") or (args.total == "ru_ru")):
    print("Be carefull,")
    print("you must use Russian characters")
    print("and supported encoding")
    print("If you want check russian names")
    print("starting with latin letters,")
    print("you can use the keyword ru_en.")


with open(path) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sexreader:
        regex = "^" + args.chars.upper()
        match = re.search(regex, row[0].upper())
        if match:
            print(row[0])
