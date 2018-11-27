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
from app.gender import Gender

class TddInPythonExample(unittest.TestCase):

    def test_gender_guess_method_returns_correct_result(self):
        g = Gender()
        r = Gender.guess(self, name="David", binary=True)
        self.assertEqual(r, 1)
        r = Gender.guess(self, name="David", binary=False)
        self.assertEqual(r, "male")
        r = Gender.guess(self, name="Laura", binary=True)
        self.assertEqual(r, 0)
        r = Gender.guess(self, name="Laura", binary=False)
        self.assertEqual(r, "female")
        r = Gender.guess(self, name="Andrea", binary=True)
        self.assertEqual(r, 2)

    def test_sexmachine_gender_list_method_returns_correct_result(self):
        g = Gender()
        gl = g.gender_list()
        self.assertEqual(gl, [1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(g.females, 3)
        self.assertEqual(g.males, 16)
        self.assertEqual(g.unknown, 2)
