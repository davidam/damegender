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
        dn.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Namsor')

    if (dg.config['DEFAULT']['genderize'] == 'yes'):
        dg = DameGenderize()
        dg.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Genderize')

    dgg = DameGenderGuesser()
    dgg.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Genderguesser')

    ds = DameSexmachine()
    ds.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Damegender')

    if (dg.config['DEFAULT']['genderapi'] == 'yes'):
        dga = DameGenderApi()
        dga.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Genderapi')

    if (dg.config['DEFAULT']['nameapi'] == 'yes'):
        dna = DameNameapi()
        dna.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Nameapi')

elif (args.api == "namsor"):
    dn = DameNamsor()
    dn.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Namsor')

elif (args.api == "genderize"):
    dg = DameGenderize()
    dg.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Genderize')

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    dgg.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Genderguesser')

elif (args.api == "customsearch"):
    dc = DameCustomsearch()
    dc.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Customsearch')

elif (args.api == "damegender"):
    ds = DameSexmachine()
    ds.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Damegender')

elif (args.api == "genderapi"):
    dga = DameGenderApi()
    dga.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Genderapi')

elif (args.api == "nameapi"):
    dna = DameNameapi()
    dna.pretty_gg_list(path=args.csv, jsonf=args.jsondownloaded, measure=args.measure, api='Nameapi')
