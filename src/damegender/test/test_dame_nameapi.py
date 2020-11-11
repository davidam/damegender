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


import unittest

from app.dame_gender import Gender
from app.dame_nameapi import DameNameapi


class TddInPythonExample(unittest.TestCase):

    def test_dame_nameapi_init_method_returns_correct_result(self):
        g = DameNameapi()
        self.assertEqual(g.males, 0)
        self.assertEqual(g.females, 0)
        self.assertEqual(g.unknown, 0)

    def test_dame_nameapi_gender_guess_method_returns_correct_result(self):
        g = DameNameapi()
        if (g.config['DEFAULT']['nameapi'] == 'yes'):
            self.assertEqual(1, g.guess("David", "Arroyo", binary=True))
            self.assertEqual(0, g.guess("Andrea", "Arroyo", binary=True))

    def test_dame_nameapi_gender_prob_method_returns_correct_result(self):
        g = DameNameapi()
        if (g.config['DEFAULT']['nameapi'] == 'yes'):
            self.assertTrue(0.8 < g.confidence("David", "Arroyo", binary=True))

    def test_dame_nameapi_gender_list_method_returns_correct_result(self):
        g = DameNameapi()
        gl = g.gender_list(path="files/names/partial.csv")
        if (g.config['DEFAULT']['nameapi'] == 'yes'):
            self.assertEqual(gl,
                             [1, 1, 1, 1, 2, 1, 0, 0, 1, 1,
                              2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
            self.assertEqual(len(gl), 21)
            self.assertEqual(g.females, 3)
            self.assertEqual(g.males, 16)
            self.assertEqual(g.unknown, 2)

    def test_dame_nameapi_features_list_method_returns_correct_result(self):
        g = DameNameapi()
        fl = g.features_list()
        self.assertTrue(len(fl) > 20)

    def test_dame_nameapi_guess_list_method_returns_correct_result(self):
        dna = DameNameapi()
        if (dna.config['DEFAULT']['nameapi'] == 'yes'):
            jsonf1 = 'files/names/nameapifiles_names_partial.csv.json'
            l = dna.json2guess_list(jsonf1, binary=True)
            self.assertEqual(l, [1, 1, 1, 1, 1, 1, 0, 0, 1,
                              1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 1])


    def test_dame_nameapi_confusion_matrix_net_returns_correct_result(self):
        dna = DameNameapi()
        jsonf = 'files/names/nameapifiles_names_partial.csv.json'
        if (dna.config['DEFAULT']['nameapi'] == 'yes'):
            cm = dna.confusion_matrix_gender(path="files/names/partial.csv",
                                             dimensions="2x3",
                                             jsonf=jsonf)
            self.assertEqual([[3, 0, 0], [0, 15, 1]],
                             cm)

    def test_dame_nameapi_confusion_matrix_json_returns_correct_result(self):
        dna = DameNameapi()
        jsonf = 'files/names/nameapifiles_names_min.csv.json'
        if (dna.config['DEFAULT']['nameapi'] == 'yes'):
            cm = dna.confusion_matrix_gender(path="files/names/min.csv",
                                             dimensions="2x3",
                                             jsonf=jsonf)
            self.assertEqual([[1, 0, 0], [0, 5, 0]],
                             cm)


    def test_dame_nameapi_json2names(self):
        dn = DameNameapi()
        l = dn.json2names(jsonf="files/names/nameapifiles_names_min.csv.json")
        self.assertEqual(['Pierre', 'Raul', 'Adriano', 'Ralf', 'Guillermo', 'Sabina'], l)


    def test_dame_nameapi_json2guess_list(self):
        dn = DameNameapi()
        j2gl = dn.json2guess_list(jsonf="files/names/namsorfiles_names_min.csv.json", binary=False)
        self.assertEqual(['male', 'male', 'male', 'male', 'male', 'female'], j2gl)
        j2gl = dn.json2guess_list(jsonf="files/names/namsorfiles_names_min.csv.json", binary=True)
        self.assertEqual([1, 1, 1, 1, 1, 0], j2gl)
