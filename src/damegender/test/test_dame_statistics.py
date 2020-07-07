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

   # def test_dame_gender_inesurname_province_and_frec(self):
   #      ds = DameStatistics()
   #      frec1 = ds.inesurname_province_and_frec("GIL", province='madrid')
   #      frec2 = ds.inesurname_province_and_frec("GIL", province='alava')
   #      frec3 = ds.inesurname_province_and_frec("GIL", province='bizkaia')
   #      frec4 = ds.inesurname_province_and_frec("GIL", province='guipuzkoa')                
   #      frec5 = ds.inesurname_province_and_frec("GIL", province='navarra')

   #      self.assertEqual(frec1, 19961)
   #      self.assertEqual(frec2, 1003)
   #      self.assertEqual(frec3, 2829)
   #      self.assertEqual(frec4, 1389)
   #      self.assertEqual(frec5, 2462)                                
                
    def test_dame_statistics_error_gender_bias(self):
        ds = DameStatistics()
        v1 = [0, 1, 1, 1]
        v2 = [0, 0, 1, 1]
        self.assertEqual(ds.error_gender_bias(v1, v2), 0.25)

    # def test_dame_statistics_features_list(self):
    #     ds = DameStatistics()
    #     fl = ds.features_list()
    #     self.assertTrue(len(fl) > 20)
        
