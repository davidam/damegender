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
# from app.dame_namsor import DameNamsor
# from app.dame_genderize import DameGenderize
# from app.dame_genderapi import DameGenderApi
# from app.dame_nameapi import DameNameapi
from app.dame_brazilapi import DameBrazilApi

import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--csv', type=str, required=True,
                    default="files/names/min.csv", help='input file for names')
parser.add_argument('--name_position', type=int, required=False,
                    default=0, help='input file for names')
parser.add_argument('--api', required=False, default='brazilapi',
                    choices=['brazilapi']) #, 'genderapi', 'genderize', 'namsor', 'nameapi'])
parser.add_argument('--outcsv', type=str, required=False,
                    default="names.csv", help='output csv file for names')
parser.add_argument('--format', type=str, required=False,
                    default="all", choices=['all', 'males', 'females'])
args = parser.parse_args()

print("This command is under construction, brazilapi is the unique option in this moment")

if (args.api == 'brazilapi'):
    dba = DameBrazilApi()
    if (args.format=='all'):
        text2 = dba.download_csv(path=args.csv,
                                 name_position=args.name_position,
                                 backup_all=args.outcsv)
    elif (args.format=='females'):
        text2 = dba.download_csv(path=args.csv,
                                 name_position=args.name_position,
                                 backup_females=args.outcsv)
    elif (args.format=='males'):
        text2 = dba.download_csv(path=args.csv,
                                 name_position=args.name_position,
                                 backup_males=args.outcsv)
        
