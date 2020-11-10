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
