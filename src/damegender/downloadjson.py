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
from app.dame_namsor import DameNamsor
from app.dame_genderize import DameGenderize
from app.dame_genderapi import DameGenderApi
from app.dame_nameapi import DameNameapi


import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--csv', type=str, required=True, default="files/names/min.csv", help='input file for names')
parser.add_argument('--api', required=True, choices=['namsor', 'genderize', 'genderapi', 'nameapi'])
parser.add_argument("--surnames", default=False, action="store_true", help="Flag to surnames")
args = parser.parse_args()


if (args.api=='genderize'):
    dg = DameGenderize()
    text1 = dg.download(path=args.csv, surnames=args.surnames)
elif (args.api=='genderapi'):
    dga = DameGenderApi()
    if (dga.config['DEFAULT']['genderapi'] == 'yes'):
        if (dga.apikey_limit_exceeded_p() == False):
            text1 = dga.download(path=args.csv)
        elif (dga.apikey_count_requests() < len(dga.csv2names(args.csv))):
            print("You don't have enough requests with this api key")
        elif (dga.apikey_count_requests() >= len(dga.csv2names(args.csv))):
            text1 = dga.download(path=args.csv)
        else:
            print("You have not money with this api key")
    else:
        print("You must enable genderapi in config.cfg")
elif (args.api=='namsor'):
    dn = DameNamsor()
    if (dn.config['DEFAULT']['namsor'] == 'yes'):
        text1 = dn.download(path=args.csv)
    else:
        print("You must enable namsor in config.cfg")
elif (args.api=='nameapi'):
    dna = DameNameapi()
    if (dna.config['DEFAULT']['nameapi'] == 'yes'):
        text1 = dna.download(path=args.csv)
    else:
        print("You must enable nameapi in config.cfg")
