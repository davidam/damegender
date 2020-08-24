#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import unittest
import os
from app.dame_nltk import DameNLTK

class TddInPythonExample(unittest.TestCase):

        def test_sentence_similarity(self):
            dn = DameNLTK()
            self.assertTrue(dn.sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split()) > 0.7)
