#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

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
                    choices=['at', 'au', 'be', 'ca', 'de', 'es', 'fi',
                             'ie', 'ine', 'is', 'nz', 'mx', 'pt',
                             'si', 'uy', 'uk', 'us'])
parser.add_argument('--gender', default="female", choices=['male', 'female'])
parser.add_argument('--surname', default=False, action="store_true")
parser.add_argument('--version', action='version', version='0.3')
args = parser.parse_args()

g = Gender()

print(args.surname)
if (args.surname):
    if ((args.total == "es") or (args.total == "us")):
        print(args.total)
else:
    du = DameUtils()
    dicc = du.dicc_dataset(args.gender)

    path = dicc[args.total]

with open(path) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sexreader:
        regex = "^" + args.chars.upper()
        match = re.search(regex, row[0].upper())
        if match:
            print(row[0])
