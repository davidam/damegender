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

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_namsor import DameNamsor
from app.dame_genderize import DameGenderize
from app.dame_genderguesser import DameGenderGuesser
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/min.csv")
args = parser.parse_args()
print(args.csv)



dn = DameNamsor()
print("################### Namsor!!")
gl = dn.gender_list(path=args.csv)
print("Gender list: " + str(gl))
sl = dn.guess_list(path=args.csv, binary=True)
print("Guess list:  " +str(sl))

namsor_accuracy = dn.accuracy_score_dame(gl, sl)
#print(dn.accuracy_score_dame([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1]))
#namsor_accuracy = dn.accuracy_score_dame([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1])
print(namsor_accuracy)
print("Namsor accuracy: %s" % namsor_accuracy)

dg = DameGenderize()
print("################### Genderize!!")
gl = dg.gender_list(path=args.csv)
print("Gender list: " + str(gl))
sl = dg.guess_list(path=args.csv, binary=True)
print("Guess list:  " +str(gl))

genderize_accuracy = dg.accuracy_score_dame(gl,sl)
print("Genderize accuracy: %s" % genderize_accuracy)

dgg = DameGenderGuesser()
print("################### GenderGuesser!!")
gl = dgg.gender_list(path=args.csv)
print("Gender list: " + str(gl))
sl = dgg.guess_list(path=args.csv, binary=True)
print("Guess list:  " +str(sl))

genderguesser_accuracy = dgg.accuracy_score_dame(gl,sl)
print("GenderGuesser accuracy: %s" % genderguesser_accuracy)

ds = DameSexmachine()
print("################### Sexmachine!!")
gl = ds.gender_list(path=args.csv)
print("Gender list: " + str(gl))
sl = ds.guess_list(path=args.csv, binary=True)
print("Guess list:  " +str(sl))

sexmachine_accuracy = ds.accuracy_score_dame(gl,sl)
print("Sexmachine accuracy: %s" % sexmachine_accuracy)
