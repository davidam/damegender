#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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
from app.dame_utils import DameUtils

class TddInPythonExample(unittest.TestCase):
    def test_split_method_returns_correct_result(self):
        u = DameUtils()
        x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        sp = u.split(x, 5)
        self.assertEqual(sp, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]])

    def test_drop_dots_method_returns_correct_result(self):
        u = DameUtils()
        self.assertEqual(1212, int(u.drop_dots(12.12)))

    def test_drop_accents_method_returns_correct_result(self):
        u = DameUtils()
        self.assertEqual("Ines", u.drop_accents("Inés"))

    def test_drop_white_space_method_returns_correct_result(self):
        u = DameUtils()
        self.assertEqual("In", u.drop_white_space("In "))
        self.assertEqual("Ines", u.drop_accents(u.drop_white_space("Inés ")))

    def test_drop_quotes_method_returns_correct_result(self):
        u = DameUtils()
        self.assertEqual('Hola Mexico', u.drop_quotes('Hola "Mexico'))
        self.assertEqual("Hola Mexico", u.drop_quotes("Hola' 'Mexico"))

    def test_dame_utils_delete_duplicated_method_returns_correct_result(self):
        du = DameUtils()
        self.assertEqual(du.delete_duplicated([1, 2, 2, 1, 3]), [1, 2, 3])

    def test_dame_utils_clean_list_method_returns_correct_result(self):
        du = DameUtils()
        self.assertEqual(du.clean_list(['', 'H. Peter Anvin', 'hiranotaka@zng.info', 'Ram Yalamanchili', 'Ferenc Wagner']), ['H. Peter Anvin', 'Ram Yalamanchili', 'Ferenc Wagner'])
