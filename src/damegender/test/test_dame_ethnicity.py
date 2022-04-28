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
import numpy as np
import os
import collections
collections.Callable = collections.abc.Callable

from app.dame_ethnicity import DameEthnicity


class TddInPythonExample(unittest.TestCase):

    def test_dame_ethnicity_surname2ethnicity(self):
        de = DameEthnicity()
        surname = "Smith".upper()
        dicc = de.surname2ethnicity(surname)
        self.assertEqual(dicc["white"], "73.35")
        self.assertEqual(dicc["black"], "22.22")
        self.assertEqual(dicc["api"], "0.40")
        self.assertEqual(dicc["aian"], "0.85")
        self.assertEqual(dicc["doublerace"], "1.63")
        self.assertEqual(dicc["hispanic"], "1.56")
        dicc2 = de.surname2ethnicity("JAURENA")
        self.assertFalse(dicc2)

    def test_dame_ethnicity_inesurname2ethnicity(self):
        de = DameEthnicity()
        l1 = de.inesurname2ethnicity(surname="KHAN", locale="af")
        self.assertEqual(l1, ["af"])

    def test_dame_locale_match(self):
        de = DameEthnicity()
        path = 'files/inesurnames/apellidos-afganistan.xls.csv'
        str1 = de.locale_match(surname="KHAN", path=path, locale="af")
        self.assertEqual(str1, "af")

    def test_dame_ethnicity_iso3166_to_eng(self):
        de = DameEthnicity()
        string0 = de.iso3166_to_eng("zw")
        self.assertEqual(string0, "Zimbabwe")

    def test_dame_ethnicity_dicc_iso639_2(self):
        de = DameEthnicity()
        dicc0 = de.dicc_iso639_2()
        self.assertEqual(dicc0["baq"][0], "Basque")
