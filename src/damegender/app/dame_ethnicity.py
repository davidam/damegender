#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv
from app.dame_utils import DameUtils

class DameEthnicity(object):

    def surname2ethnicity(self, surname):
        path = 'files/names/names_us/surnames.csv'
        print(path)
        boolean = False
        with open(path) as csvfile:
            surnamereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(surnamereader, None)
            w = ""
            b = ""
            api = ""
            aian = ""
            doublerace = ""
            h = ""
            for row in surnamereader:
#                print(row)
                if (row[0] == surname):
                    # white
                    w = row[5]
                    # black
                    b = row[6]
                    # api = Asian Pacific American
                    api = row[7]
                    # aian = American Indian and Alaska Native
                    aian = row[8]
                    # 2prace
                    doublerace = row[9]
                    # hispanic
                    h = row[10]
        dicc = {"white": w, "black": b, "api": api, "aian": aian, "doublerace": doublerace, "hispanic": h}
        if (dicc == {"white": "", "black": "", "api": "", "aian": "", "doublerace": "", "hispanic": ""}):
            res = False
        else:
            res = dicc
        return res

# de = DameEthnicity()
# dicc = de.surname2ethnicity("Smith")
