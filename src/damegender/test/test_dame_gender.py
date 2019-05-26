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

import unittest
import numpy as np
import os
from app.dame_gender import Gender

class TddInPythonExample(unittest.TestCase):

    def test_dame_gender_in_dict_method_returns_correct_result(self):
        g = Gender()
        self.assertEqual(g.in_dict("Table"), True)
        self.assertEqual(g.in_dict("Mesa"), True)

    def test_dame_gender_features_method_returns_correct_result(self):
        g = Gender()
        f = g.features("David")
        self.assertEqual(f['has(a)'], True)
        self.assertEqual(f['count(i)'], 1)
        self.assertEqual(f['count(v)'], 1)
        self.assertEqual(f['last_letter'], 'd')
        self.assertEqual(f['first_letter'], 'd')

    def test_dame_gender_features_int_method_returns_correct_result(self):
        g = Gender()
        features_int = g.features_int("David")
        self.assertTrue(features_int["first_letter"] == 100)
        self.assertTrue(features_int["last_letter"] == 100)
        self.assertTrue(features_int["vocals"] == 2)
        self.assertTrue(features_int["consonants"] == 2)
        self.assertTrue(features_int["first_letter_vocal"] == 0)
        self.assertTrue(features_int["last_letter_vocal"] == 0)
        self.assertTrue(features_int["first_letter_consonant"] == 1)
        self.assertTrue(features_int["last_letter_consonant"] == 1)
        #self.assertTrue(features_int["syllables"] == 2)
        self.assertTrue(features_int["last_letter_a"] == 0)
        self.assertTrue(len(features_int) > 0)

    def test_dame_gender_males_list_method_returns_correct_result(self):
        g = Gender()
        m = g.males_list()
        self.assertTrue("Adrian" in m)

    def test_dame_gender_females_list_method_returns_correct_result(self):
        g = Gender()
        f = g.females_list()
        self.assertTrue("Eva" in f)

    def test_dame_gender_name2gender_in_dataset_method_returns_correct_result(self):
        g = Gender()
        guess = g.name2gender_in_dataset("David", dataset='files/names/names_es')
        self.assertTrue(guess, 1)
        guess = g.name2gender_in_dataset("David", dataset='files/names/all.csv')
        self.assertTrue(guess, 1)
        guess = g.name2gender_in_dataset("David", dataset='files/names/yob2017.csv')
        self.assertTrue(guess, 1)
        guess = g.name2gender_in_dataset("Laura", dataset='files/names/names_es')
        self.assertTrue(guess, 0)
        guess = g.name2gender_in_dataset("Laura", dataset='files/names/all.csv')
        self.assertTrue(guess, 0)
        guess = g.name2gender_in_dataset("Laura", dataset='files/names/yob2017.csv')
        self.assertTrue(guess, 0)
        guess = g.name2gender_in_dataset("Teppei", dataset='files/names/yob2017.csv')
        self.assertTrue(guess, 2)
        guess = g.name2gender_in_dataset("Filka", dataset='files/names/nam_dict.txt')
        self.assertTrue(guess, 0)

    def test_dame_gender_guess_method_returns_correct_result(self):
        g = Gender()
        r = g.guess(name="David", binary=True)
        self.assertEqual(r, 1)
        r = g.guess(name="Andrea", binary=True)
        self.assertEqual(r, 2)
        r = g.guess(name="David", binary=False)
        self.assertEqual(r, "male")
        r = g.guess(name="Laura", binary=True)
        self.assertEqual(r, 0)
        r = g.guess(name="Laura", binary=False)
        self.assertEqual(r, "female")
        r = g.guess(name="Andrea", binary=True)
        self.assertEqual(r, 2)

    def test_dame_gender_csv2names_method_returns_correct_result(self):
        g = Gender()
        names = g.csv2names(path='files/names/partial.csv')
        self.assertTrue(len(names) > 10)

    def test_dame_gender_guess_list_method_returns_correct_result(self):
        g = Gender()
        self.assertEqual(['unknown', 'male', 'male', 'male', 'unknown', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'male', 'unknown', 'male', 'male', 'male', 'female', 'male', 'unknown'], g.guess_list(path="files/names/partial.csv", binary=False))
        self.assertEqual([2, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2], g.guess_list(path="files/names/partial.csv",binary=True))


    # def test_dame_gender_accuracy_method_returns_correct_result(self):
    #     g = Gender()
    #     self.assertTrue(g.accuracy(path="files/names/partial.csv") >= 0.5)

    def test_dame_gender_confusion_matrix_method_returns_correct_result(self):
        g = Gender()
        cm = g.confusion_matrix(path="files/names/partial.csv")
        print(cm)
        am = np.array([[3, 0, 0],[0, 13, 3],[0, 1, 1]])
        self.assertTrue(np.array_equal(cm,am))

    # def test_gender_guess_list_method_returns_correct_result(self):
    #     g = Gender()
    #     string = g.guess_list(path="files/names/partial.csv", binary=False)
    #     self.assertEqual('thomas', g.remove_quotes(string))
