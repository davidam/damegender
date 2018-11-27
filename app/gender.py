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

from nltk.corpus import names
import csv

class Gender(object):
# That's the root class in the heritage, apis classes and sexmachine is inheriting from gender
    def __init__(self):
        self.males = 0
        self.females = 0
        self.unknown = 0

    def guess(self, name, binary=False):
    # guess method to check names dictionary
        guess = ''
        if (name in names.words('male.txt')) and (name in names.words('female.txt')):
            if binary:
                guess = 2
            else:
                guess = 'unknown'
        elif name in names.words('male.txt'):
            if binary:
                guess = 1
            else:
                guess = 'male'
        elif name in names.words('female.txt'):
            if binary:
                guess = 0
            else:
                guess = 'female'
        else:
            if binary:
                guess = 2
            else:
                guess = 'unknown'
        return guess

    def gender_list(self, path='files/partial.csv'):
        glist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(sexreader, None)
            count_females = 0
            count_males = 0
            count_unknown = 0
            for row in sexreader:
                gender = row[4]
                if (gender == 'f'):
                    g = 0
                    count_females = count_females + 1
                elif (gender == 'm'):
                    g = 1
                    count_males = count_males + 1
                else:
                    g = 2
                    count_unknown = count_unknown + 1
                glist.append(g)
        self.females = count_females
        self.males = count_males
        self.unknown = count_unknown
        return glist
