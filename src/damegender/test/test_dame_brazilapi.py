#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022  David Arroyo Menéndez (davidam@gmail.com)
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
import os
import requests
import json
from pprint import pprint
from app.dame_brazilapi import DameBrazilApi
from app.dame_utils import DameUtils
import collections
collections.Callable = collections.abc.Callable

class TddInPythonExample(unittest.TestCase):

    def test_dame_brazilapi_get(self):
        dba = DameBrazilApi()
        v = dba.get("Ana")
        self.assertTrue(v['female'] > 70000)
        self.assertTrue(v['male'] < 11000)        
        v = dba.get("Jose")
        self.assertTrue(v['male'] > 70000)
        self.assertTrue(v['female'] < 30000)        

    def test_dame_brazilapi_download(self):
        dba = DameBrazilApi()
        du = DameUtils()
        path1 = "files/names/min.csv"
        g = dba.download(path1)
        self.assertTrue(
            os.path.isfile(
                "files/names/brazilnames.json"))
        
