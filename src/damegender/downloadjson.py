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
from app.dame_namsor import DameNamsor
from app.dame_genderize import DameGenderize
from app.dame_genderapi import DameGenderApi
from app.dame_nameapi import DameNameapi


import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv", help='input file for names')
parser.add_argument('--api', default="damegender", choices=['namsor', 'genderize', 'genderapi', 'nameapi'])
args = parser.parse_args()

if (args.api=='genderize'):
    dg = DameGenderize()
    text1 = dg.download(path=args.csv)
elif (args.api=='genderapi'):
    dga = DameGenderApi()
    text1 = dga.download(path=args.csv)
elif (args.api=='namsor'):    
    dn = DameNamsor()
    text1 = dn.download(path=args.csv)
elif (args.api=='nameapi'):
    dna = DameNameapi()
    text1 = dna.download(path=args.csv)
