#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

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
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()

results = []

de = DameEthnicity()
du = DameUtils()
surname = args.surname.upper()

l1 = de.inesurname2ethnicity(surname, "all")
l1 = sorted(du.clean_list(l1))
if (len(l1) > 0):
    print("In Spain, the surname %s exists for these countries:" % surname)
else:
    print("In Spain, the surname %s does not exist" % surname)

for i in l1:
    print("+ %s" % de.locale2eng(i))
