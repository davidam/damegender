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
from app.dame_sexmachine import DameSexmachine
from app.dame_statistics import DameStatistics
from app.dame_namsor import DameNamsor
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_genderize import DameGenderize
from app.dame_nameapi import DameNameapi
from app.dame_namsor import DameNamsor
import sys,os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default='files/names/min.csv')
parser.add_argument('--jsondownloaded', help="files/names/genderapifiles_names_min.csv.json")
parser.add_argument('--api', default='damegender', choices=['damegender', 'namsor', 'genderize', 'genderapi', 'nameapi', 'genderguesser'])
args = parser.parse_args()

dsex = DameSexmachine()


if (args.api in ['damegender', 'namsor', 'genderize', 'genderapi', 'nameapi']):
    try:
        file = open(args.jsondownloaded)
    except FileNotFoundError:
        print("---------------------------------------------------------------------------------------------------------------")
        print("If you are using damegender, namsor, genderize, genderapi, or nameapi. You must introduce a json in a real path")
        print("---------------------------------------------------------------------------------------------------------------")
        
elif ((args.api=='genderguesser') and (args.jsondownloaded)):
    print("---------------------------------------------------------------------------")    
    print("You don't need introduce jsondownloaded argument using genderguesser option")
    print("---------------------------------------------------------------------------")    

if (args.api == "genderguesser"):
    dg = DameGenderGuesser()
    gl2 = dg.guess_list(path=args.csv, binary=True)
    print("Gender Guesser with %s has: " % args.csv)
else:
    gl2 = dsex.json2guess_list(jsonf=args.jsondownloaded, binary=True)             
    print("Damegender with %s has: " % args.csv)

gl1 = dsex.gender_list(path=args.csv)
dst = DameStatistics()
ec = dst.error_coded(gl1, gl2)
print("+ The error code: %s" % ec)
ecwa = dst.error_coded_without_na(gl1, gl2)
print("+ The error code without na: %s" %  ecwa)
naCoded = dst.na_coded(gl1, gl2)
print("+ The na coded: %s" %  naCoded)
egb = dst.error_gender_bias(gl1, gl2)
print("+ The error gender bias: %s" %  egb)


