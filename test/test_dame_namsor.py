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
from app.dame_namsor import DameNamsor
from app.dame_gender import Gender

class TddInPythonExample(unittest.TestCase):


    def test_dame_namsor_init_method_returns_correct_result(self):
        g = DameNamsor()
        self.assertEqual(g.males, 0)
        self.assertEqual(g.females, 0)
        self.assertEqual(g.unknown, 0)

    def test_dame_namsor_gender_guess_method_returns_correct_result(self):
        g = DameNamsor()
        self.assertEqual(1, g.guess("David", "Arroyo", binary=True))
        self.assertEqual(0, g.guess("Andrea", "Arroyo", binary=True))
        self.assertEqual(0, g.guess("Asdf", "qwer", binary=True))

    def test_dame_namsor_gender_list_method_returns_correct_result(self):
        g = DameNamsor()
        gl = g.gender_list()
        self.assertEqual(gl, [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(g.females, 3)
        self.assertEqual(g.males, 16)
        self.assertEqual(g.unknown, 2)

    def test_dame_namsor_features_list_method_returns_correct_result(self):
        g = DameNamsor()
        fl = g.features_list()
        self.assertTrue(len(fl) > 20)

    def test_dame_namsor_guess_list_method_returns_correct_result(self):
        g = Gender()
        self.assertEqual(['unknown', 'male', 'male', 'male', 'unknown', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'male', 'unknown', 'male', 'male', 'male', 'female', 'male', 'unknown'], g.guess_list(path="files/partial.csv", binary=False))
        self.assertEqual([2, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2], g.guess_list(path="files/partial.csv",binary=True))


    # def test_dame_namsor_accuracy_method_returns_correct_result(self):
    #     g = DameNamsor()
    #     self.assertTrue(g.accuracy(path="files/partial.csv") >= 0.5)

    def test_dame_gender_accuracy_score_dame_method_returns_correct_result(self):
       g = Gender()
       score1 = g.accuracy_score_dame([1, 1], [1, 1])
       self.assertEqual(score1, 1)
       score2 = g.accuracy_score_dame([1, 1, 1, 0], [1, 1, 2, 0])
       self.assertEqual(score2, 0.75)
       score3 = g.accuracy_score_dame([1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1])
       self.assertEqual(score3, 1)


    # def test_namsor_accuracy_method_returns_correct_result(self):
    #     s = DameNamsor()
    #     self.assertTrue(s.accuracy() > 0.5)