#        self.assertEqual([1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], g.guess_list(path="file/partial.csv",binary=True))


    def test_dame_gender_gender_list_method_returns_correct_result(self):
        g = Gender()
        gl = g.gender_list()
        self.assertEqual(gl, [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(g.females, 3)
        self.assertEqual(g.males, 16)
        self.assertEqual(g.unknown, 2)

    def test_dame_gender_dataset2genderlist_method_returns_correct_result(self):
        g = Gender()
        gl = g.dataset2genderlist(dataset="files/names/all.csv")
        self.assertEqual(gl[0:4], [1, 1, 1, 1])
        gl2 = g.dataset2genderlist(dataset="files/names/yob2017.txt")
        self.assertEqual(gl2[0:4], [0, 0, 0, 0])

    def test_dame_gender_features_list_method_returns_correct_result(self):
        g = Gender()
        fl = g.features_list()
        self.assertTrue(len(fl) > 20)

    def test_dame_gender_features_list_categorical_method_returns_correct_result(self):
        g = Gender()
        flc = g.features_list_categorical('files/names/partial.csv')
        self.assertEqual(len(flc[0]), 6)
        self.assertEqual(flc[0], [112, 101, 0, 0, 1, 0])

    def test_dame_gender_features_list_noundefined_method_returns_correct_result(self):
        g = Gender()
        flnu = g.features_list_no_undefined('files/names/allnoundefined.csv')
        self.assertTrue(len(flnu) > 5000)

    def test_dame_gender_features_list_no_categorical_method_returns_correct_result(self):
        g = Gender()
        flnc = g.features_list_no_categorical('files/names/partial.csv')
        self.assertTrue(len(flnc[0]) > 25)
        self.assertTrue(flnc[0], [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3])

    def test_dame_gender_features_list_no_letters_method_returns_correct_result(self):
        g = Gender()
        flnl = g.features_list_no_letters('files/names/partial.csv')
        self.assertTrue(len(flnl[0]) > 5)
        self.assertEqual(flnl[0], [112, 101, 0, 0, 1, 0])

    def test_dame_gender_features_list2csv_method_returns_correct_result(self):
        # TODO: You can write asserts to verify the first line
        g = Gender()
        csv1 = g.features_list2csv(path="files/names/min.csv")
        csv2 = g.features_list2csv(path="files/names/min.csv", categorical="categorical")
        csv3 = g.features_list2csv(path="files/names/min.csv", categorical="nocategorical")
        csv4 = g.features_list2csv(path="files/names/allnoundefined.csv", categorical="noundefined")
        self.assertTrue(os.path.isfile("files/features_list.csv"))
        file = open("files/features_list.csv", "r")
        if (file):
            self.assertTrue(os.path.isfile("files/features_list_cat.csv"))
            self.assertTrue(os.path.isfile("files/features_list_no_cat.csv"))
            self.assertTrue(os.path.isfile("files/features_list_no_undefined.csv"))

    def test_dame_gender_dame_accuracy_score_dame_method_returns_correct_result(self):
       g = Gender()
       score1 = g.accuracy_score_dame([1, 1], [1, 1])
       self.assertEqual(score1, 1)
       score2 = g.accuracy_score_dame([1, 1, 1, 0], [1, 1, 2, 0])
       self.assertEqual(score2, 0.75)
       score3 = g.accuracy_score_dame([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1])
       self.assertEqual(score3, 1)
       score4 = g.accuracy_score_dame([1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
       self.assertEqual(score4, 1)

    def test_dame_gender_count_true2guess_method_returns_correct_result(self):
        g = Gender()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(g.count_true2guess(v1, v2, 1, 1), 2)
        vv1 = [1, 0, 1, 1, 1]
        vv2 = [1, 1, 1, 0]
        self.assertEqual(g.count_true2guess(vv2, vv1, 1, 1), 2) # malemale
        self.assertEqual(g.count_true2guess(vv2, vv1, 0, 1), 1) # femalemale
        self.assertEqual(g.count_true2guess(vv2, vv1, 1, 0), 1) # malefemale

    def test_dame_gender_error_coded_method_returns_correct_result(self):
        g = Gender()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(g.error_coded(v1, v2), 0.5)

    def test_dame_gender_error_coded_without_na_method_returns_correct_result(self):
        g = Gender()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(g.error_coded(v1, v2), 0.5)

    def test_dame_gender_error_coded_without_na_method_returns_correct_result(self):
        g = Gender()
        v1 = [1, 0, 1, 1, 1]
        v2 = [1, 1, 1, 0, 1]
        self.assertEqual(g.error_coded(v1, v2), 0.4)

    def test_dame_gender_na_coded_method_returns_correct_result(self):
        g = Gender()
        v1 = [0, 1, 1, 1]
        v2 = [2, 0, 1, 1]
        self.assertEqual(g.na_coded(v1, v2), 0.25)

    # def test_dame_gender_ine_frec_method_returns_correct_result(self):
    #     g = Gender()
    #     ines = g.ine_frec("INES")
    #     self.assertEqual(int(ines['females']), 61337)
    #     self.assertEqual(int(ines['males']), 0)
    #     bea = g.ine_frec("BEATRIZ")
    #     self.assertTrue(int(bea['females']) > 10)


    def test_dame_gender_name_frec_method_returns_correct_result(self):
        g = Gender()
        frec1 = g.name_frec("INES", dataset='ine')
        self.assertEqual(int(frec1['females']), 61337)
        self.assertEqual(int(frec1['males']), 0)
        frec2 = g.name_frec("BEATRIZ", dataset='ine')
        self.assertTrue(int(frec2['females']) > 10)
        frec3 = g.name_frec("ALMUDENA", dataset='ine')
        self.assertTrue(int(frec2['females']) > 10)
        frec4 = g.name_frec("JULIA", dataset='uscensus')
        self.assertTrue(int(frec2['females']) > 10)
        frec5 = g.name_frec("ELISABETH", dataset='uscensus')
        self.assertTrue(int(frec2['females']) > 10)
        frec6 = g.name_frec("MARIA", dataset='ukcensus')
        self.assertTrue(int(frec6['females']) > 10)


    def test_dame_gender_error_gender_bias_method_returns_correct_result(self):
        g = Gender()
        v1 = [0, 1, 1, 1]
        v2 = [0, 0, 1, 1]
        self.assertEqual(g.error_gender_bias(v1, v2), 0.25)


    # def test_dame_gender_weighted_error_method_returns_correct_result(self):
    #     g = Gender()
    #     v1 = [1, 0, 1, 1, 1]
    #     v2 = [1, 1, 0, 1, 1]
    #     self.assertEqual(g.weighted_error(v1, v2, 2), 0.4)
