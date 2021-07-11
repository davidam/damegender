#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


import unittest
import os
from app.dame_nltk import DameNLTK


class TddInPythonExample(unittest.TestCase):

    def test_sentence_similarity(self):
        dn = DameNLTK()
        good = "This is a good sentence"
        bad = "This is a bad sentence"
        similar = dn.sentence_similarity(good.split(), bad.split())
        self.assertTrue(similar > 0.7)
