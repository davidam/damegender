#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from genderize import Genderize
import csv
import requests
import json

class Gendergenderize(object):
    def guess(self, name, binary=False):
    # guess method to check names dictionary
        namsorlist = []
        v = Genderize().get([name])
        g = v[0]['gender']
        if ((g == 'female') and binary):
            guess = 0
        elif ((g == 'male') and binary):
            guess = 1
        elif (not(binary)):
            guess = g
        return guess

    def list(self):
        with open('files/min.csv') as csvfile:
            genderizereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(genderizereader, None)
            l = []
            for row in genderizereader:
                name = row[0]
                name = name.replace('"', '')
                l.append(name)
        lgenderize = Genderize().get(l)
        lgen = []
        for elem in lgenderize:
            lgen.append((elem['name'], elem['gender']))
        return lgen
