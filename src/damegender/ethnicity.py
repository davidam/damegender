#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

from app.dame_gender import Gender
from app.dame_ethnicity import DameEthnicity
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
surname = args.surname.upper()
dicc = de.surname2ethnicity(surname)

if (dicc):
        print("In United States of America the percentages about the race of %s surname is: " % surname.capitalize())
        print("White: %s" % dicc['white'])
        print("Black: %s" % dicc['black'])
        print("Hispanic: %s" % dicc['hispanic'])
        print("Asian Pacific Indian American: %s" % dicc['api'])
        print("American Indian and Alaska Native: %s" % dicc['aian'])
        print("Various races: %s" % dicc['doublerace'])
else:
        print("This string %s is not a surname in United States of America" % surname.capitalize())
