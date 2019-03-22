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
from app.dame_customsearch import DameCustomsearch

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv")
parser.add_argument('--api', default="all")
args = parser.parse_args()
#print(args.csv)


print("A confusion matrix C is such that Ci,j is equal to the number of observations known to be in group i but predicted to be in group j.")
print("If the classifier is nice, the diagonal is high because there are true positives")

# g = Gender()
# gl1 = g.gender_list(path=args.csv)
# print(gl1)
# gl2 = g.guess_list(path=args.csv, binary=True)
# print(gl2)

# g.print_confusion_matrix_dame(path='files/names/partial.csv')

if (args.api == "all"):
    dn = DameNamsor()
    print("Namsor confusion matrix:\n")
    dn.print_confusion_matrix_dame(path=args.csv)

    dg = DameGenderize()
    print("Genderize confusion matrix:\n")
    dg.print_confusion_matrix_dame(path=args.csv)

    dgg = DameGenderGuesser()
    print("Gender Guesser confusion matrix:\n")
    dgg.print_confusion_matrix_dame(path=args.csv)

    ds = DameSexmachine()
    print("Sexmachine confusion matrix:\n")
    ds.print_confusion_matrix_dame(path=args.csv)

    dna = DameNameapi()
    print("Nameapi confusion matrix:\n")
    dna.print_confusion_matrix_dame(path=args.csv)


elif (args.api == "namsor"):
    dn = DameNamsor()
    print("Namsor confusion matrix:\n %s")
    dn.print_confusion_matrix_dame(path=args.csv)

elif (args.api == "genderize"):
    dg = DameGenderize()
    print("Genderize confusion matrix:\n")
    dg.print_confusion_matrix_dame(path=args.csv)

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    print("Gender Guesser confusion matrix:\n %s" % genderguesser_confusion_matrix)
    dgg.print_confusion_matrix_dame(path=args.csv)

elif (args.api == "sexmachine"):
    ds = DameSexmachine()
    print("Sexmachine confusion matrix:\n")
    ds.print_confusion_matrix_dame(path=args.csv)

elif (args.api == "nameapi"):
    dna = DameNameapi()
    print("Nameapi confusion matrix:\n")
    dna.print_confusion_matrix_dame(path=args.csv)

elif (args.api == "customsearch"):
    dc = DameCustomsearch()
    print("Google Custom Search confusion matrix:\n")
    dc.print_confusion_matrix_dame(path=args.csv)
