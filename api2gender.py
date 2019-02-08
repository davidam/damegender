#!/usr/bin/python
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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_genderize import DameGenderize
from app.dame_namsor import DameNamsor
from app.dame_all import DameAll
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', help="Name to be detected")
parser.add_argument('--surname', help="Surname is required in namsor")
parser.add_argument("--api", choices=['namsor', 'genderize', 'genderguesser', 'genderapi', 'nameapi'])
parser.add_argument('--prob', default="yes", choices=['yes', 'no'])
parser.add_argument('--version', action='version', version='0.1')

args = parser.parse_args()



if (len(sys.argv) > 1):
    if (args.api == "genderguesser"):
        dgg = DameGenderGuesser()
        print(dgg.guess(args.name))
    elif (args.api == "genderapi"):
        dga = DameGenderApi()
        print(dga.guess(args.name))
    elif (args.api == "genderize"):
        dg = DameGenderize()
        print(dg.guess(args.name))
        print(dg.prob(args.name))
    elif (args.api == "namsor"):
        dn = DameNamsor()
        print(dn.guess(str(args.name), str(args.surname)))
    elif (args.api == "nameapi"):
        if (args.surname != ""):
            dn = DameNameapi()
            print(dn.guess(str(args.name), str(args.surname)))
        else:
            print("In nameapi, you must provide a surname")
    elif (args.api == "average"):
        da = DameAll()
        average = da.average(args.name, args.surname)
        print(str(average))
