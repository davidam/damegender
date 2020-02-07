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
from app.dame_genderize import DameGenderize
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_nameapi import DameNameapi
from app.dame_customsearch import DameCustomsearch
from app.dame_utils import DameUtils

import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--csv', type=str, required=True, default="files/names/min.csv", help='input file for names')
parser.add_argument('--jsondownloaded', required=True, help='if you have downloaded the results from an api in a json file, you can try this argument')
parser.add_argument('--measure', default="accuracy", choices=['accuracy', 'precision', 'recall', 'f1score'])
parser.add_argument('--api', required=True, choices=['customsearch', 'namsor', 'genderize', 'genderguesser', 'damegender', 'genderapi', 'nameapi', 'all'])
args = parser.parse_args()

du = DameUtils()

if (args.api == "all"):
    dg = Gender()

    if (dg.config['DEFAULT']['namsor'] == 'yes'):
        dn = DameNamsor()
        print("################### Namsor!!")
        gl = dn.gender_list(path=args.csv)
        print("Gender list: " + str(gl))
        sl = dn.guess_list(path=args.csv, binary=True)
        print("Guess list:  " +str(sl))
        dg.print_measures(gl, sl, args.measure, "Namsor")

    if (dg.config['DEFAULT']['genderize'] == 'yes'):
        dg = DameGenderize()
        print("################### Genderize!!")
        gl = dg.gender_list(path=args.csv)
        print("Gender list: " + str(gl))
        sl = dg.guess_list(path=args.csv, binary=True)
        print("Guess list:  " +str(gl))
        dg.print_measures(gl, sl, args.measure, "Genderize")

    dgg = DameGenderGuesser()
    print("################### GenderGuesser!!")
    gl = dgg.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dgg.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    dgg.print_measures(gl, sl, args.measure, "GenderGuesser")


    ds = DameSexmachine()
    print("################### Dame Gender!!")
    gl = ds.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = ds.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    ds.print_measures(gl, sl, args.measure, "Dame Gender")



    if (dg.config['DEFAULT']['genderapi'] == 'yes'):
        dga = DameGenderApi()
        print("################### GenderApi!!")
        gl = dga.gender_list(path=args.csv)
        print("Gender list: " + str(gl))
        if (args.jsondownloaded is None):
            sl = dga.guess_list(path=args.csv, binary=True)
        elif (os.path.isfile(args.jsondownloaded)):
            sl = json2guess_list(jsonf="", binary=False)
        else:
            print("In the path %s doesn't exist file" % args.jsondownloaded)
        print("Guess list:  " +str(sl))
        dga.print_measures(gl, sl, args.measure, "Genderapi")

    if (dg.config['DEFAULT']['nameapi'] == 'yes'):
        dna = DameNameapi()
        print("################### Nameapi!!")
        gl = dna.gender_list(path=args.csv)
        print("Gender list: " + str(gl))
        sl = dna.guess_list(path=args.csv, binary=True)
        print("Guess list:  " +str(sl))
        dna.print_measures(gl, sl, args.measure, "Nameapi")

elif (args.api == "namsor"):
    dn = DameNamsor()
    gl = dn.gender_list(path=args.csv)
    if (args.jsondownloaded is None):
        print("################### Namsor!!")
        print("Gender list: " + str(gl))
        sl = dn.guess_list(path=args.csv, binary=True)
        print("Guess list:  " +str(sl))
    else:
        if (dn.json_eq_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)):
            if (os.path.isfile(args.jsondownloaded)):
                print("################### Namsor!!")
                print("Gender list: " + str(gl))
                sl = dn.json2guess_list(jsonf=args.jsondownloaded, binary=True)
                print("Guess list:  " +str(sl))
                dn.print_measures(gl, sl, args.measure, "Namsor")
            else:
                print("In the path %s doesn't exist file" % args.jsondownloaded)
        else:
            print("Names in json and csv are differents")
            print("Names in csv: %s:" % ds.csv2names(path=args.csv))
            print("Names in json: %s:" % ds.json2names(jsonf=args.jsondownloaded, surnames=False))


