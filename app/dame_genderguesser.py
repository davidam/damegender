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

import csv
import requests
import json
import gender_guesser.detector as gender

class Genderguesser(object):
    def guess(self, name, binary=False):
    # guess method to check names dictionary
        genderguesserlist = []
        d = gender.Detector()
        get = d.get_gender(name)
        if ((get == 'female') and binary):
            guess = 0
        elif ((get == 'male') and binary):
            guess = 1
        elif (not(binary)):
            guess = get
        return guess
    
    # def list(self):
    #     d = gender.Detector()
    #     with open('files/partial.csv') as csvfile:
    #         genderguesserreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #         next(genderguesserreader, None)
    #         genderguesserlist = []
    #         for row in genderguesserreader:
    #             name = row[0]
    #             name = name.replace('"', '')
    #             name = name.capitalize()
    #             genderguesserlist.append((name, d.get_gender(name)))
    #     return genderguesserlist
# #        print(d.get_gender(name.capitalize()))

# dgg = Genderguesser()
# print(dgg.guess("Sara", binary=False))
# print(gg.list())
