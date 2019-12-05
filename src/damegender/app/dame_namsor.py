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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv
import requests
import json
import numpy as np

from app.dame_utils import DameUtils
from app.dame_gender import Gender


class DameNamsor(Gender):

    def get(self, name, surname, binary=False):
        # obtaining data from namsor
        string = 'https://api.namsor.com/onomastics/api/json/gender/'
        string = string + name + '/' + surname
        r = requests.get(string)
        d = json.loads(r.text)
        v = [d['gender'], d['scale']]
        return v

    def guess(self, name, surname, binary=False):
        # guess method to check names dictionary
        v = self.get(name, surname)
        if ((v[0] == 'female') and binary):
            guess = 0
        elif ((v[0] == 'male') and binary):
            guess = 1
        elif ((v[0] == 'unknown') and binary):
            guess = 2
        else:
            guess = v[0]
        return guess

    def scale(self, name, surname):
        # scale is a probability measure
        v = self.get(name, surname)
        return v[1]

    def guess_list(self, path='files/partial.csv', binary=False):
        # guess list method
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                surname = row[2].title()
                surname = surname.replace('\"', '')
                slist.append(self.guess(name, surname, binary))
        return slist

    def download(self, path="files/names/min.csv"):
        du = DameUtils()
        namsorjson = path
        namsorjson = open("files/names/namsor"+du.path2file(path)+".json", "w+")
        surnames=True
        names = self.csv2names(path, surnames=surnames)
        namsorjson.write("[")
        length = len(names)
        i = 0
        while (i < length):
            name = names[i][0]
            namsorjson.write('{"name":"'+str(names[i][0])+'",\n')
            surname = names[i][1]
            namsorjson.write('"surname":"'+str(names[i][1])+'",\n')
            dnget = self.get(name=name, surname=surname, binary=True)
            namsorjson.write('"gender":"'+str(dnget[0])+'",\n')
            namsorjson.write('"scale":'+str(dnget[1])+'\n')
            if ((length -1) == i):
                namsorjson.write('} \n')
            else:
                namsorjson.write('}, \n')
            i = i + 1
        namsorjson.write("]")
        namsorjson.close()

    def json2guess_list(self, jsonf="", binary=False):
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        guesslist = []

        for i in json_object:
            if binary:
                if (i['gender'] == 'female'):
                    guesslist.append(0)
                elif (i['gender'] == 'male'):
                    guesslist.append(1)
                else:
                    guesslist.append(2)
            else:
                guesslist.append(i['gender'])
        return guesslist
