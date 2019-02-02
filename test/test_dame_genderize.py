#!/usr/bin/python
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
from app.dame_genderize import DameGenderize

class TddInPythonExample(unittest.TestCase):

    def test_dame_genderize_guess_method_returns_correct_result(self):
        gg = DameGenderize()
        self.assertEqual(gg.guess("David"), "male")
        self.assertEqual(gg.guess("David", binary=True), 1)

    def test_dame_genderize_guess_file_method_returns_correct_result(self):
        gg = DameGenderize()
        self.assertEqual(gg.guess("David", binary=True), 1)

    def test_dame_genderize_gender_list_method_returns_correct_result(self):
        gg = DameGenderize()
        gl = gg.gender_list()
        self.assertEqual(gl, [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(gg.females, 3)
        self.assertEqual(gg.males, 16)
        self.assertEqual(gg.unknown, 2)

    def test_dame_genderize_guess_list_method_returns_correct_result(self):
        gg = DameGenderize()
        self.assertEqual(['male', 'male', 'male', 'male', 'unknown', 'male', 'female', 'female', 'male', 'male'], gg.guess_list(path="files/partial.csv", binary=False)[0:10])
        self.assertEqual([1, 1, 1, 1, 2, 1, 0, 0, 1, 1], gg.guess_list(path="files/partial.csv",binary=True)[0:10])

    def test_dame_genderize_guess_list_method_returns_correct_result(self):
        gg = DameGenderize()
        self.assertEqual(['male', 'male', 'male', 'male', 'unknown', 'male', 'female', 'female', 'male', 'male'], gg.guess_list(path="files/partial.csv", binary=False)[0:10])
        self.assertEqual([1, 1, 1, 1, 2, 1, 0, 0, 1, 1], gg.guess_list(path="files/partial.csv",binary=True)[0:10])



    # def test_dame_genderize_confusion_matrix_dame_method_returns_correct_result(self):
    #     g = DameGenderize()
    #     cm = g.confusion_matrix_dame(path="files/min.csv")
    #     am = [[5, 0, 0], [0, 2, 0]]
    #     self.assertEqual(cm,am)
