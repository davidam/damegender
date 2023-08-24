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
from app.dame_brazilapi import DameBrazilApi
from app.dame_utils import DameUtils
import collections
collections.Callable = collections.abc.Callable


class TddInPythonExample(unittest.TestCase):

    def test_dame_brazilapi_get(self):
        dba = DameBrazilApi()
        try:
            v0 = dba.get("Ana")
            v1 = dba.get("Jose")
            self.assertTrue(v0['females'] > 70000)
            self.assertTrue(v0['males'] < 11000)
            self.assertTrue(v1['males'] > 70000)
            self.assertTrue(v1['females'] < 30000)
        except requests.exceptions.Timeout:
            self.assertTrue(True)

    # def test_dame_brazilapi_download(self):
    #     dba = DameBrazilApi()
    #     du = DameUtils()
    #     path1 = "files/names/min.csv"
    #     try:
    #         g = dba.download(path1)
    #         self.assertTrue(
    #             os.path.isfile(
    #                 "files/tmp/brazilnames.json"))
    #     except requests.exceptions.Timeout:
    #         self.assertTrue(True)

    def test_dame_brazilapi_download_csv(self):
        dba = DameBrazilApi()
        du = DameUtils()
        path1 = "files/names/min.csv"
        try:
            g = dba.download_csv(path1)
            text2 = dba.download_csv(path=path1,
                                     name_position=0,
                                     backup_all="files/tmp/brazilnames.csv")
            self.assertTrue(
                os.path.isfile(
                    "files/tmp/brazilnames.csv"))
        except requests.exceptions.Timeout:
            self.assertTrue(True)
