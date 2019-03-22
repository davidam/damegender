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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_namsor import DameNamsor
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_genderize import DameGenderize
from app.dame_nameapi import DameNameapi

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv")
parser.add_argument('--api', default="all")
args = parser.parse_args()
#print(args.csv)


print("A confusion matrix C is such that Ci,j is equal to the number of observations known to be in group i but predicted to be in group j.")
print("If the classifier is nice, the diagonal is high because there are true positives")

if (args.api == "all"):
    dn = DameNamsor()
    namsor_confusion_matrix = dn.confusion_matrix(path=args.csv)
    print("Namsor confusion matrix:\n %s" % namsor_confusion_matrix)

    dg = DameGenderize()
    genderize_confusion_matrix = dg.confusion_matrix(path=args.csv)
    print("Genderize confusion matrix:\n %s" % genderize_confusion_matrix)

    dgg = DameGenderGuesser()
    genderguesser_confusion_matrix = dgg.confusion_matrix(path=args.csv)
    print("Gender Guesser confusion matrix:\n %s" % genderguesser_confusion_matrix)

    ds = DameSexmachine()
    sexmachine_confusion_matrix = ds.confusion_matrix(path=args.csv)
    print("Sexmachine confusion matrix:\n %s" % sexmachine_confusion_matrix)

    dna = DameNameapi()
    nameapi_confusion_matrix = dna.confusion_matrix(path=args.csv)
    print("Nameapi confusion matrix:\n %s" % nameapi_confusion_matrix)

elif (args.api == "namsor"):
    dn = DameNamsor()
    namsor_confusion_matrix = dn.confusion_matrix(path=args.csv)
    print("Namsor confusion matrix:\n %s" % namsor_confusion_matrix)

elif (args.api == "genderize"):
    dg = DameGenderize()
    genderize_confusion_matrix = dg.confusion_matrix(path=args.csv)
    print("Genderize confusion matrix:\n %s" % genderize_confusion_matrix)

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    genderguesser_confusion_matrix = dgg.confusion_matrix(path=args.csv)
    print("Gender Guesser confusion matrix:\n %s" % genderguesser_confusion_matrix)

elif (args.api == "sexmachine"):
    ds = DameSexmachine()
    sexmachine_confusion_matrix = ds.confusion_matrix(path=args.csv)
    print("Sexmachine confusion matrix:\n %s" % sexmachine_confusion_matrix)

elif (args.api == "nameapi"):
    dna = DameNameapi()
    nameapi_confusion_matrix = dna.confusion_matrix(path=args.csv)
    print("Nameapi confusion matrix:\n %s" % nameapi_confusion_matrix)
