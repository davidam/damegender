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
import os
import requests
import json
import collections
collections.Callable = collections.abc.Callable

from app.dame_genderapi import DameGenderApi
from app.dame_utils import DameUtils


class TddInPythonExample(unittest.TestCase):

    def test_dame_genderapi_get(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            v = dga.get("Diana")
            self.assertEqual(v[0], "female")
            self.assertTrue(v[1] > 90)
            self.assertTrue(v[2] > 50000)
            self.assertEqual(len(v), 3)

    def test_dame_genderapi_guess(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            g = dga.guess("Sara", binary=False)
            self.assertEqual(g, "female")
            g = dga.guess("Paula", binary=False)
            self.assertEqual(g, "female")
            g = dga.guess("Sara", binary=True)
            self.assertEqual(g, 0)

    def test_dame_genderapi_download(self):
        dga = DameGenderApi()
        du = DameUtils()
        path1 = "files/names/min.csv"
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            g = dga.download(path1)
            self.assertTrue(
                os.path.isfile(
                    "files/names/genderapi"+du.path2file(path1)+".json"))

    def test_dame_genderapi_accuracy(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            acc = dga.accuracy("Diana")
            self.assertTrue(acc > 90)

    def test_dame_genderapi_guess_list(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            l1 = ['male', 'male', 'male', 'male', 'male', 'female']
            self.assertEqual(l1,
                             dga.guess_list(path="files/names/min.csv",
                                            binary=False))
            l2 = [1, 1, 1, 1, 1, 0]
            self.assertEqual(l2,
                             dga.guess_list(path="files/names/min.csv",
                                            binary=True))

    def test_dame_genderapi_confusion_matrix_gender(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            cm = dga.confusion_matrix_gender(path="files/names/min.csv")
            am = [[1, 0, 0], [0, 5, 0], [0, 5, 0]]
            self.assertEqual(cm, am)

    def test_dame_gender_check_names(self):
        g = DameGenderApi()
        jsonf = "files/names/genderapifiles_names_min.csv.json"
        b = g.json_eq_csv_in_names(jsonf=jsonf,
                                   path="files/names/min.csv")
        self.assertTrue(b)

    def test_dame_genderapi_json2gender_list(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            l1 = ['male', 'male', 'male', 'male', 'male', 'female']
            l2 = [1, 1, 1, 1, 1, 0]
            jsonf = "files/names/genderapifiles_names_min.csv.json"
            self.assertEqual(l1, dga.json2gender_list(jsonf=jsonf))
            self.assertEqual(l2, dga.json2gender_list(jsonf=jsonf,
                                                      binary=True))
