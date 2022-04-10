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
import collections
collections.Callable = collections.abc.Callable

from app.dame_genderguesser import DameGenderGuesser
from app.dame_statistics import DameStatistics


class TddInPythonExample(unittest.TestCase):

    def test_genderguesser_list(self):
        dgg = DameGenderGuesser()
        g1 = dgg.guess("Sara", binary=False)
        self.assertEqual(g1, "female")
        g2 = dgg.guess("Sara", binary=True)
        self.assertEqual(g2, 0)
        g3 = dgg.guess("Laura", binary=False)
        self.assertEqual(g3, "female")
        g4 = dgg.guess("Laura", binary=True)
        self.assertEqual(g4, 0)

    def test_dame_genderguesser_gender_list(self):
        dgg = DameGenderGuesser()
        gl = dgg.csv2gender_list(path="files/names/partial.csv")
        self.assertEqual(gl, [1, 1, 1, 1, 2, 1, 0, 0, 1, 1,
                              2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(dgg.females, 3)
        self.assertEqual(dgg.males, 16)
        self.assertEqual(dgg.unknown, 2)

    def test_dame_genderguesser_guess_list(self):
        dgg = DameGenderGuesser()
        self.assertEqual(['male', 'male', 'male', 'male', 'male',
                          'male', 'female', 'female', 'male', 'male'],
                         dgg.guess_list(path="files/names/partial.csv",
                                        binary=False)[0:10])
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                         dgg.guess_list(path="files/names/partial.csv",
                                        binary=True)[0:10])

    def test_dame_genderguesser_accuracy(self):
        dgg = DameGenderGuesser()
        ds = DameStatistics()
        gl1 = dgg.csv2gender_list(path="files/names/partial.csv")
        gl2 = dgg.guess_list(path="files/names/partial.csv",
                             binary=True)
        self.assertTrue(ds.accuracy_score_dame(gl1, gl2) >= 0.5)
#        self.assertTrue(ds.accuracy(path="files/names/partial.csv") >= 0.5)
