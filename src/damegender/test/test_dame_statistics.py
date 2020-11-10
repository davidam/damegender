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
import numpy as np
import os
from app.dame_gender import Gender
from app.dame_statistics import DameStatistics

class TddInPythonExample(unittest.TestCase):

    def test_dame_statistics_count_true2guess(self):
        ds = DameStatistics()
        v1 = [1, 0, 1, 1, 0, 0]
        v2 = [1, 1, 1, 0, 0, 0]
        self.assertEqual(ds.count_true2guess(v1, v2, 0, 0), 2) # femalefemale
        self.assertEqual(ds.femalefemale(v1, v2), 2)
        self.assertEqual(ds.count_true2guess(v1, v2, 1, 1), 2) # malemale
        self.assertEqual(ds.malemale(v1, v2), 2)
        self.assertEqual(ds.count_true2guess(v1, v2, 0, 1), 1) # femalemale
        self.assertEqual(ds.femalemale(v1, v2), 1)
        self.assertEqual(ds.count_true2guess(v1, v2, 1, 0), 1) # malefemale
        self.assertEqual(ds.malefemale(v1, v2), 1)
        vv1 = [1, 0, 1, 1, 1]
        vv2 = [1, 1, 1, 0]
        self.assertEqual(ds.count_true2guess(vv2, vv1, 1, 1), 2)  # malemale
        self.assertEqual(ds.count_true2guess(vv2, vv1, 0, 1), 1)  # femalemale
        self.assertEqual(ds.count_true2guess(vv2, vv1, 1, 0), 1)  # malefemale
        vvv1 = [1, 0, 2, 2, 1]
        vvv2 = [2, 0, 1, 2, 1]
        self.assertEqual(ds.count_true2guess(vvv2, vvv1, 2, 2), 1)  # undefinedundefined
        self.assertEqual(ds.undefinedundefined(vvv2, vvv1), 1)
        self.assertEqual(ds.count_true2guess(vvv2, vvv1, 2, 1), 1)  # undefinedmale


    def test_dame_statistics_error_coded(self):
        ds = DameStatistics()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(ds.error_coded(v1, v2), 0.5)

    def test_dame_statistics_error_coded_without_na(self):
        ds = DameStatistics()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(ds.error_coded(v1, v2), 0.5)

    def test_dame_statistics_error_coded_without_na(self):
        ds = DameStatistics()
        v1 = [1, 0, 1, 1, 1]
        v2 = [1, 1, 1, 0, 1]
        self.assertEqual(ds.error_coded(v1, v2), 0.4)

    def test_dame_statistics_na_coded(self):
        ds = DameStatistics()
        v1 = [0, 1, 1, 1]
        v2 = [2, 0, 1, 1]
        self.assertEqual(ds.na_coded(v1, v2), 0.25)
                
    def test_dame_statistics_error_gender_bias(self):
        ds = DameStatistics()
        v1 = [0, 1, 1, 1]
        v2 = [0, 0, 1, 1]
        self.assertEqual(ds.error_gender_bias(v1, v2), 0.25)

