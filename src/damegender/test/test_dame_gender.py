#!/usr/bin/python3
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


import unittest
import numpy as np
import os
import collections
collections.Callable = collections.abc.Callable

from app.dame_gender import Gender


class TddInPythonExample(unittest.TestCase):

    def test_dame_gender_features(self):
        g = Gender()
        f = g.features("David")
        self.assertEqual(f['has(a)'], True)
        self.assertEqual(f['count(i)'], 1)
        self.assertEqual(f['count(v)'], 1)
        self.assertEqual(f['last_letter'], 'd')
        self.assertEqual(f['first_letter'], 'd')

    def test_dame_gender_features_int(self):
        g = Gender()
        features_int = g.features_int("David")
#        self.assertTrue(features_int["first_letter"] == 100)
        self.assertTrue(features_int["last_letter"] == 100)
        self.assertTrue(features_int["vocals"] == 2)
        self.assertTrue(features_int["consonants"] == 2)
#        self.assertTrue(features_int["first_letter_vocal"] == 0)
        self.assertTrue(features_int["last_letter_vocal"] == 0)
#        self.assertTrue(features_int["first_letter_consonant"] == 1)
        self.assertTrue(features_int["last_letter_consonant"] == 1)
        self.assertTrue(features_int["last_letter_a"] == 0)
        self.assertEqual(len(features_int), 36)

    def test_dame_gender_males_list(self):
        g = Gender()
        m = g.males_list(corpus="es")
        self.assertTrue("ADRIAN" in m)
        self.assertTrue(len(m) > 24511)

    def test_dame_gender_females_list(self):
        g = Gender()
        f = g.females_list(corpus="es")
        self.assertTrue("EVA" in f)
        self.assertTrue(len(f) > 24818)
        f3 = g.females_list(corpus="ie")
        self.assertTrue("Anna" in f3)

    def test_dame_gender_filenamdict2list(self):
        g = Gender()
        name = g.filenamdict2list()[0]
        self.assertEqual(name, "Aad")

    def test_dame_gender_name2gender_in_dataset(self):
        g = Gender()
        guess = g.name2gender_in_dataset("David",
                                         dataset='files/names/names_es')
        self.assertTrue(guess, 1)
        guess = g.name2gender_in_dataset("David",
                                         dataset='files/names/all.csv')
        self.assertTrue(guess, 1)
        guess = g.name2gender_in_dataset("David",
                                         dataset='files/names/yob2017.csv')
        self.assertTrue(guess, 1)
        guess = g.name2gender_in_dataset("Laura",
                                         dataset='files/names/names_es')
        self.assertTrue(guess, 0)
        guess = g.name2gender_in_dataset("Laura",
                                         dataset='files/names/all.csv')
        self.assertTrue(guess, 0)
        guess = g.name2gender_in_dataset("Laura",
                                         dataset='files/names/yob2017.csv')
        self.assertTrue(guess, 0)
        guess = g.name2gender_in_dataset("Teppei",
                                         dataset='files/names/yob2017.csv')
        self.assertTrue(guess, 2)
        guess = g.name2gender_in_dataset("Filka",
                                         dataset='files/names/nam_dict.txt')
        self.assertTrue(guess, 0)

    def test_dame_gender_guess(self):
        g = Gender()
        r = g.guess(name="David", binary=True, dataset="ine")
        self.assertEqual(r, 1)
        r = g.guess(name="Andrea", binary=True)
        self.assertEqual(r, 0)
        r = g.guess(name="David", binary=False)
        self.assertEqual(r, "male")
        r = g.guess(name="Laura", binary=True)
        self.assertEqual(r, 0)
        r = g.guess(name="Laura", binary=False)
        self.assertEqual(r, "female")
        r = g.guess(name="Andrea", binary=True)
        self.assertEqual(r, 0)

    def test_dame_gender_guess_surname(self):
        g = Gender()
        self.assertEqual(g.guess_surname("Smith", "us"), [True, 2376206])
        self.assertEqual(g.guess_surname("Serrano", "ar"), [True, 73])
        self.assertEqual(g.guess_surname("Serrano", "es"), [True, 131371])
        self.assertEqual(g.guess_surname("Arroyo", "ine"), [True, 39834])
        
    def test_dame_gender_string2gender(self):
        g = Gender()
        gender1 = g.string2gender("Arroyo Menéndez, David")
        gender2 = g.string2gender("xxxxx Laura")
        self.assertTrue(gender1, 'male')
        self.assertTrue(gender2, 'female')

    def test_dame_gender_csv2names(self):
        g = Gender()
        names = g.csv2names(path='files/names/partial.csv')
        self.assertTrue(len(names) > 10)
        names = g.csv2names(path='files/names/min.csv')
        l1 = ['Pierre', 'Raul', 'Adriano', 'Ralf', 'Guillermo', 'Sabina']
        self.assertEqual(l1, names)
        names = g.csv2names(path='files/names/min.csv', surnames=False)
        l2 = ['Pierre', 'Raul', 'Adriano', 'Ralf', 'Guillermo', 'Sabina']
        self.assertEqual(l2, names)
        names = g.csv2names(path='files/names/min.csv', surnames=True)
        l3 = [['Pierre', 'grivel'], ['Raul', 'serapioni'],
              ['Adriano', 'moura'], ['Ralf', 'kieser'],
              ['Guillermo', 'leon-de-la-barra'], ['Sabina', 'pannek']]
        self.assertEqual(l3, names)

    def test_dame_gender_csv2json(self):
        g = Gender()
        g.csv2json(path="files/names/min.csv")
        self.assertTrue(os.path.isfile("files/names/csv2json.json"))

    def test_dame_gender_json2gender_list(self):
        g = Gender()
        path = "files/names/partial.csv.json"
        gl = g.json2gender_list(jsonf=path, binary=True)
        l1 = [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        self.assertEqual(gl, l1)

    def test_dame_gender_guess_list(self):
        g = Gender()
        self.assertEqual(['male', 'male', 'male', 'male', 'male',
                          'male', 'female', 'female', 'male', 'male',
                          'male', 'male', 'male', 'male', 'male',
                          'male', 'male', 'male', 'female', 'male', 'male'],
                         g.guess_list(path="files/names/partial.csv",
                                      binary=False))
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                         g.guess_list(path="files/names/partial.csv",
                                      binary=True))
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                         g.guess_list(path="files/names/partial.csv",
                                      binary=True, dataset='inter'))

    def test_dame_gender_confusion_matrix_gender(self):
        g = Gender()
        cm = g.confusion_matrix_gender(path="files/names/min.csv")
        am = [[1, 0, 0], [0, 5, 0], [0, 5, 0]]
        self.assertEqual(cm, am)
        cm = g.confusion_matrix_gender(path="files/names/partial.csv")
        am = [[3, 0, 0], [0, 16, 0], [0, 16, 0]]
        self.assertEqual(cm, am)

    def test_dame_gender_csv2gender_list(self):
        g = Gender()
        gl = g.csv2gender_list(path="files/names/partial.csv")
        self.assertEqual(gl,
                         [1, 1, 1, 1, 2, 1, 0, 0, 1, 1,
                          2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(g.females, 3)
        self.assertEqual(g.males, 16)
        self.assertEqual(g.unknown, 2)

    def test_dame_gender_dataset2genderlist(self):
        g = Gender()
        path1 = "files/names/all.csv"
        gl = g.dataset2genderlist(dataset=path1)
        self.assertEqual(gl[0:4], [1, 1, 1, 1])

    def test_dame_gender_features_list(self):
        g = Gender()
        fl = g.features_list()
        self.assertTrue(len(fl) > 20)

    def test_dame_gender_inesurname_province_and_frec(self):
        g = Gender()
        frec1 = g.inesurname_province_and_frec("GIL", province='madrid')
        frec2 = g.inesurname_province_and_frec("GIL", province='alava')
        frec3 = g.inesurname_province_and_frec("GIL", province='bizkaia')
        frec4 = g.inesurname_province_and_frec("GIL", province='guipuzkoa')
        frec5 = g.inesurname_province_and_frec("GIL", province='navarra')
        self.assertEqual(frec1, 19961)
        self.assertEqual(frec2, 1003)
        self.assertEqual(frec3, 2829)
        self.assertEqual(frec4, 1389)
        self.assertEqual(frec5, 2462)
        frec1 = g.inesurname_province_and_frec("PÉREZ", province='madrid')
        frec2 = g.inesurname_province_and_frec("Pérez", province='alava')
        self.assertEqual(frec1, 95280)
        self.assertEqual(frec2, 4519)

    def test_dame_gender_name_frec(self):
        g = Gender()
        frec1 = g.name_frec("INES", dataset='ine')
        self.assertEqual(int(frec1['females']), 63378)
        self.assertEqual(int(frec1['males']), 0)
        frec2 = g.name_frec("BEATRIZ", dataset='ine')
        self.assertEqual(int(frec2['females']), 122917)
        frec3 = g.name_frec("ALMUDENA", dataset='ine')
        self.assertEqual(int(frec3['females']), 30517)
        frec5 = g.name_frec("ELIZABETH", dataset='us')
        self.assertEqual(int(frec5['females']), 1655053)
        frec5n = g.name_frec("ELISABETH", dataset='us')
        self.assertEqual(int(frec5n['females']), 46811)
        frec6 = g.name_frec("MARIA", dataset='gb')
        self.assertEqual(int(frec6['females']), 10401)
        frec7 = g.name_frec("JULIAN", dataset='gb')
        self.assertEqual(int(frec7['males']), 1713)
        frec8 = g.name_frec("A", dataset='gb')
        self.assertEqual(int(frec8['males']), 42)
        frec6 = g.name_frec("MARIA", dataset='nz')
        self.assertEqual(int(frec6['females']), 5541)
        frec6 = g.name_frec("MARIA", dataset='ca')
        self.assertEqual(int(frec6['females']), 1725)
        frec7 = g.name_frec("MARIA", dataset='si')
        self.assertEqual(int(frec7['females']), 2867)

    def test_dame_gender_name_frec_from_file(self):
        g = Gender()
        path = "files/names/names_at/atmales.csv"
        num = g.name_frec_from_file("David", path)
        self.assertEqual(num, '90451')

    def test_dame_gender_path_surname_dataset(self):
        dg = Gender()
        path = "files/names/names_be/besurnames.csv"
        self.assertEqual(dg.path_surname_dataset("be"), path)

    def test_dame_gender_name_prob_countries(self):
        g = Gender()
        self.assertEqual.__self__.maxDiff = None
        x = [{'females': {'es': 0.0, 'ie': 0.0, 'is': 0.0,
                          'uy': 0.0, 'gb': 0.0, 'us': 1.0,
                          'nz': 0.0, 'ca': 0.0, 'fi': 0.0,
                          'au': 0.0, 'pt': 0.0},
              'males': {'es': 0.09, 'ie': 0.0, 'is': 0.0,
                        'uy': 0.0, 'gb': 0.02, 'us': 0.88,
                        'nz': 0.01, 'ca': 0.0, 'fi': 0.0,
                        'au': 0.0, 'pt': 0.0}}]
        self.assertEqual(x, g.name_prob_countries("David"))
        y = [{'males':
              {'is': 0, 'ca': 0, 'fi': 0, 'au': 0,
               'pt': 0, 'ie': 0, 'gb': 0, 'nz': 0,
               'es': 0, 'uy': 0, 'us': 0},
              'females':
              {'is': 0.0, 'ca': 0.0, 'fi': 0.0,
               'au': 0.0, 'pt': 0.0, 'ie': 0.0,
               'gb': 0.0, 'nz': 0.0, 'es': 1.0,
               'uy': 0.0, 'us': 0.0}}]
        self.assertEqual(y, g.name_prob_countries("Nekane"))

#     def test_dame_gender_error_gender_bias(self):
#         g = Gender()
#         v1 = [0, 1, 1, 1]
#         v2 = [0, 0, 1, 1]
#         self.assertEqual(g.error_gender_bias(v1, v2), 0.25)

    def test_dame_gender_json2names(self):
        g = Gender()
        path = "files/names/namsorfiles_names_min.csv.json"
        j2n = g.json2names(jsonf=path)
        l1 = ["Pierre", "Raul", "Adriano", "Ralf", "Guillermo", "Sabina"]
        self.assertEqual(l1, j2n)
        j2ns = g.json2names(jsonf=path, surnames=True)
        l2 = [["Pierre", "grivel"], ["Raul", "serapioni"],
              ["Adriano", "moura"], ["Ralf", "kieser"],
              ["Guillermo", "leon-de-la-barra"], ["Sabina", "pannek"]]
        self.assertEqual(j2ns, l2)

    def test_dame_gender_check_names(self):
        g = Gender()
        path1 = "files/names/namsorfiles_names_min.csv.json"
        path2 = "files/names/min.csv"
        path3 = "files/names/partial.csv"
        path4 = "files/names/genderizefiles_names_min.csv.json"
        path5 = "files/names/genderizefiles_names_partial.csv.json"
        path6 = "files/names/nameapifiles_names_min.csv.json"
        path7 = "files/names/nameapifiles_names_partial.csv.json"
        self.assertTrue(g.json_eq_csv_in_names(jsonf=path1, path=path2))
        self.assertTrue(g.json_eq_csv_in_names(jsonf=path4, path=path2))
        self.assertTrue(g.json_eq_csv_in_names(jsonf=path5, path=path3))
        self.assertTrue(g.json_eq_csv_in_names(jsonf=path6, path=path2))
        self.assertTrue(g.json_eq_csv_in_names(jsonf=path7, path=path3))

    def test_dame_gender_first_uneq(self):
        g = Gender()
        path1 = "files/names/genderizefiles_names_min.csv.json"
        path2 = "files/names/min.csv"
        path3 = "files/names/nameapifiles_names_min.csv.json"
        path4 = "files/names/partial.csv"
        path5 = "files/names/genderizefiles_names_min.csv.json"
        sabina = g.first_uneq_json_and_csv_in_names(jsonf=path1, path=path2)[0]
        self.assertEqual("", sabina)
        five = g.first_uneq_json_and_csv_in_names(jsonf=path1, path=path2)[1]
        self.assertEqual(5, five)
        guille = g.first_uneq_json_and_csv_in_names(jsonf=path3, path=path4)[0]
        self.assertEqual("guillermo", guille)
        four = g.first_uneq_json_and_csv_in_names(jsonf=path3, path=path4)[1]
        self.assertEqual(4, four)
        guille2 = g.first_uneq_csv_and_csv_in_names(csv1=path2, csv2=path4)[0]
        self.assertEqual("guillermo", guille2)
        api = g.first_uneq_json_and_json_in_names(json1=path1, json2=path3)[0]
        self.assertEqual("", api)
        api2 = g.first_uneq_json_and_json_in_names(json1=path1, json2=path5)[0]
        self.assertEqual("", api2)
        
# THE NEXT TESTS HAS BEEN COMMENTED BY TIME REASONS EXECUTING TESTS
#     def test_dame_gender_features_list_categorical(self):
#         g = Gender()
#         flc = g.features_list_categorical('files/names/partial.csv')
#         self.assertEqual(len(flc[0]), 6)
#         self.assertEqual(flc[0], [112, 101, 0, 0, 1, 0])

#     def test_dame_gender_features_list_noundefined(self):
#         g = Gender()
#         flnu = g.features_list_no_undefined('files/names/allnoundefined.csv')
#         self.assertTrue(len(flnu) > 5000)

#     def test_dame_gender_features_list_no_categorical(self):
#         g = Gender()
#         flnc = g.features_list_no_categorical('files/names/partial.csv')
#         self.assertTrue(len(flnc[0]) > 25)
#         self.assertTrue(flnc[0], [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0,
#                                   0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3])

#     def test_dame_gender_features_list_no_letters(self):
#         g = Gender()
#         flnl = g.features_list_no_letters('files/names/partial.csv')
#         self.assertTrue(len(flnl[0]) > 5)
#         self.assertEqual(flnl[0], [112, 101, 3, 2, 0, 1, 1, 0, 0, 0])

#     def test_dame_gender_features_list2csv(self):
#         # TODO: You can write asserts to verify the first line
#         g = Gender()
#         csv1 = g.features_list2csv(path="files/names/min.csv")
#         csv2 = g.features_list2csv(path="files/names/min.csv",
#                                    categorical="categorical")
#         csv3 = g.features_list2csv(path="files/names/min.csv",
#                                    categorical="nocategorical")
#         csv4 = g.features_list2csv(path="files/names/allnoundefined.csv",
#                                    categorical="noundefined")
#         self.assertTrue(os.path.isfile("files/features_list.csv"))
#         file = open("files/features_list.csv", "r")
#         if (file):
#             self.assertTrue(
#                 os.path.isfile("files/features_list_cat.csv"))
#             self.assertTrue(
#                 os.path.isfile("files/features_list_no_cat.csv"))
#             self.assertTrue(
#                 os.path.isfile("files/features_list_no_undefined.csv"))
