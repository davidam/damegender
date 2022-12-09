#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# DESCRIPTION: From a name give a list of countries where the people
# is using the name (using namdict dataset)

import re
import os
import csv
import sys
from app.dame_utils import DameUtils
from app.dame_gender import Gender
from app.dame_ethnicity import DameEthnicity
from app.dame_genderguesser import DameGenderGuesser
import argparse

du = DameUtils()
de = DameEthnicity()
dgg = DameGenderGuesser()
g = Gender()

parser = argparse.ArgumentParser()
parser.add_argument("name", help="display the country")
parser.add_argument('--dataset', default="inter",
                    choices=['namdict', 'inter', 'damegender'])
args = parser.parse_args()

if (args.dataset == "namdict"):
    print("We are using nam_dict.txt as dataset in this script")
    cmd = 'grep -i " ' + args.name
    cmd = cmd + ' " files/names/nam_dict.txt > files/logs/grep.tmp'
    print(cmd)
    os.system(cmd)
    results = [i for i in open('files/logs/grep.tmp', 'r').readlines()]
    males = []
    females = []
    both = []
    for rowres in results:
        regex = "(M|F|=|\\?|1)( |M|F)?( )(\\w+)( )?(\\w+)?( )?(\\w+)?"
        n = re.match(regex, rowres)
        if (n.group(6)):
            string = str(n.group(4)) + str(n.group(5)) + str(n.group(6))
        else:
            string = str(n.group(4)) + str(n.group(5))
        namecapitalize = du.drop_white_space(args.name.capitalize())
        if (namecapitalize == du.drop_white_space(string)):
            twochars = rowres[0] + rowres[1]
            for i in range(30, 84):
                if (dgg.exists_in_country(int(i), rowres)):
                    bool1 = (rowres[0].title() == "M")
                    bool1 = bool1 or (twochars.title() == "1M")
                    bool1 = bool1 or (twochars.title() == "?M")
                    bool2 = (rowres[0].title() == "F")
                    bool2 = bool2 or (twochars.title() == "1F")
                    bool2 = bool2 or (twochars.title() == "?F")
                    if bool1:
                        males.append(dgg.keyscountries[str(i)])
                    elif bool2:
                        females.append(dgg.keyscountries[str(i)])
                    elif (rowres[0].title() == "="):
                        both.append(dgg.keyscountries[str(i)])

    print("males: " + (str(sorted(males))))
    print("females: " + str(sorted(females)))
    print("both: " + str(sorted(both)))

elif ((args.dataset == "damegender") or (args.dataset == "inter")):
    print("We are using the international dataset in this script")
    official_names = ["ar", "at", "au", "be", "ca", "ch", "de",
                      "dk", "es", "fi", "fr", "gb", "ie", "is",
                      "no", "nz", "mx", "pt", "ru", "se", "si",
                      "us", "uy"]
    males = []
    females = []
    both = []
    iso3166_to_eng = de.dicc_iso3166_to_eng()
    for i in official_names:
        dicc = g.name_frec(args.name, dataset=i)
        if ((int(dicc["females"]) > 10) or (int(dicc["males"]) > 10)):
            print("%s (females: %s, males: %s)" %
                  (iso3166_to_eng[i], dicc["females"], dicc["males"]))
