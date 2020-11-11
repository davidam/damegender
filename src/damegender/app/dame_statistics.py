#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

#from nltk.corpus import names
#import nltk

import csv
import unidecode
import unicodedata
import numpy as np
import configparser
import os
import re
import sys
import json
import datetime

from collections import OrderedDict
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from app.dame_utils import DameUtils

csv.field_size_limit(3000000)

du = DameUtils()
#g = Gender()

class DameStatistics(object):
    # That's the root class in the heritage,
    # apis classes and sexmachine is a gender
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read('config.cfg')
        self.males = 0
        self.females = 0
        self.unknown = 0
        
# METHODS ABOUT STATISTICS #

    def count_true2guess(self, truevector, guessvector, true, guess):
        i = 0
        count = 0
        if (len(truevector) >= len(guessvector)):
            maxi = len(guessvector)
        else:
            maxi = len(truevector)
        while (i < maxi):
            if ((truevector[i] == true) and (guessvector[i] == guess)):
                count = count + 1
            i = i + 1
        return count

    def femalefemale(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 0, 0)

    def femalemale(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 0, 1)

    def femaleundefined(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 0, 2)

    def malefemale(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 1, 0)

    def malemale(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 1, 1)

    def maleundefined(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 1, 2)

    def undefinedfemale(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 2, 0)

    def undefinedmale(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 2, 1)

    def undefinedundefined(self, truevector, guessvector):
        return self.count_true2guess(truevector, guessvector, 2, 2)

    def accuracy_score_dame(self, truevector, guessvector):
        if (len(truevector) == len(guessvector)):
            divider = self.femalefemale(truevector, guessvector)
            divider = divider + self.malemale(truevector, guessvector)
            dividend = self.femalefemale(truevector, guessvector)
            dividend = dividend + self.malemale(truevector, guessvector)
            dividend = dividend + self.malefemale(truevector, guessvector)
            dividend = dividend + self.femalemale(truevector, guessvector)
            dividend = dividend + self.femaleundefined(truevector, guessvector)
            dividend = dividend + self.maleundefined(truevector, guessvector)
            result = divider / dividend
        else:
            result = 0
            print("Both vectors must have the same length")
            print("truevector length: %s" % len(truevector))
            print("guessvector length: %s" % len(guessvector))
            print("truevector: %s" % truevector)
            print("guessvector: %s" % guessvector)
        return result

    def precision(self, truevector, guessvector):
        result = 0
        divider = self.femalefemale(truevector, guessvector)
        divider = divider + self.malemale(truevector, guessvector)
        dividend = self.femalefemale(truevector, guessvector)
        dividend = dividend + self.malemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        result = divider / dividend
        return result

    def recall(self, truevector, guessvector):
        result = 0
        divider = self.femalefemale(truevector, guessvector)
        divider = divider + self.malemale(truevector, guessvector)
        dividend = self.femalefemale(truevector, guessvector)
        dividend = dividend + self.malemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        dividend = dividend + self.femaleundefined(truevector, guessvector)
        dividend = dividend + self.maleundefined(truevector, guessvector)
        result = divider / dividend
        return result

    def f1score(self, truevector, guessvector):
        result = 0
        divider = self.precision(truevector, guessvector)
        divider = divider * self.recall(truevector, guessvector)
        dividend = self.precision(truevector, guessvector)
        dividend = dividend + self.recall(truevector, guessvector)
        result = 2 * (divider / dividend)
        return result

    def error_coded(self, truevector, guessvector):
        result = 0
        divider = self.femalemale(truevector, guessvector)
        divider = divider + self.malefemale(truevector, guessvector)
        divider = divider + self.maleundefined(truevector, guessvector)
        divider = divider + self.femaleundefined(truevector, guessvector)
        dividend = self.malemale(truevector, guessvector)
        dividend = dividend + self.femalemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        dividend = dividend + self.femalefemale(truevector, guessvector)
        dividend = dividend + self.maleundefined(truevector, guessvector)
        dividend = dividend + self.femaleundefined(truevector, guessvector)
        result = divider / dividend
        return result

    def error_coded_without_na(self, truevector, guessvector):
        result = 0
        divider = self.femalemale(truevector, guessvector)
        divider = divider + self.malefemale(truevector, guessvector)
        dividend = self.malemale(truevector, guessvector)
        dividend = dividend + self.femalemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        dividend = dividend + self.femalefemale(truevector, guessvector)
        result = divider / dividend
        return result

    def na_coded(self, truevector, guessvector):
        result = 0
        divider = self.maleundefined(truevector, guessvector)
        divider = divider + self.femaleundefined(truevector, guessvector)
        dividend = self.malemale(truevector, guessvector)
        dividend = dividend + self.femalemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        dividend = dividend + self.femalefemale(truevector, guessvector)
        dividend = dividend + self.maleundefined(truevector, guessvector)
        dividend = dividend + self.femaleundefined(truevector, guessvector)
        result = divider / dividend
        return result

    def error_gender_bias(self, truevector, guessvector):
        divider = self.malefemale(truevector, guessvector)
        divider = divider - self.femalemale(truevector, guessvector)
        dividend = self.malemale(truevector, guessvector)
        dividend = dividend + self.femalemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        dividend = dividend + self.femalefemale(truevector, guessvector)
        result = divider / dividend
        return result

    def weighted_error(self, truevector, guessvector, w):
        divider = self.femalemale(truevector, guessvector)
        divider = divider + self.malefemale(truevector, guessvector)
        dot = self.maleundefined(truevector, guessvector)
        dot = dot + self.femaleundefined(truevector, guessvector)
        divider = divider + w * dot
        dividend = self.malemale(truevector, guessvector)
        dividend = dividend + self.femalemale(truevector, guessvector)
        dividend = dividend + self.malefemale(truevector, guessvector)
        dividend = dividend + self.femalefemale(truevector, guessvector)
        dot = self.maleundefined(truevector, guessvector)
        dot = dot + self.femaleundefined(truevector, guessvector)
        dividend = dividend + w * dot
        result = divider / dividend
        return result

    
    def confusion_matrix_table(self, truevector, guessvector):
        # this method returns a 3x3 confusion matrix as python vectors
        # femalefemale
        self.ff = self.count_true2guess(truevector, guessvector, 0, 0)
        # femalemale
        self.fm = self.count_true2guess(truevector, guessvector, 0, 1)
        # femaundefined
        self.fu = self.count_true2guess(truevector, guessvector, 0, 2)
        # malefemale
        self.mf = self.count_true2guess(truevector, guessvector, 1, 0)
        # malemale
        self.mm = self.count_true2guess(truevector, guessvector, 1, 1)
        # maleundefined
        self.mu = self.count_true2guess(truevector, guessvector, 1, 2)
        # undefinedfemale
        self.uf = self.count_true2guess(truevector, guessvector, 1, 0)
        # undefinedmale
        self.um = self.count_true2guess(truevector, guessvector, 1, 1)
        # undefinedundefined
        self.uu = self.count_true2guess(truevector, guessvector, 1, 2)

        l = [[self.ff, self.fm, self.fu],
             [self.mf, self.mm, self.mu],
             [self.uf, self.um, self.uu]]

        res = [[l[0][0], l[0][1], l[0][2]],
               [l[1][0], l[1][1], l[1][2]],
               [l[2][0], l[2][1], l[2][2]]]
        return res




    # def pca(self, path='files/names/partial.csv', n=2):
    #     X = np.array(g.features_list())
    #     pca = PCA(n_components=n)
    #     return pca.fit(X)

    # def print_envolve_measures
    #     if (ds.json_eq_csv_in_names(jsonf=args.jsondownloaded, path=args.csv)):
    #         print("################### Damegender!!")
    #         print("Gender list: " + str(gl))
    #         sl = ds.json2guess_list(jsonf=args.jsondownloaded, binary=True)
    #         print("Guess list:  " +str(sl))
    #         ds.print_measures(gl, sl, args.measure, "Damegender")
    #     else:
    #         print("Names in json and csv are differents")
    #         print("Names in csv: %s:" % ds.csv2names(path=args.csv))
    #         print("Names in json: %s:" % ds.json2names(jsonf=args.jsondownloaded, surnames=False))


    def print_measures(self, gl1, gl2, measure, api_name):
        if (measure == "accuracy"):
            gender_accuracy = self.accuracy_score_dame(gl1, gl2)
            print("%s accuracy: %s" % (api_name, gender_accuracy))

        elif (measure == "precision"):
            gender_precision = self.precision(gl1, gl2)
            print("%s precision: %s" % (api_name, gender_precision))

        elif (measure == "recall"):
            gender_recall = self.recall(gl1, gl1)
            print("%s recall: %s" % (api_name, gender_recall))
        elif (measure == "f1score"):
            gender_f1score = self.f1score(gl1, gl2)
            print("%s f1score: %s" % (api_name, gender_f1score))

    def pretty_cm(self, path, jsonf, *args, **kwargs):
        api = kwargs.get('api', 'damegender')
        reverse = kwargs.get('reverse', False)
        dimensions = kwargs.get('dimensions', '3x2')
        gl = self.gender_list(path=path)
#        dna = DameNameapi()
        print("%s confusion matrix:\n" % api)
        #    dna.print_confusion_matrix_gender(path=args.csv, dimensions=args.dimensions)
        if (os.path.isfile(jsonf)):
            self.print_confusion_matrix_gender(path=path, dimensions=dimensions, jsonf=jsonf, reverse=reverse)
        elif (args.jsondownloaded == ''):
            self.print_confusion_matrix_gender(path=path, dimensions=dimensions, reverse=reverse)
        else:
            print("In the path %s doesn't exist file" % jsonf)

