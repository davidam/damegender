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
import os
from app.dame_utils import DameUtils
from app.dame_statistics import DameStatistics
from app.dame_namsor import DameNamsor
from app.dame_gender import Gender


class TddInPythonExample(unittest.TestCase):

    def test_dame_namsor_init(self):
        g = DameNamsor()
        self.assertEqual(g.males, 0)
        self.assertEqual(g.females, 0)
        self.assertEqual(g.unknown, 0)

    def test_dame_namsor_get(self):
        dn = DameNamsor()
        if (dn.config['DEFAULT']['namsor'] == 'yes'):
            l1 = dn.get("David", "Arroyo", binary=False)
            self.assertEqual(['male', -1.0], [l1[0], round(l1[1])])
            l2 = dn.get("David", "Arroyo", binary=True)
            self.assertEqual(['male', -1.0], [l2[0], round(l2[1])])
            l3 = dn.get("Karen", "Arroyo", binary=True)
            self.assertEqual(['female', 1.0], [l3[0], round(l3[1])])

    def test_dame_namsor_getGeo(self):
        dn = DameNamsor()
        if (dn.config['DEFAULT']['namsor'] == 'yes'):
            l1 = dn.get("David", "Arroyo", binary=False)
            self.assertEqual(['male', -1.0], [l1[0], round(l1[1])])


    def test_dame_namsor_scale(self):
        dn = DameNamsor()
        if (dn.config['DEFAULT']['namsor'] == 'yes'):
            self.assertEqual(-1.0, round(dn.scale("David", "Arroyo")))

    def test_dame_namsor_gender_guess(self):
        dn = DameNamsor()
        if (dn.config['DEFAULT']['namsor'] == 'yes'):
            self.assertEqual(1, dn.guess("David", "Arroyo", binary=True))
            self.assertEqual(0, dn.guess("Andrea", "Arroyo", binary=True))
            self.assertEqual(1, dn.guess("Asdf", "qwer", binary=True))

    def test_dame_namsor_gender_list(self):
        dn = DameNamsor()
        gl = dn.gender_list(path="files/names/partial.csv")
        self.assertEqual(gl,
                         [1, 1, 1, 1, 2, 1, 0, 0, 1, 1,
                          2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(dn.females, 3)
        self.assertEqual(dn.males, 16)
        self.assertEqual(dn.unknown, 2)

    def test_dame_namsor_features_list(self):
        dn = DameNamsor()
        fl = dn.features_list()
        self.assertTrue(len(fl) > 20)

    def test_dame_namsor_guess_list(self):
        dn = DameNamsor()
        if (dn.config['DEFAULT']['namsor'] == 'yes'):
            self.assertEqual(['male', 'male', 'male', 'male', 'male', 'male',
                          'female', 'female', 'male', 'male', 'male',
                          'male', 'male', 'male', 'male', 'male', 'male',
                          'male', 'female', 'male', 'male'],
                             dn.guess_list(path="files/names/partial.csv",
                                      binary=False))
            self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0,
                              1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 0, 1, 1],
                             dn.guess_list(path="files/names/partial.csv",
                                      binary=True))

    def test_dame_namsor_accuracy_score_dame(self):
        dn = DameNamsor()
        ds = DameStatistics()
        if (dn.config['DEFAULT']['namsor'] == 'yes'):        
            gl1 = dn.gender_list(path="files/names/partial.csv")
            gl2 = dn.guess_list(path="files/names/partial.csv",
                             binary=True)
            score1 = ds.accuracy_score_dame(gl1, gl2)
            self.assertEqual(score1, 1)


    def test_dame_namsor_download(self):
        dn = DameNamsor()
        du = DameUtils()
        path1 = "files/names/min.csv"
        if (dn.config['DEFAULT']['namsor'] == 'yes'):
            g = dn.download(path1)
            self.assertTrue(
                os.path.isfile(
                    "files/names/namsor"+du.path2file(path1)+".json"))

    def test_dame_namsor_json2guess_list(self):
        dn = DameNamsor()
        j2gl = dn.json2guess_list(jsonf="files/names/namsorfiles_names_min.csv.json", binary=False)
        self.assertEqual(['male', 'male', 'male', 'male', 'male', 'female'], j2gl)
        j2gl = dn.json2guess_list(jsonf="files/names/namsorfiles_names_min.csv.json", binary=True)
        self.assertEqual([1, 1, 1, 1, 1, 0], j2gl)

    def test_dame_namsor_json2names(self):
        dn = DameNamsor()
        l = dn.json2names(jsonf="files/names/namsorfiles_names_min.csv.json")
        self.assertEqual(['Pierre', 'Raul', 'Adriano', 'Ralf',
                          'Guillermo', 'Sabina'], l)
