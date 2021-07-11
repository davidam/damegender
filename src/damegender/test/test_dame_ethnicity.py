#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


import unittest
import numpy as np
import os
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
