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

# DESCRIPTION: This script allows to download a list of names in a
# csv file from a csv file guessing names, gender and frequency
# with an api system

from app.dame_gender import Gender
from app.dame_namsor import DameNamsor
from app.dame_genderize import DameGenderize
from app.dame_genderapi import DameGenderApi
# from app.dame_nameapi import DameNameapi
from app.dame_brazilapi import DameBrazilApi

import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--csv', type=str, required=True,
                    default="files/names/min.csv", help='input file for names')
parser.add_argument('--name_position', type=int, required=False,
                    default=0, help='input file for names')
parser.add_argument('--surname_position', type=int, required=False,
                    default=0, help='input file for names')
parser.add_argument('--api', required=False, default='brazilapi',
                    choices=['brazilapi', 'genderapi', 'genderize'])
parser.add_argument('--outcsv', type=str, required=False,
                    default="names.csv", help='output csv file for names')
parser.add_argument('--outformat', type=str, required=False,
                    default="all", choices=['all', 'males', 'females'])
args = parser.parse_args()

g = Gender()

if (args.api == 'brazilapi'):
    dba = DameBrazilApi()
    if (args.outformat == 'all'):
        text2 = dba.download_csv(path=args.csv,
                                 name_position=args.name_position,
                                 backup_all=args.outcsv)
    elif (args.outformat == 'females'):
        text2 = dba.download_csv(path=args.csv,
                                 name_position=args.name_position,
                                 backup_females=args.outcsv)
    elif (args.outformat == 'males'):
        text2 = dba.download_csv(path=args.csv,
                                 name_position=args.name_position,
                                 backup_males=args.outcsv)

elif (args.api == 'genderapi'):
    if (g.config['DEFAULT']['genderapi'] == 'yes'):
        dga = DameGenderApi()
        if (args.outformat == 'all'):
            text2 = dga.download_csv(path=args.csv,
                                     name_position=args.name_position,
                                     backup_all=args.outcsv)
        elif (args.outformat == 'females'):
            text2 = dga.download_csv(path=args.csv,
                                     name_position=args.name_position,
                                     backup_females=args.outcsv)
        elif (args.outformat == 'males'):
            text2 = dga.download_csv(path=args.csv,
                                     name_position=args.name_position,
                                     backup_males=args.outcsv)
    else:
        print("You must to enable genderapi in")
        print("config.cfg and to add the api key in files/apikeys")

elif (args.api == 'genderize'):
    if (g.config['DEFAULT']['genderize'] == 'yes'):
        dg = DameGenderize()
        if (args.outformat == 'all'):
            text2 = dg.download_csv(path=args.csv,
                                    name_position=args.name_position,
                                    outpath=args.outcsv,
                                    outformat="all",
                                    backup_format=args.outformat)
        elif (args.outformat == 'females'):
            text2 = dg.download_csv(path=args.csv,
                                    name_position=args.name_position,
                                    outpath=args.outcsv,
                                    outformat="females",
                                    backup_format=args.outformat)
        elif (args.outformat == 'males'):
            text2 = dg.download_csv(path=args.csv,
                                    name_position=args.name_position,
                                    outpath=args.outcsv,
                                    outformat="males",
                                    backup_format=args.outformat)
    else:
        print("You must to enable genderize in config.cfg")
        print("and to add the api key in files/apikeys")

# elif (args.api == 'namsor'):
#     if (g.config['DEFAULT']['namsor'] == 'yes'):
#         dn = DameNamsor()
#         print("Surname position is required using namsor")
#         if (args.outformat=='all'):
#             text2 = dn.download_csv(path=args.csv,
#                                     name_position=args.name_position,
#                                     surname_position=args.surname_position,
#                                     outpath=args.outcsv,
#                                     outformat="all",
#                                     backup_format=args.outformat)
#         elif (args.outformat=='females'):
#             text2 = dn.download_csv(path=args.csv,
#                                     name_position=args.name_position,
#                                     surname_position=args.surname_position,
#                                     outpath=args.outcsv,
#                                     outformat="females",
#                                     backup_format=args.outformat)
#         elif (args.outformat=='males'):
#             text2 = dn.download_csv(path=args.csv,
#                                     name_position=args.name_position,
#                                     surname_position=args.surname_position,
#                                     outpath=args.outcsv,
#                                     outformat="males",
#                                     backup_format=args.outformat)
#     else:
#         print("You must to enable namsor in config.cfg
#               and to add the api key in files/apikeys")
