#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

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
        self.assertEqual(ds.count_true2guess(v1, v2, 0, 0), 2)  # femalefemale
        self.assertEqual(ds.femalefemale(v1, v2), 2)
        self.assertEqual(ds.count_true2guess(v1, v2, 1, 1), 2)  # malemale
        self.assertEqual(ds.malemale(v1, v2), 2)
        self.assertEqual(ds.count_true2guess(v1, v2, 0, 1), 1)  # femalemale
        self.assertEqual(ds.femalemale(v1, v2), 1)
        self.assertEqual(ds.count_true2guess(v1, v2, 1, 0), 1)  # malefemale
        self.assertEqual(ds.malefemale(v1, v2), 1)
        vv1 = [1, 0, 1, 1, 1]
        vv2 = [1, 1, 1, 0]
        self.assertEqual(ds.count_true2guess(vv2, vv1, 1, 1), 2)  # malemale
        self.assertEqual(ds.count_true2guess(vv2, vv1, 0, 1), 1)  # femalemale
        self.assertEqual(ds.count_true2guess(vv2, vv1, 1, 0), 1)  # malefemale
        vvv1 = [1, 0, 2, 2, 1]
        vvv2 = [2, 0, 1, 2, 1]
        t2g = ds.count_true2guess(vvv2, vvv1, 2, 2)  # undefinedundefined
        self.assertEqual(t2g, 1)
        uu = ds.undefinedundefined(vvv2, vvv1)
        self.assertEqual(uu, 1)
        t2g = ds.count_true2guess(vvv2, vvv1, 2, 1)
        self.assertEqual(t2g, 1)  # undefinedmale

    def test_dame_statistics_error_coded(self):
        ds = DameStatistics()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(ds.error_coded(v1, v2), 0.5)

    def test_dame_statistics_error_coded_without_na(self):
        ds = DameStatistics()
        v1 = [1, 0, 1, 1]
        v2 = [1, 1, 1, 0]
        self.assertEqual(ds.error_coded_without_na(v1, v2), 0.5)

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

    def test_dame_statistics_accuracy_score_dame(self):
        ds = DameStatistics()
        score1 = ds.accuracy_score_dame([1, 1], [1, 1])
        self.assertEqual(score1, 1)
        score2 = ds.accuracy_score_dame([1, 1, 1, 0],
                                        [1, 1, 2, 0])
        self.assertEqual(score2, 0.75)
        score3 = ds.accuracy_score_dame([1, 1, 1, 1, 2, 1],
                                        [1, 1, 1, 1, 2, 1])
        self.assertEqual(score3, 1)
        score4 = ds.accuracy_score_dame([1, 1, 1, 1, 2, 1, 0,
                                         0, 1, 1, 2, 1, 1, 1,
                                         1, 1, 1, 1, 0, 1, 1],
                                        [1, 1, 1, 1, 2, 1, 0,
                                         0, 1, 1, 2, 1, 1, 1,
                                         1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(score4, 1)

    def test_dame_gender_precision(self):
        ds = DameStatistics()
        score1 = ds.precision([1, 1], [1, 1])
        self.assertEqual(score1, 1)
        score2 = ds.precision([1, 1, 1, 0], [1, 1, 2, 0])
        self.assertEqual(score2, 1)
        score3 = ds.precision([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1])
        self.assertEqual(score3, 1)
        l1 = [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        l2 = [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        score4 = ds.precision(l1, l2)
        self.assertEqual(score4, 1)

    def test_dame_gender_recall(self):
        ds = DameStatistics()
        score1 = ds.recall([1, 1], [1, 1])
        self.assertEqual(score1, 1)
        score2 = ds.recall([1, 1, 1, 0], [1, 1, 2, 0])
        self.assertEqual(score2, 0.75)
        score3 = ds.recall([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1])
        self.assertEqual(score3, 1)
        l1 = [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        l2 = [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        score4 = ds.recall(l1, l2)
        self.assertEqual(score4, 1)
