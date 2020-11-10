#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

from genderize import Genderize
import csv
import requests
import json
import configparser
from app.dame_gender import Gender
from app.dame_utils import DameUtils
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

class DameGenderize(Gender):

    def get(self, name, *args, **kwargs):
        # obtaining data from genderize
        string = 'https://api.genderize.io/?name='
        string = string + name
        if ('country_id' in kwargs):
            string = string + "&country_id=" + kwargs.get('country_id')
        if ('surname' in kwargs):
            string = string + "&surname=" + kwargs.get('surname')
        r = requests.get(string)
        d = json.loads(r.text)
        return d

    def get2to10(self, l):
        string = 'https://api.genderize.io/'

        if ((len(l) > 1) and (len(l) <= 10)):
            string = string + '?name[]='+l[0]
            for i in l[1:10]:
                string = string + '&name[]='+ i
            r = requests.get(string)
            d = json.loads(r.text)
        elif (len(l) == 1):
            d = [self.get(l[0])]
        else:
            d = ""
        return d

    def guess(self, name, binary=False):
        d = self.get(name)
        if (binary == True):
            if (d['gender'] == 'female'):
                gender = 0
            elif (d['gender'] == 'male'):
                gender = 1
            else:
                gender = 2
        else:
            gender = d['gender']
        return gender

    def prob(self, name):
        d = self.get(name)
        return d['probability']

    def download(self, path='files/names/partial.csv', surnames=False):
        du = DameUtils()
        new = []
        d = ""
        lresult = []
        res = ""
        if (surnames == True):
            l = self.csv2names(path, surnames=True)
            for i in range(0, len(l)):
                d = self.get(l[i][0], surname=l[i][1])
                d["surname"] = l[i][1]
                lresult.append(d)
            res = str(lresult)
        else:
            l = self.csv2names(path)
            # We must split the list in different lists with size 10
            for i in range(0, len(l), 10):
                new.append(l[i:i+10])
            for j in new:
                lresult.append(self.get2to10(j))
            for k in lresult:
                res = res + str(k)
        res = str(res).replace("\'", "\"")
        res = str(res).replace('None', '"unknown"')
        backup = open("files/names/genderize"+du.path2file(path)+".json", "w+")
        backup.write(res)
        backup.close()
        return res

    def json2guess_list(self, jsonf="", binary=False):
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        guesslist = []
        for i in json_object:
            if binary:
                if (i["gender"] == 'female'):
                    guesslist.append(0)
                elif (i["gender"] == 'male'):
                    guesslist.append(1)
                else:
                    guesslist.append(2)
            else:
                guesslist.append(i["gender"])
        return guesslist


    def apikey_limit_exceeded_p(self):
        j = ""
        if (self.config['DEFAULT']['genderize'] == 'yes'):
            fichero = open("files/apikeys/genderizepass.txt", "r+")
            contenido = fichero.readline()
            contenido = contenido.replace('\n', '')
            string = 'https://api.genderize.io/?name[]=peter&name[]=lois&name[]=stevie?apikey=' + contenido
        else:
            string = 'https://api.genderize.io/?name[]=peter&name[]=lois&name[]=stevie'
        r = requests.get(string)
        j = json.loads(r.text)
        if (j["error"] is not None):
            p = True
        else:
            p = False
        return p


    # def guess(self, name, binary=False):
    #     # guess method to check names dictionary
    #     if (self.config['DEFAULT']['genderize'] == 'no'):
    #         v = Genderize().get([name])
    #     elif (self.config['DEFAULT']['genderize'] == 'yes'):
    #         fichero = open(self.config['FILES']['genderize'], "r+")
    #         apikey = fichero.readline().rstrip()
    #         v = Genderize(
    #             user_agent='GenderizeDocs/0.0',
    #             api_key=apikey).get([name])
    #     g = v[0]['gender']
    #     if ((g == 'female') and binary):
    #         guess = 0
    #     elif ((g == 'male') and binary):
    #         guess = 1
    #     elif (not(binary)):
    #         guess = g
    #     return guess


    # def prob(self, name, binary=False):
    #     # guess method to check names dictionary
    #     if (self.config['DEFAULT']['genderize'] == 'no'):
    #         v = Genderize().get([name])
    #     elif (self.config['DEFAULT']['genderize'] == 'yes'):
    #         fichero = open(self.config['DEFAULT']['genderizefile'], "r+")
    #         apikey = fichero.readline().rstrip()
    #         v = Genderize(
    #             user_agent='GenderizeDocs/0.0',
    #             api_key=apikey).get([name])
    #     prob = v[0]['probability']
    #     return prob

    # def guess_list(self, path='files/names/partial.csv', binary=False):
    #     # guess list method
    #     slist = []
    #     with open(path) as csvfile:
    #         sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #         next(sexreader, None)
    #         i = 0
    #         genderlist = list()
    #         for row in sexreader:
    #             name = row[0].title()
    #             name = name.replace('\"', '')
    #             genderlist.append(name)
    #     new = []
    #     # We must split the list in different lists with size 10
    #     for i in range(0, len(genderlist), 10):
    #         new.append(genderlist[i:i+10])
    #     for i in new:
    #         if (self.config['DEFAULT']['genderize'] == 'no'):
    #             jsonlist = Genderize().get(i)
    #         elif (self.config['DEFAULT']['genderize'] == 'yes'):
    #             fichero = open("files/apikeys/genderizepass.txt", "r+")
    #             apikey = fichero.readline().rstrip()
    #             jsonlist = Genderize(user_agent='GenderizeDocs/0.0',
    #                                  api_key=apikey).get(i)
    #         for item in jsonlist:
    #             if ((item['gender'] is None) & binary):
    #                 slist.append(2)
    #             elif ((item['gender'] is None) & (not binary)):
    #                 slist.append("unknown")
    #             elif ((item['gender'] == "male") & binary):
    #                 slist.append(1)
    #             elif ((item['gender'] == "male") & (not binary)):
    #                 slist.append("male")
    #             elif ((item['gender'] == "female") & binary):
    #                 slist.append(0)
    #             elif ((item['gender'] == "female") & (not binary)):
    #                 slist.append("female")
    #     return slist
