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
import numpy as np

from app.dame_gender import Gender

class DameNamsor(Gender):

    def guess(self, name, surname, binary=False):
    # guess method to check names dictionary
        namsorlist = []
        r = requests.get('https://api.namsor.com/onomastics/api/json/gender/'+ name +'/' + surname)
        d = json.loads(r.text)
        if ((d['gender'] == 'female') and binary):
            guess = 0
        elif ((d['gender'] == 'male') and binary):
            guess = 1
        elif ((d['gender'] == 'unknown') and binary):
            guess = 2
        else:
            guess = d['gender']
        return guess

    def guess_list(self, path='files/partial.csv', binary=False):
    # guess list method
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"','')
                surname = row[2].title()
                surname = surname.replace('\"','')
                slist.append(self.guess(name, surname, binary))
        return slist
