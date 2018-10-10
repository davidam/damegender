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

# class Genderguesser(object):
#     def list(self):
#         d = gender.Detector()
#         with open('partial.csv') as csvfile:
#             genderguesserreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#             next(genderguesserreader, None)
#             genderguesserlist = []
#             for row in genderguesserreader:
#                 name = row[0]
#                 name = name.replace('"', '')
#                 name = name.capitalize()
#                 print(d.get_gender(name))
#                 genderguesserlist.append((name, d.get_gender(name)))
# #        print(d.get_gender(name.capitalize()))

# gg = Genderguesser()
# d = gender.Detector()
# genderguesserlist =  gg.list()

# print(genderguesserlist)
# print("Bob is", d.get_gender(u"Bob"))
# print("Sally is", d.get_gender(u"Sally"))
# print("Pauley is", d.get_gender(u"Pauley"))
# print("Jamie is", d.get_gender(u"Jamie", u'great_britain'))
