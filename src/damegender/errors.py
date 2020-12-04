#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.




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


