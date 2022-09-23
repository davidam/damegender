#!/usr/bin/python
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


import csv
import unidecode
import unicodedata
import configparser
import os
import re
import sys
import json
import datetime

from collections import OrderedDict
from app.dame_utils import DameUtils

csv.field_size_limit(3000000)

du = DameUtils()


class DameStatistics(object):
    # That's the root class in the heritage,
    # apis classes and sexmachine is a gender
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read('config.cfg')
        self.binary = {0: "female", 1: "male"}
        self.isoiec5218 = {0: "not know", 1: "male", 2: "female", 9: "not applicable"}
        self.males = 0
        self.females = 0
        self.unknown = 0

# METHODS ABOUT STATISTICS #

    def count_true2guess(self, truevector, guessvector, mytrue, myguess):
        # counting what is happenning between the true vector and
        # the guess vector
        i = 0
        count = 0
        if (len(truevector) >= len(guessvector)):
            maxi = len(guessvector)
        else:
            maxi = len(truevector)
        while (i < maxi):
            if ((truevector[i] == mytrue) and (guessvector[i] == myguess)):
                count = count + 1
            i = i + 1
        return count

    def femalefemale(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are female and
        # in the guess vector there are female
        # 
        # true positive in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        # true positive in jargon math (universe: female, male)
        # in the universe female male the property is to be female
        return self.count_true2guess(truevector, guessvector, 0, 0)

    def femalemale(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are female and
        # in the guess vector there are male
        #
        # true negative in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex
        # false positive in jargon math (universe: female, male)
        # in the universe female male the property is to be female
        return self.count_true2guess(truevector, guessvector, 0, 1)

    def femaleundefined(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are female and
        # in the guess vector there are undefined
        # 
        # true negative in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        return self.count_true2guess(truevector, guessvector, 0, 2)

    def malefemale(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are male and
        # in the guess vector there are female
        # 
        # true negative in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        # false negative in jargon math (universe: female, male)
        # in this universe the property it to be female        
        return self.count_true2guess(truevector, guessvector, 1, 0)

    def malemale(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are male and
        # in the guess vector there are male
        # 
        # true positive in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        # true negative in jargon math (universe: female, male)
        # in this universe the property it to be female
        return self.count_true2guess(truevector, guessvector, 1, 1)

    def maleundefined(self, truevector, guessvector):
        # how many times occurs that in the true vector there are male
        # and in the guess vector there are undefined
        # true negative in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        return self.count_true2guess(truevector, guessvector, 1, 2)

    def undefinedfemale(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are undefined and
        # in the guess vector there are female
        # false positive in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        return self.count_true2guess(truevector, guessvector, 2, 0)

    def undefinedmale(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are undefined
        # and in the guess vector there are male
        # false positive in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        return self.count_true2guess(truevector, guessvector, 2, 1)

    def undefinedundefined(self, truevector, guessvector):
        # how many times occurs that
        # in the true vector there are undefined and
        # in the guess vector there are undefined
        # false negative in jargon math (universe: female, male, undefined)
        # in this universe the property is to be defined and to be truth the sex        
        return self.count_true2guess(truevector, guessvector, 2, 2)
    
# STATISTICAL MEASURES LECTURES
# https://towardsdatascience.com/a-look-at-precision-recall-and-f1-score-36b5fd0dd3ec
# https://arxiv.org/abs/2010.16061
# https://github.com/davidam/damegender/blob/dev/manual/damegender.pdf
# https://en.wikipedia.org/wiki/Precision_and_recall
# https://peerj.com/articles/cs-156/

# One example about illness:
# Diagnostic     |   Illness (predicted)
# (verified)     +----------------------------
#                | Absence        | Presence
# Test negative  | True Negative  | False Negative
# Test positive  | False Positive | True Positive 

# One example about to be male:
# Diagnostic     |   To be male (predicted)
# (verified)     +----------------------------
#                | Absence        | Presence
# Test negative  | True Negative  | False Negative
# Test positive  | False Positive | True Positive 

# One example about to be precise guessing gender:
# You can detect "not know", "male", "female" or "not applicable"
# Diagnostic     |   To be precise guessing gender
# (verified)     |   (predicted)
#                +----------------------------
#                | Absence        | Presence
# Test negative  | True Negative  | False Negative
# Test positive  | False Positive | True Positive 
#

# Cosidering test condition in the column
# and predicted condition in the row ...
# One matrix with property to be male in the dimension female, male is:
# #####################
# femalefemale    malefemale
# femalemale      malemale
# #####################
# because female had been coded as 0 and male as 1
#

# This situation could be changed in the future
# TODO: ISO/IEC 5218 proposes a norm about coding gender
# ``0 as not know'',``1 as male'', ``2 as female''
# and ``9 as not applicable''

    def true_negative(self, testvector, guessvector, *args, **kwargs):
        dimension = kwargs.get('dimension', self.binary)
        if (dimension == self.binary):
            res = self.femalefemale(testvector, guessvector)
        return res

    def false_negative(self, testvector, guessvector, *args, **kwargs):
        dimension = kwargs.get('dimension', self.binary)
        if (dimension == self.binary):
            res = self.femalemale(testvector, guessvector)
        return res

    def false_positive(self, testvector, guessvector, *args, **kwargs):
        dimension = kwargs.get('dimension', self.binary)
        if (dimension == self.binary):
            res = self.malefemale(testvector, guessvector)
        return res

    def true_positive(self, testvector, guessvector, *args, **kwargs):
        withundefined = {"female": 0, "male": 1, "undefined": 2}
        dimension = kwargs.get('dimension', self.binary)
        if (dimension == self.binary):
            res = self.malemale(testvector, guessvector)
        return res
    
    def accuracy_score_dame(self, testvector, guessvector):
        # accuracy score is about successful between true and guess:
        # true positive + true negative dividing
        # true positive + true negative + false negative + false positive
        # femalefemale + malemale dividing the sum of all options
        # or
        # femalefemale + malemale + undefinedundefined dividing
        # by the sum of all options
        if ((2 in testvector) or (2 in guessvector)):
        # (femalefemale + malemale + undefinedundefined ) /
        # (femalefemale + malemale + malefemale + femalemale +
        # + femaleundefined + undefinedfemale + undefinedmale + maleundefined)
            if (len(testvector) == len(guessvector)):
                divider = self.femalefemale(testvector,
                                            guessvector)
                divider = divider + self.malemale(testvector,
                                                  guessvector)
                divider = divider + self.undefinedundefined(testvector,
                                                            guessvector)
                dividend = self.femalefemale(testvector,
                                             guessvector)
                dividend = dividend + self.femalemale(testvector,
                                                      guessvector)
                dividend = dividend + self.femaleundefined(testvector,
                                                           guessvector)
                dividend = dividend + self.malefemale(testvector,
                                                      guessvector)
                dividend = dividend + self.malemale(testvector,
                                                    guessvector)
                dividend = dividend + self.maleundefined(testvector,
                                                         guessvector)
                dividend = dividend + self.undefinedfemale(testvector,
                                                           guessvector)
                dividend = dividend + self.undefinedmale(testvector,
                                                         guessvector)
                dividend = dividend + self.undefinedundefined(testvector,
                                                              guessvector)
                result = divider / dividend
            else:
                result = 0
                print("Both vectors must have the same length")
                print("testvector length: %s" % len(testvector))
                print("guessvector length: %s" % len(guessvector))
                print("testvector: %s" % testvector)
                print("guessvector: %s" % guessvector)
        else:
        # (femalefemale + malemale ) /
        # (femalefemale + malemale +
        #   malefemale + femalemale)
            if (len(testvector) == len(guessvector)):
                divider = self.true_positive(testvector, guessvector)
                divider = divider + self.true_negative(testvector, guessvector)
                dividend = self.true_positive(testvector, guessvector)
                dividend = dividend + self.true_negative(testvector, guessvector)
                dividend = dividend + self.false_negative(testvector, guessvector)
                dividend = dividend + self.false_positive(testvector, guessvector)
                result = divider / dividend
            else:
                result = 0
                print("Both vectors must have the same length")
                print("testvector length: %s" % len(testvector))
                print("guessvector length: %s" % len(guessvector))
                print("testvector: %s" % testvector)
                print("guessvector: %s" % guessvector)
        return result

    def precision(self, testvector, guessvector):
        # precision is about successful in the predicted positive:
        # true positive dividing
        # true positive + false positive
        result = 0
        divider = self.true_positive(testvector, guessvector)
        dividend = self.true_positive(testvector, guessvector)
        dividend = dividend + self.false_positive(testvector, guessvector)
        try :
            result = divider / dividend
            # note that braces () are necessary here for multiple exceptions
        except(ZeroDivisionError, NameError):
            print("\nprecision has troubles with the zero division")
            print("\nand the zero is being given as result")            

        return result

    def recall(self, testvector, guessvector):
        # recall is about success in the actual positive:
        # true positive dividing
        # false negative + true positive
        result = 0
        
        if ((2 in testvector) or (2 in guessvector)):
            divider = self.femalefemale(testvector, guessvector)
            divider = divider + self.malemale(testvector, guessvector)
            dividend = self.femalefemale(testvector, guessvector)
            dividend = dividend + self.malemale(testvector, guessvector)
            dividend = dividend + self.malefemale(testvector, guessvector)
            dividend = dividend + self.femaleundefined(testvector, guessvector)
            dividend = dividend + self.maleundefined(testvector, guessvector)
        else:
            divider = self.true_positive(testvector, guessvector)
            dividend = self.false_negative(testvector, guessvector)
            dividend = self.true_positive(testvector, guessvector)
        result = divider / dividend
        return result

    def f1score(self, testvector, guessvector):
        # f1score is about precision and recall:
        # 2 multiplied by
        # (precision * recall) divided by
        # (precision + recall)
        result = 0
        divider = self.precision(testvector, guessvector)
        divider = divider * self.recall(testvector, guessvector)
        dividend = self.precision(testvector, guessvector)
        dividend = dividend + self.recall(testvector, guessvector)
        result = 2 * (divider / dividend)
        return result

    def error_coded(self, testvector, guessvector):
        # error coded is about errors 
        # divided by all results
        result = 0
        divider = self.femalemale(testvector, guessvector)
        divider = divider + self.malefemale(testvector, guessvector)
        divider = divider + self.femaleundefined(testvector, guessvector)
        divider = divider + self.maleundefined(testvector, guessvector)
        divider = divider + self.undefinedfemale(testvector, guessvector)
        divider = divider + self.undefinedmale(testvector, guessvector)
        dividend = self.femalefemale(testvector, guessvector)
        dividend = dividend + self.femalemale(testvector, guessvector)
        dividend = dividend + self.femaleundefined(testvector, guessvector)        
        dividend = dividend + self.malefemale(testvector, guessvector)
        dividend = dividend + self.malemale(testvector, guessvector)
        dividend = dividend + self.maleundefined(testvector, guessvector)
        dividend = dividend + self.undefinedmale(testvector, guessvector)
        dividend = dividend + self.undefinedfemale(testvector, guessvector)
        dividend = dividend + self.undefinedundefined(testvector, guessvector)        
        result = divider / dividend
        return result

    def error_coded_without_na(self, testvector, guessvector):
        # error coded without na is about errors
        # without taking into account missing values
        result = 0
        divider = self.femalemale(testvector, guessvector)
        divider = divider + self.malefemale(testvector, guessvector)
        dividend = self.malemale(testvector, guessvector)
        dividend = dividend + self.femalemale(testvector, guessvector)
        dividend = dividend + self.malefemale(testvector, guessvector)
        dividend = dividend + self.femalefemale(testvector, guessvector)
        result = divider / dividend
        return result

    def na_coded(self, testvector, guessvector):
        # this measure is about 
        # missing values divided by
        # all results
        result = 0
        divider = self.maleundefined(testvector, guessvector)
        divider = divider + self.femaleundefined(testvector, guessvector)
        divider = divider + self.undefinedfemale(testvector, guessvector)
        divider = divider + self.undefinedmale(testvector, guessvector)         
        dividend = self.malemale(testvector, guessvector)
        dividend = dividend + self.femalemale(testvector, guessvector)
        dividend = dividend + self.malefemale(testvector, guessvector)
        dividend = dividend + self.femalefemale(testvector, guessvector)
        dividend = dividend + self.maleundefined(testvector, guessvector)
        dividend = dividend + self.femaleundefined(testvector, guessvector)
        dividend = dividend + self.undefinedmale(testvector, guessvector)
        dividend = dividend + self.undefinedfemale(testvector, guessvector)
        dividend = dividend + self.undefinedundefined(testvector, guessvector)        
        result = divider / dividend
        return result

    def error_gender_bias(self, testvector, guessvector):
        # this measure is about the error is doing biases
        # in males or in females
        divider = self.malefemale(testvector, guessvector)
        divider = divider - self.femalemale(testvector, guessvector)
        dividend = self.malemale(testvector, guessvector)
        dividend = dividend + self.femalemale(testvector, guessvector)
        dividend = dividend + self.malefemale(testvector, guessvector)
        dividend = dividend + self.femalefemale(testvector, guessvector)
        result = divider / dividend
        return result

    def weighted_error(self, testvector, guessvector, w):
        # this measure is about the error giving a weight w
        # https://peerj.com/articles/cs-156/
        divider = self.femalemale(testvector, guessvector)
        divider = divider + self.malefemale(testvector, guessvector)
        dot = self.maleundefined(testvector, guessvector)
        dot = dot + self.femaleundefined(testvector, guessvector)
        divider = divider + w * dot
        dividend = self.malemale(testvector, guessvector)
        dividend = dividend + self.femalemale(testvector, guessvector)
        dividend = dividend + self.malefemale(testvector, guessvector)
        dividend = dividend + self.femalefemale(testvector, guessvector)
        dot = self.maleundefined(testvector, guessvector)
        dot = dot + self.femaleundefined(testvector, guessvector)
        dividend = dividend + w * dot
        result = divider / dividend
        return result

    def confusion_matrix_table(self, testvector, guessvector):
        # this method returns a 3x3 confusion matrix as python vectors
        # femalefemale
        self.ff = self.count_true2guess(testvector, guessvector, 0, 0)
        # femalemale
        self.fm = self.count_true2guess(testvector, guessvector, 0, 1)
        # femaundefined
        self.fu = self.count_true2guess(testvector, guessvector, 0, 2)
        # malefemale
        self.mf = self.count_true2guess(testvector, guessvector, 1, 0)
        # malemale
        self.mm = self.count_true2guess(testvector, guessvector, 1, 1)
        # maleundefined
        self.mu = self.count_true2guess(testvector, guessvector, 1, 2)
        # undefinedfemale
        self.uf = self.count_true2guess(testvector, guessvector, 1, 0)
        # undefinedmale
        self.um = self.count_true2guess(testvector, guessvector, 1, 1)
        # undefinedundefined
        self.uu = self.count_true2guess(testvector, guessvector, 1, 2)

        l1 = [[self.ff, self.fm, self.fu],
              [self.mf, self.mm, self.mu],
              [self.uf, self.um, self.uu]]

        res = [[l1[0][0], l1[0][1], l1[0][2]],
               [l1[1][0], l1[1][1], l1[1][2]],
               [l1[2][0], l1[2][1], l1[2][2]]]
        return res

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
        gl = self.csv2gender_list(path=path)
        print("%s confusion matrix:\n" % api)
        if (os.path.isfile(jsonf)):
            self.print_confusion_matrix_gender(path=path,
                                               dimensions=dimensions,
                                               jsonf=jsonf,
                                               reverse=reverse)
        elif (args.jsondownloaded == ''):
            self.print_confusion_matrix_gender(path=path,
                                               dimensions=dimensions,
                                               reverse=reverse)
        else:
            print("In the path %s doesn't exist file" % jsonf)
