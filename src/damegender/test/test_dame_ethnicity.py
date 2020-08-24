#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

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
        self.assertEqual(de.inesurname2ethnicity(surname="KHAN", locale="af"), ["af"])

    def test_dame_locale_match(self):
        de = DameEthnicity()
        self.assertEqual(de.locale_match(surname="KHAN", path='files/inesurnames/apellidos-afganistan.xls.csv', locale="af"), "af")
