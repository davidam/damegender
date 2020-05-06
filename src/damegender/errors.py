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
from app.dame_namsor import DameNamsor

import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv")
parser.add_argument('--jsondownloaded', required=True, help="files/names/genderapifiles_names_min.csv.json")
args = parser.parse_args()

d = DameSexmachine()
print("Damegender with %s has: " % args.csv)
gl1 = d.gender_list(path=args.csv)
gl2 = d.json2guess_list(jsonf=args.jsondownloaded, binary=True)        

ec = d.error_coded(gl1, gl2)
print("+ The error code: %s" % ec)
ecwa = d.error_coded_without_na(gl1, gl2)
print("+ The error code without na: %s" %  ecwa)
naCoded = d.na_coded(gl1, gl2)
print("+ The na coded: %s" %  naCoded)
egb = d.error_gender_bias(gl1, gl2)
print("+ The error gender bias: %s" %  egb)


