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
from app.dame_genderize import DameGenderize
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_nameapi import DameNameapi
from app.dame_customsearch import DameCustomsearch

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--csv', default="files/names/min.csv")
parser.add_argument('--api', default="damegender", choices=['customsearch', 'namsor', 'genderize', 'genderguesser', 'damegender', 'genderapi', 'nameapi', 'all'])
parser.add_argument('--ml', default="nltk", choices=['nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB'])
args = parser.parse_args()

if (args.api == "all"):

    dn = DameNamsor()
    print("################### Namsor!!")
    gl = dn.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dn.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))

    namsor_accuracy = dn.accuracy_score_dame(gl, sl)

    #print(dn.accuracy_score_dame([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1]))
    #namsor_accuracy = dn.accuracy_score_dame([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1])

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
    print("################### Dame Gender!!")
    gl = ds.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = ds.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))

    sexmachine_accuracy = ds.accuracy_score_dame(gl,sl)
    print("Sexmachine accuracy: %s" % sexmachine_accuracy)

    dga = DameGenderApi()
    print("################### GenderApi!!")
    gl = dga.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dga.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    genderapi_accuracy = dga.accuracy_score_dame(gl,sl)
    print("Genderapi accuracy: %s" % genderapi_accuracy)

    
    dna = DameNameapi()
    print("################### Nameapi!!")
    gl = dna.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dna.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    nameapi_accuracy = dna.accuracy_score_dame(gl,sl)
    print("Nameapi accuracy: %s" % nameapi_accuracy)

elif (args.api == "namsor"):
    dn = DameNamsor()
    print("################### Namsor!!")
    gl = dn.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dn.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    namsor_accuracy = dn.accuracy_score_dame(gl, sl)
    print("Namsor accuracy: %s" % namsor_accuracy)

elif (args.api == "genderize"):
    dg = DameGenderize()
    print("################### Genderize!!")
    gl = dg.gender_list(path=args.csv)

    print("Gender list: " + str(gl))
    sl = dg.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(gl))
    genderize_accuracy = dg.accuracy_score_dame(gl, sl)
    print("Genderize accuracy: %s" % genderize_accuracy)

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    print("################### GenderGuesser!!")
    gl = dgg.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dgg.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    genderguesser_accuracy = dgg.accuracy_score_dame(gl,sl)
    print("GenderGuesser accuracy: %s" % genderguesser_accuracy)

elif (args.api == "customsearch"):
    dc = DameCustomsearch()
    print("################### Google Custom Search!!")
    gl = dc.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dc.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    customsearch_accuracy = dc.accuracy_score_dame(gl,sl)
    print("Google Custom Search: %s" % customsearch_accuracy)


elif (args.api == "damegender"):

    # ds = DameSexmachine()
    # print("################### Dame Gender!!")
    # gl = ds.gender_list(path=args.csv)
    # print("Gender list: " + str(gl))
    # sl = ds.guess_list(path=args.csv, binary=True)
    # print("Guess list:  " +str(sl))
    # sexmachine_accuracy = ds.accuracy_score_dame(gl,sl)
    # print("Sexmachine accuracy: %s" % sexmachine_accuracy)

    if (args.ml == "nltk"):
        ds = DameSexmachine()
        print("################### NLTK!!")
        gl1 = ds.gender_list(path=args.csv)
        print("Gender list: " + str(gl1))
        gl2 = ds.guess_list(path=args.csv, binary=True)
        print("Guess list:  " +str(gl2))
        nltk_accuracy = ds.accuracy_score_dame(gl1, gl2)
        print("Dame Gender accuracy: %s" % nltk_accuracy)

    elif (args.ml == "svc"):
        ds = DameSexmachine()
        print("################### Support Vector Machines!!")
        gl1 = ds.gender_list(path=args.csv)
        print("Gender list: " + str(gl1))
        gl2 = ds.guess_list(path=args.csv, binary=True, ml="svc")
        print("Guess list:  " +str(gl2))
        svc_accuracy = ds.accuracy_score_dame(gl1, gl2)
        print("Support Vector Machines accuracy: %s" % svc_accuracy)

    elif (args.ml == "sgd"):
        ds = DameSexmachine()
        print("################### Stochastic Gradient Descent!!")
        gl1 = ds.gender_list(path=args.csv)
        print("Gender list: " + str(gl1))
        gl2 = ds.guess_list(path=args.csv, binary=True, ml="sgd")
        print("Guess list:  " +str(gl2))
        sgd_accuracy = ds.accuracy_score_dame(gl1, gl2)
        print("Stochastic Gradient Descendent accuracy: %s" % sgd_accuracy)

    elif (args.ml == "gaussianNB"):
        ds = DameSexmachine()
        print("################### Gaussian Naive Bayes!!")
        gl1 = ds.gender_list(path=args.csv)
        print("Gender list: " + str(gl1))
        gl2 = ds.guess_list(path=args.csv, binary=True, ml="gaussianNB")
        print("Guess list:  " +str(gl2))
        gaussianNB_accuracy = ds.accuracy_score_dame(gl1, gl2)
        print("Gaussian Naive Bayes accuracy: %s" % gaussianNB_accuracy)

    elif (args.ml == "multinomialNB"):
        ds = DameSexmachine()
        print("################### Multinomial Naive Bayes!!")
        gl1 = ds.gender_list(path=args.csv)
        print("Gender list: " + str(gl1))
        gl2 = ds.guess_list(path=args.csv, binary=True, ml="multinomialNB")
        print("Guess list:  " +str(gl2))
        multinomialNB_accuracy = ds.accuracy_score_dame(gl1, gl2)
        print("Multinomial Naive Bayes accuracy: %s" % multinomialNB_accuracy)

    elif (args.ml == "bernoulliNB"):
        ds = DameSexmachine()
        print("################### Bernoulli Naive Bayes!!")
        gl1 = ds.gender_list(path=args.csv)
        print("Gender list: " + str(gl1))
        gl2 = ds.guess_list(path=args.csv, binary=True, ml="bernoulliNB")
        print("Guess list:  " +str(gl2))
        bernoulliNB_accuracy = ds.accuracy_score_dame(gl1, gl2)
        print("Bernoulli Naive Bayes accuracy: %s" % bernoulliNB_accuracy)



elif (args.api == "genderapi"):
    dga = DameGenderApi()
    print("################### GenderApi!!")
    gl = dga.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dga.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    genderapi_accuracy = dga.accuracy_score_dame(gl,sl)
    print("Genderapi accuracy: %s" % genderapi_accuracy)

elif (args.api == "nameapi"):
    dna = DameNameapi()
    print("################### Nameapi!!")
    gl = dna.gender_list(path=args.csv)
    print("Gender list: " + str(gl))
    sl = dna.guess_list(path=args.csv, binary=True)
    print("Guess list:  " +str(sl))
    nameapi_accuracy = dna.accuracy_score_dame(gl,sl)
    print("Nameapi accuracy: %s" % nameapi_accuracy)
