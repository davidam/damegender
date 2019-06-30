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
from app.dame_customsearch import DameCustomsearch

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv")
parser.add_argument('--api', default="all", choices=['namsor', 'genderize', 'genderapi', 'genderguesser', 'damegender', 'all'])
parser.add_argument('--ml', default="nltk", choices=['nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB'])
parser.add_argument('--dimensions', default="3x2", choices=['3x2', '3x3'])
args = parser.parse_args()


print("A confusion matrix C is such that Ci,j is equal to the number of observations known to be in group i but predicted to be in group j.")
print("If the classifier is nice, the diagonal is high because there are true positives")


if (args.api == "all"):
    dn = DameNamsor()
    if (args.dimensions == "3x2"):
        print("Namsor confusion matrix:\n")
        dn.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        namsor_confusion_matrix = dn.confusion_matrix(path=args.csv)
        print("Namsor confusion matrix:\n %s" % namsor_confusion_matrix)

    dg = DameGenderize()
    if (args.dimensions == "3x2"):
        print("Genderize confusion matrix:\n")
        dg.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        dg = DameGenderize()
        genderize_confusion_matrix = dg.confusion_matrix(path=args.csv)
        print("Genderize confusion matrix:\n %s" % genderize_confusion_matrix)

    dga = DameGenderApi()
    if (args.dimensions == "3x2"):
        print("Genderapi confusion matrix:\n")
        dga.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        dga = DameGenderApi()
        genderapi_confusion_matrix = dga.confusion_matrix(path=args.csv)
        print("Genderize confusion matrix:\n %s" % genderapi_confusion_matrix)

    dgg = DameGenderGuesser()
    if (args.dimensions == "3x2"):
        print("Gender Guesser confusion matrix:\n")
        dgg.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        genderguesser_confusion_matrix = dgg.confusion_matrix(path=args.csv)
        print("Gender Guesser confusion matrix:\n %s" % genderguesser_confusion_matrix)

    ds = DameSexmachine()
    if (args.dimensions == "3x2"):
        print("Damegender confusion matrix:\n")
        ds.print_confusion_matrix_dame(path=args.csv, ml=args.ml)
    elif (args.dimensions == "3x3"):
        ds = DameSexmachine()
        sexmachine_confusion_matrix = ds.confusion_matrix(path=args.csv)
        print("Damegender confusion matrix:\n %s" % sexmachine_confusion_matrix)

    # dna = DameNameapi()
    # if (args.dimensions == "3x2"):
    #     print("Nameapi confusion matrix:\n")
    #     dna.print_confusion_matrix_dame(path=args.csv)
    # elif (args.dimensions == "3x3"):
    #     nameapi_confusion_matrix = dna.confusion_matrix(path=args.csv)
    #     print("Nameapi confusion matrix:\n %s" % nameapi_confusion_matrix)


elif (args.api == "namsor"):
    dn = DameNamsor()
    if (args.dimensions == "3x2"):
        print("Namsor confusion matrix:\n")
        dn.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        namsor_confusion_matrix = dn.confusion_matrix(path=args.csv)
        print("Namsor confusion matrix:\n %s" % namsor_confusion_matrix)

elif (args.api == "genderize"):
    dg = DameGenderize()
    if (args.dimensions == "3x2"):
        print("Genderize confusion matrix:\n")
        dg.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        dg = DameGenderize()
        genderize_confusion_matrix = dg.confusion_matrix(path=args.csv)
        print("Genderize confusion matrix:\n %s" % genderize_confusion_matrix)

elif (args.api == "genderapi"):
    dga = DameGenderApi()
    if (args.dimensions == "3x2"):
        print("Genderapi confusion matrix:\n")
        dga.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        dga = DameGenderApi()
        genderapi_confusion_matrix = dga.confusion_matrix(path=args.csv)
        print("Genderize confusion matrix:\n %s" % genderapi_confusion_matrix)

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    if (args.dimensions == "3x2"):
        print("Gender Guesser confusion matrix:\n")
        dgg.print_confusion_matrix_dame(path=args.csv)
    elif (args.dimensions == "3x3"):
        genderguesser_confusion_matrix = dgg.confusion_matrix(path=args.csv)
        print("Gender Guesser confusion matrix:\n %s" % genderguesser_confusion_matrix)

elif (args.api == "damegender"):
    ds = DameSexmachine()
    if (args.dimensions == "3x2"):
        print("Damegender confusion matrix:\n")
        ds.print_confusion_matrix_dame(path=args.csv, ml=args.ml)
    elif (args.dimensions == "3x3"):
        ds = DameSexmachine()
        sexmachine_confusion_matrix = ds.confusion_matrix(path=args.csv)
        print("Damegender confusion matrix:\n %s" % sexmachine_confusion_matrix)

# elif (args.api == "nameapi"):
#     dna = DameNameapi()
#     if (args.dimensions == "3x2"):
#         print("Nameapi confusion matrix:\n")
#         dna.print_confusion_matrix_dame(path=args.csv)
#     elif (args.dimensions == "3x3"):
#         nameapi_confusion_matrix = dna.confusion_matrix(path=args.csv)
#         print("Nameapi confusion matrix:\n %s" % nameapi_confusion_matrix)

# elif (args.api == "customsearch"):
#     dc = DameCustomsearch()
#     print("Google Custom Search confusion matrix:\n")
#     dc.print_confusion_matrix_dame(path=args.csv)
