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
from googleapiclient.discovery import build
from app.dame_gender import Gender
from app.dame_customsearch import DameCustomsearch
from app.dame_customsearch import DameCustomsearch


class TddInPythonExample(unittest.TestCase):

    def test_dame_customsearch_method_returns_correct_result(self):
        dc = DameCustomsearch()
        if (dc.config['DEFAULT']['customsearch'] == 'yes'):
            self.assertEqual(1, dc.guess("David", binary=True))
