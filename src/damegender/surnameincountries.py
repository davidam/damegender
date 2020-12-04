#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.




from app.dame_gender import Gender
from app.dame_ethnicity import DameEthnicity
from app.dame_utils import DameUtils
import sys
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("surname", help="display the gender")
#parser.add_argument('--total', required=True, default="ine", choices=['ine', 'es', 'us'])
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()

results = []

de = DameEthnicity()
du = DameUtils()
surname = args.surname.upper()

l = de.inesurname2ethnicity(surname, 'all')
l = sorted(du.clean_list(l))
if (len(l) > 0):
    print("In Spain (Instituto Nacional de Estadística) the surname %s is present with people of another countries:" % surname)
else:
    print("In Spain (Instituto Nacional de Estadística) the surname %s is not present with people of another countries" % surname)

#print(l)
# print(de.locale2eng('ci'))
# print(de.locale2eng('cu'))
# print(de.locale2eng('fr'))
# print(de.locale2eng('gt'))
# print(de.locale2eng('it'))


for i in l:
    print("+ %s" % de.locale2eng(i))
