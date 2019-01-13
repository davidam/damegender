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
from app.dame_gender import Gender
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


class DameGenderize(Gender):
    def guess(self, name, binary=False):
    # guess method to check names dictionary
        v = Genderize().get([name])
        g = v[0]['gender']
        if ((g == 'female') and binary):
            guess = 0
        elif ((g == 'male') and binary):
            guess = 1
        elif (not(binary)):
            guess = g
        return guess

    def guess_list(self, path='files/partial.csv', binary=False):
    # guess list method
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            i = 0
#            string = ""
            listnames = list()
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"','')
                listnames.append(name)
#        print("len listnames:"+str(len(listnames)))
        new = []
        for i in range(0, len(listnames), 10): # We must split the list in different lists with size 10
            new.append(listnames[i : i+10])
        for i in new:
            jsonlist = Genderize().get(i)
#            print("len jsonlist:"+str(len(jsonlist)))
            for item in jsonlist:
                if ((item['gender'] == None) & binary):
                    slist.append(2)
                elif ((item['gender'] == None) & (not binary)):
                    slist.append("unknown")
                elif ((item['gender'] == "male") & binary):
                    slist.append(1)
                elif ((item['gender'] == "male") & (not binary) ):
                    slist.append("male")
                elif ((item['gender'] == "female") & binary):
                    slist.append(0)
                elif ((item['gender'] == "female") & (not binary) ):
                    slist.append("female")
        return slist

    def accuracy(self, path):
        gl = self.gender_list(path)
        sl = self.guess_list(path, binary=True)
        return accuracy_score(gl, sl)
