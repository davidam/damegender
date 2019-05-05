#!/usr/bin/python3
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
from app.dame_gender import Gender

class DameGenderApi(Gender):

    def get(self, name):
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            fichero = open("files/apikeys/genderapipass.txt", "r+")
            contenido = fichero.readline()
            r = requests.get('https://gender-api.com/get?name='+name+'&key='+contenido)
            j = json.loads(r.text)
            v = [j['gender'], j['accuracy']]
        return v

    def guess(self, name, binary=False):
        v = self.get(name)
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            guess = v[0]
            if (guess == 'male'):
                if binary:
                    guess = 1
            elif (guess == 'female'):
                if binary:
                    guess = 0
            else:
                if binary:
                    guess = 2
                else:
                    guess = 'unknown'
        else:
            if binary:
                guess = 2
            else:
                guess = 'unknown'
        return guess

    def accuracy(self, name):
        v = self.get(name)
        return v[1]

    def guess_list(self, path="files/names/partial.csv", binary=False):
        fichero = open("files/apikeys/genderapipass.txt", "r+")
        contenido = fichero.readline()
        string = ""
        names = self.csv2names(path)
#        print(names)
        count = 1
        for n in names:
            if (len(names) > count):
                string = string + n + ";"
            else:
                string = string + n
            count = count + 1
        r = requests.get('https://gender-api.com/get?name='+string+'&multi=true&key='+contenido)
        d = json.loads(r.text)
        slist = []
        for item in d['result']:
            if ((item['gender'] == None) & binary):
                slist.append(2)
            elif ((item['gender'] == None) & (not binary)):
                slist.append("unknown")
            elif ((item['gender'] == "male") & binary):
                slist.append(1)
            elif ((item['gender'] == "male") & (not binary)):
                slist.append("male")
            elif ((item['gender'] == "female") & binary):
                slist.append(0)
            elif ((item['gender'] == "female") & (not binary)):
                slist.append("female")
        return slist
