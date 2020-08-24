#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

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
