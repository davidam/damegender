#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,


import requests
import json
import os
from app.dame_gender import Gender
from app.dame_utils import DameUtils
du = DameUtils()


class DameGenderApi(Gender):

    def get(self, name):
        # it allows to download a name from an API
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            fichero = open("files/apikeys/genderapipass.txt", "r+")
            contenido = fichero.readline()
            contenido = contenido.replace('\n', '')
            string = 'https://gender-api.com/get?name=' + name
            string = string + '&key=' + contenido
            r = requests.get(string)
            j = json.loads(r.text)
            v = [j['gender'], j['accuracy'], j['samples']]
        return v

    def guess(self, name, gender_encoded=False, *args, **kwargs):
        # returns a gender from a name
        standard = kwargs.get('standard', 'damegender')
        v = self.get(name)
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            guess = v[0]
            if (guess == 'male'):
                if gender_encoded:
                    guess_damegender = 1
                    guess_isoiec5218 = 1
                    guess_rfc6350 = "m"
                else:
                    guess_damegender = "male"
                    guess_isoiec5218 = "male"
                    guess_rfc6350 = "male"                    
            elif (guess == 'female'):
                if gender_encoded:
                    guess_damegender = 0
                    guess_isoiec5218 = 2
                    guess_rfc6350 = "f"
                else:
                    guess_damegender = "female"
                    guess_isoiec5218 = "female"
                    guess_rfc6350 = "female"

            else:
                if gender_encoded:
                    guess_damegender = 2
                    guess_isoiec5218 = 9
                    guess_rfc6350 = "u"
                else:
                    guess_damegender = "unknow"
                    guess_isoiec5218 = "not know"
                    guess_rfc6350 = "undefined"
        else:
            if gender_encoded:
                guess_damegender = 2
                guess_isoiec5218 = 9
                guess_rfc6350 = "u"
            else:
                guess_damegender = "unknow"
                guess_isoiec5218 = "not know"
                guess_rfc6350 = "undefined"
        if (standard == "damegender"):
            guess = guess_damegender
        elif (standard == "rfc6350"):
            guess = guess_rfc6350
        elif (standard == "isoiec5218"):
            guess = guess_isoiec5218
        return guess

    def accuracy(self, name):
        # returns the percentage of men or women using a name
        v = self.get(name)
        return v[1]

    def samples(self, name):
        # returns the number of people using a name
        v = self.get(name)
        return v[2]

    def download(self, path="files/names/partial.csv", *args, **kwargs):
        # download a json of people's names from a csv given
        name_position = kwargs.get('name_position', 0)
        genderapipath = "files/names/genderapi" + du.path2file(path) + ".json"
        backup = kwargs.get('backup', genderapipath)
        fichero = open("files/apikeys/genderapipass.txt", "r+")
        if backup:
            backup = open(backup, "w+")
        else:
            backup = open(genderapipath, "w+")
        contenido = fichero.readline()
        contenido = contenido.replace('\n', '')
        string = ""
        names = self.csv2names(path, name_position=name_position)
        names_list = du.split(names, 20)
        jsondict = {'names': []}
        string = ""
        for l1 in names_list:
            # generating names string to include in url
            count = 1
            stringaux = ""
            for n in l1:
                if (len(l1) > count):
                    stringaux = stringaux + n + ";"
                else:
                    stringaux = stringaux + n
                count = count + 1
            url1 = 'https://gender-api.com/get?name=' + stringaux
            url1 = url1 + '&multi=true&key=' + contenido
            r = requests.get(url1)
            j = json.loads(r.text)
            jsondict['names'].append(j['result'])
        jsonv = json.dumps(jsondict)
        backup.write(jsonv)
        backup.close()
        return 1

    def download_csv(self, path="files/names/partial.csv", *args, **kwargs):
        # download a csv of people's names from a csv given
        dir0 = 'files/tmp/'
        if (not os.path.exists(dir0)):
            os.mkdir('files/tmp/')
        backup_all = kwargs.get('backup_all',
                                dir0 + 'genderapiall.csv')
        backup_females = kwargs.get('backup_females',
                                    dir0 + 'genderapifemales.csv')
        backup_males = kwargs.get('backup_males',
                                  dir0 + 'genderapimales.csv')
        name_position = kwargs.get('name_position', 0)
        names = self.csv2names(path, name_position=name_position)
        if backup_females:
            file_females = open(backup_females, "w+")
        if backup_males:
            file_males = open(backup_males, "w+")
        if backup_all:
            file_all = open(backup_all, "w+")

        for i in names:
            name = self.get(i)
            guess = self.guess(i)
            if (guess == "female"):
                file_females.write(str(i)+","+str(name[2])+"\n")
            if (guess == "male"):
                file_males.write(str(i)+","+str(name[2])+"\n")
            if ((guess == "male") or (guess == "female")):
                file_all.write(str(i)+","+str(name[2])+"\n")
        file_females.close()
        file_males.close()
        file_all.close()
        return 1

    def json2gender_list(self, jsonf="", gender_encoded=False, *args, **kwargs):
        # transforms the json into a gender_encoded array of males and females
        standard = kwargs.get('standard', 'damegender')        
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        guesslist = []
        for i in json_object["names"][0]:
            if gender_encoded:
                if (i["gender"] == 'female'):
                    guess_damegender = 0
                    guess_isoiec5218 = 2
                    guess_rfc6350 = "f"
                elif (i["gender"] == 'male'):
                    guess_damegender = 1
                    guess_isoiec5218 = 1
                    guess_rfc6350 = "m"
                else:
                    guess_damegender = 2
                    guess_isoiec5218 = 0
                    guess_rfc6350 = "u"
                if (standard == "damegender"):
                    guesslist.append(guess_damegender)
                elif (standard == "isoiec5218"):
                    guesslist.append(guess_isoiec5218)
                elif (standard == "rfc6350"):
                    guesslist.append(guess_rfc6350)
            else:
                if ((i["gender"] == "male") or (i["gender"] == "female")):
                    guesslist.append(i["gender"])
                else:
                    if (standard == "damegender"):
                        guesslist.append("unknown")
                    elif (standard == "isoiec5218"):
                        guesslist.append("not know")
                    elif (standard == "rfc6350"):
                        guesslist.append("undefined")
        return guesslist

    def json2names(self, jsonf="", surnames=False):
        # transforms the json into an array of male and female names
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        nameslist = []
        for i in json_object["names"][0]:
            if (i["name"] != ''):
                if surnames:
                    nameslist.append([i["name"], i["surname"]])
                else:
                    nameslist.append(i["name"])
        return nameslist

    def guess_list(self, path="files/names/partial.csv", gender_encoded=False, *args, **kwargs):
        # returns a list of males, females
        standard = kwargs.get('standard', 'damegender')
        fichero = open("files/apikeys/genderapipass.txt", "r+")
        contenido = fichero.readline()
        string = ""
        names = self.csv2names(path)
        list_total = []
        names_list = du.split(names, 20)
        for l1 in names_list:
            count = 1
            string = ""
            for n in l1:
                if (len(l1) > count):
                    string = string + n + ";"
                else:
                    string = string + n
                count = count + 1
            url = 'https://gender-api.com/get?name='
            url = url + string + '&multi=true&key=' + contenido
            r = requests.get(url)
            d = json.loads(r.text)
            slist = []
            for item in d['result']:
                if (((item['gender'] is None) or
                     (item['gender'] == 'unknown')) & gender_encoded):
                    if (standard == "damegender"):
                        slist.append(2)
                    elif (standard == "isoiec5218"):
                        slist.append(0)
                    elif (standard == "rfc6350"):
                        slist.append("u")
                elif (((item['gender'] is None) or
                       (item['gender'] == 'unknown')) & (not(gender_encoded))):
                    if (standard == "damegender"):
                        slist.append("unknown")
                    elif (standard == "isoiec5218"):
                        slist.append("not know")
                    elif (standard == "rfc6350"):
                        slist.append("undefined")
                elif ((item['gender'] == "male") & gender_encoded):
                    if (standard == "damegender"):
                        slist.append(1)
                    elif (standard == "isoiec5218"):
                        slist.append(1)
                    elif (standard == "rfc6350"):
                        slist.append("m")
                elif ((item['gender'] == "male") & (not(gender_encoded))):
                    slist.append("male")
                elif ((item['gender'] == "female") & gender_encoded):
                    if (standard == "damegender"):
                        slist.append(0)
                    elif (standard == "isoiec5218"):
                        slist.append(2)
                    elif (standard == "rfc6350"):
                        slist.append("f")
                elif ((item['gender'] == "female") & (not(gender_encoded))):
                    slist.append("female")                    
            # print("string: " + string)
            # print("slist: " + str(slist))
            # print("slist len:" + str(len(slist)))
            list_total = list_total + slist
        return list_total

    def apikey_limit_exceeded_p(self):
        # returns a boolean explaining if the limit
        # has been exceeded
        j = ""
        limit_exceeded_p = True
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            fichero = open("files/apikeys/genderapipass.txt", "r+")
            contenido = fichero.readline()
            contenido = contenido.replace('\n', '')
            string = 'https://gender-api.com/get-stats?key=' + contenido
            r = requests.get(string)
            j = json.loads(r.text)
            limit_exceeded_p = j["is_limit_reached"]
        return limit_exceeded_p

    def apikey_count_requests(self):
        # returns the count of request done to the API
        count = -1
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            fichero = open("files/apikeys/genderapipass.txt", "r+")
            contenido = fichero.readline()
            contenido = contenido.replace('\n', '')
            string = 'https://gender-api.com/get-stats?key=' + contenido
            r = requests.get(string)
            j = json.loads(r.text)
            count = j["remaining_requests"]
        return count
