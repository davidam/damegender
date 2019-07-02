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
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_genderize import DameGenderize
from app.dame_nameapi import DameNameapi
from app.dame_namsor import DameNamsor


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv")
parser.add_argument('--api', default="damegender", choices=['damegender', 'namsor', 'genderize', 'genderguesser', 'genderapi', 'nameapi'])
args = parser.parse_args()
#print(args.csv)




if (args.api == "damegender"):
    dn = DameSexmachine()
    print("Damegender with %s has: " % args.csv)
    gl1 = dn.gender_list(path=args.csv)
    gl2 = dn.guess_list(path=args.csv, binary=True)
    ec = dn.error_coded(gl1, gl2)
    print("+ The error code: %s" % ec)
    ecwa = dn.error_coded_without_na(gl1, gl2)
    print("+ The error code without na: %s" %  ecwa)
    naCoded = dn.na_coded(gl1, gl2)
    print("+ The na coded: %s" %  naCoded)
    egb = dn.error_gender_bias(gl1, gl2)
    print("+ The error gender bias: %s" %  egb)
elif (args.api == "genderize"):
    dn = DameGenderize()
    print("Genderize with %s has: " % args.csv)
    gl1 = dn.gender_list(path=args.csv)
    gl2 = dn.guess_list(path=args.csv, binary=True)
    ec = dn.error_coded(gl1, gl2)
    print("+ The error code: %s" % ec)
    ecwa = dn.error_coded_without_na(gl1, gl2)
    print("+ The error code without na: %s" %  ecwa)
    naCoded = dn.na_coded(gl1, gl2)
    print("+ The na coded: %s" %  naCoded)
    egb = dn.error_gender_bias(gl1, gl2)
    print("+ The error gender bias: %s" %  egb)
elif (args.api == "genderapi"):
    dga = DameGenderApi()
    print("Genderapi with %s has: " % args.csv)
    gl1 = dga.gender_list(path=args.csv)
    gl2 = dga.guess_list(path=args.csv, binary=True)
    ec = dga.error_coded(gl1, gl2)
    print("+ The error code: %s" % ec)
    ecwa = dga.error_coded_without_na(gl1, gl2)
    print("+ The error code without na: %s" %  ecwa)
    naCoded = dga.na_coded(gl1, gl2)
    print("+ The na coded: %s" %  naCoded)
    egb = dga.error_gender_bias(gl1, gl2)
    print("+ The error gender bias: %s" %  egb)
elif (args.api == "genderguesser"):
    dn = DameGenderGuesser()
    print("Gender Guesser with %s has: " % args.csv)
    gl1 = dn.gender_list(path=args.csv)
    gl2 = dn.guess_list(path=args.csv, binary=True)
    ec = dn.error_coded(gl1, gl2)
    print("+ The error code: %s" % ec)
    ecwa = dn.error_coded_without_na(gl1, gl2)
    print("+ The error code without na: %s" %  ecwa)
    naCoded = dn.na_coded(gl1, gl2)
    print("+ The na coded: %s" %  naCoded)
    egb = dn.error_gender_bias(gl1, gl2)
    print("+ The error gender bias: %s" %  egb)
elif (args.api == "nameapi"):
    dn = DameNameapi()
    print("Nameapi with %s has: " % args.csv)
    gl1 = dn.gender_list(path=args.csv)
    gl2 = dn.guess_list(path=args.csv, binary=True)
    ec = dn.error_coded(gl1, gl2)
    print("+ The error code: %s" % ec)
    ecwa = dn.error_coded_without_na(gl1, gl2)
    print("+ The error code without na: %s" %  ecwa)
    naCoded = dn.na_coded(gl1, gl2)
    print("+ The na coded: %s" %  naCoded)
    egb = dn.error_gender_bias(gl1, gl2)
    print("+ The error gender bias: %s" %  egb)
elif (args.api == "namsor"):
    dn = DameNamsor()
    print("Namsor with %s has: " % args.csv)
    gl1 = dn.gender_list(path=args.csv)
    gl2 = dn.guess_list(path=args.csv, binary=True)
    ec = dn.error_coded(gl1, gl2)
    print("+ The error code: %s" % ec)
    ecwa = dn.error_coded_without_na(gl1, gl2)
    print("+ The error code without na: %s" %  ecwa)
    naCoded = dn.na_coded(gl1, gl2)
    print("+ The na coded: %s" %  naCoded)
    egb = dn.error_gender_bias(gl1, gl2)
    print("+ The error gender bias: %s" %  egb)
