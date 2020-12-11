#!/usr/bin/python
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_utils import DameUtils
import sys
import os
import re
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("chars", help="display the gender")
#parser.add_argument('--ml', choices=['nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--total', default="us", choices=['at', 'au', 'be', 'ca', 'de', 'es', 'fi', 'ie', 'ine', 'is', 'nz', 'mx', 'pt', 'si', 'uy', 'uk', 'us'])
parser.add_argument('--gender', default="female", choices=['male', 'female'])
parser.add_argument('--version', action='version', version='0.3')
args = parser.parse_args()

g = Gender()
path =  g.path_dataset(args.total, args.gender)

with open(path) as csvfile:
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sexreader:
#        print(row[0].upper())
        regex = "^" + args.chars.upper()
        match = re.search(regex, row[0].upper())
        if match:
            print(row[0])