elif (args.api == "genderize"):
    dg = DameGenderize()
    gl = dg.gender_list(path=args.csv)
    if (args.jsondownloaded is None):
        print("################### Genderize!!")
        gl = dg.gender_list(path=args.csv)
        print("Gender list: " + str(gl))
        sl = dg.guess_list(path=args.csv, binary=True)
        print("Guess list: " + str(sl))
    else:

        if (dg.json_eq_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)):
            if (os.path.isfile(args.jsondownloaded)):
                print("################### Genderize!!")
                print("Gender list: " + str(gl))
                sl = dg.json2guess_list(jsonf=args.jsondownloaded, binary=True)
                print("Guess list:  " +str(sl))
                dg.print_measures(gl, sl, args.measure, "Genderize")
            else:
                print("In the path %s doesn't exist file" % args.jsondownloaded)
        else:
            print("There are %s names in the json file and %s in the csv file" % (len(dg.csv2names(path=args.csv)), len(dg.json2names(jsonf=args.jsondownloaded))))
            print("Names in json and csv are differents")
            print("Names in csv: ")
            print(dg.csv2names(path=args.csv))
            print("Names in json: ")
            print(dg.json2names(jsonf=args.jsondownloaded))
            v = dg.first_uneq_json_and_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)
            print("First name different is %s. It's in position %s" % (v[0], v[1]))

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    print("################### GenderGuesser!!")
    gl = dgg.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dgg.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    dgg.print_measures(gl, sl, args.measure, "GenderGuesser")


elif (args.api == "customsearch"):
    dc = DameCustomsearch()
    print("################### Google Custom Search!!")
    gl = dc.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dc.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    customsearch_accuracy = dc.accuracy_score_dame(gl,sl)
    print("Google Custom Search: %s" % customsearch_accuracy)


elif (args.api == "damegender"):
    ds = DameSexmachine()
    gl = ds.gender_list(path=args.csv)

    if (os.path.isfile(args.jsondownloaded)):
        if (ds.json_eq_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)):
            print("################### Damegender!!")
            print("Gender list: " + str(gl))
            sl = ds.json2guess_list(jsonf=args.jsondownloaded, binary=True)
            print("Guess list:  " +str(sl))
            ds.print_measures(gl, sl, args.measure, "Damegender")
        else:
            print("Names in json and csv are differents")
            print("Names in csv: %s:" % ds.csv2names(path=args.csv))
            print("Names in json: %s:" % ds.json2names(jsonf=args.jsondownloaded, surnames=False))
    else:
        print("In the path %s doesn't exist file" % args.jsondownloaded)
        print("You can create one, but this process can take long time")
        yes_or_not = du.yes_or_not("Do you want create a json file? ")
        if yes_or_not:
            sl = ds.guess_list(path=args.csv, binary=args.binary, ml=args.ml)
            ds.csv2json(path=args.csv, l=sl, jsonf=args.jsondownloaded)
            if (ds.json_eq_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)):
                print("################### Damegender!!")
                print("Gender list: " + str(gl))
                print("Guess list:  " +str(sl))
                ds.print_measures(gl, sl, args.measure, "Damegender")
            else:
                print("Names in json and csv are differents")
                print("Names in csv: %s:" % ds.csv2names(path=args.csv))
                print("Names in json: %s:" % ds.json2names(jsonf=args.jsondownloaded, surnames=False))


elif (args.api == "genderapi"):
    dga = DameGenderApi()
    print("################### GenderApi!!")
    gl = dga.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    if (args.jsondownloaded is None):
        sl = dga.guess_list(path=args.csv, binary=True)
    elif (os.path.isfile(args.jsondownloaded)):
        sl = dga.json2guess_list(jsonf=args.jsondownloaded, binary=True)
    else:
        print("In the path %s doesn't exist file" % args.jsondownloaded)
    print("Guess list:  " +str(sl))
    dga.print_measures(gl, sl, args.measure, "Genderapi")


elif (args.api == "nameapi"):
    dna = DameNameapi()
    print("################### Nameapi!!")
    gl = dna.gender_list(path=args.csv)

    if (os.path.isfile(args.jsondownloaded)):
        if (dna.json_eq_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)):
            print("Gender list: " + str(gl))
            sl = dna.json2guess_list(jsonf=args.jsondownloaded, binary=True)
            print("Guess list:  " +str(sl))
            dna.print_measures(gl, sl, args.measure, "Nameapi")
        else:
            print("Names in json and csv are differents")
            print("Names in csv: %s:" % dna.csv2names(path=args.csv))
            print("Names in json: %s:" % dna.json2names(jsonf=args.jsondownloaded, surnames=False))
    else:
        print("In the path %s doesn't exist file" % args.jsondownloaded)
    # print("Guess list:" + str(sl))
    # dna.print_measures(gl, sl, args.measure, "Nameapi")
