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
from app.sexmachine import Sexmachine

class TddInPythonExample(unittest.TestCase):

    def test_sexmachine_features_method_returns_correct_result(self):
        s = Sexmachine()
        f = s.features("David")
        self.assertEqual(f['has(a)'], True)
        self.assertEqual(f['count(i)'], 1)
        self.assertEqual(f['count(v)'], 1)
        self.assertEqual(f['last_letter'], 'd')
        self.assertEqual(f['first_letter'], 'd')

    def test_sexmachine_listfeatures_method_returns_correct_result(self):
        s = Sexmachine()
        f = s.featuresint("David")
        self.assertTrue(len(f) > 0)

    def test_sexmachine_guess_method_returns_correct_result(self):
        s = Sexmachine()
        self.assertEqual(s.guess("David"), 'male')

    def test_sexmachine_list_method_returns_correct_result(self):
        s = Sexmachine()
        self.assertEqual([('"pierre"', 'male'), ('"raul"', 'male'), ('"adriano"', 'female'), ('"ralf"', 'male'), ('"teppei"', 'male'), ('"guillermo"', 'male'), ('"catherine"', 'female'), ('"sabina"', 'female'), ('"ralf"', 'male'), ('"karl"', 'female'), ('"sushil"', 'male'), ('"clemens"', 'male'), ('"gregory"', 'male'), ('"lester"', 'male'), ('"claude"', 'male'), ('"martin"', 'female'), ('"vlad"', 'male'), ('"pasquale"', 'male'), ('"lourdes"', 'male'), ('"bruno"', 'male'), ('"thomas"', 'male')], s.list())

    def test_sexmachine_featuresint_method_returns_correct_result(self):
        s = Sexmachine()
        dicc = s.featuresint("David")
        self.assertEqual(chr(dicc['last_letter']), 'd')
        self.assertEqual(chr(dicc['first_letter']), 'd')
        self.assertEqual(dicc['count(a)'], 1)
        self.assertEqual(dicc['count(b)'], 0)
        self.assertEqual(dicc['count(c)'], 0)
        self.assertEqual(dicc['count(d)'], 2)
        self.assertEqual(dicc['count(e)'], 0)
        self.assertEqual(dicc['count(f)'], 0)
        self.assertEqual(dicc['count(h)'], 0)
        self.assertEqual(dicc['count(i)'], 1)
        self.assertEqual(dicc['count(v)'], 1)
        self.assertTrue(dicc['count(a)'] > 0)
        self.assertTrue(dicc['vocals'], 2)
        self.assertTrue(dicc['consonants'], 3)
        self.assertEqual(dicc['first_letter_vocal'], 0)
        self.assertEqual(dicc['last_letter_vocal'], 0)
        self.assertEqual(len(dicc.values()), 32)

    def test_sexmachine_featuresList_method_returns_correct_result(self):
        s = Sexmachine()
        fl = s.featuresList()
        self.assertTrue(len(fl) > 20)
