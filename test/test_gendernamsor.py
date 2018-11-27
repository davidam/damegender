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
from app.gendernamsor import Gendernamsor
from app.gender import Gender

class TddInPythonExample(unittest.TestCase):


    def test_gender_namsor_init_method_returns_correct_result(self):
        g = Gendernamsor()
        self.assertEqual(g.males, 0)
        self.assertEqual(g.females, 0)
        self.assertEqual(g.unknown, 0)

    def test_gender_namsor_gender_guess_method_returns_correct_result(self):
        g = Gendernamsor()
        self.assertEqual(1, g.guess("David", "Arroyo", binary=True))
        self.assertEqual(0, g.guess("Andrea", "Arroyo", binary=True))
        self.assertEqual(0, g.guess("Asdf", "qwer", binary=True))
