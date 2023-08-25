#!/usr/bin/python
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

import csv
import requests
import json

from app.dame_utils import DameUtils
from app.dame_gender import Gender

du = DameUtils()


class DameNamsor(Gender):

    def get(self, name, surname, gender_encoded=False):
        # obtaining data from namsor returning a vector
        fichero = open("files/apikeys/namsorpass.txt", "r+")
        contenido = fichero.readline().rstrip()
        url = 'https://v2.namsor.com/NamSorAPIv2/api2/json/gender/'
        url = url + name + '/' + surname
        headers = {'content-type': 'application/json',
                   'Accept-Charset': 'UTF-8',
                   'X-API-KEY': contenido}
        r = requests.get(url, headers=headers)
        d = json.loads(r.text)
        v = [d['likelyGender'], d['genderScale']]
        return v

    def getGeo(self, name, surname, locale, gender_encoded=False):
        # obtaining data from namsor taking into account
        # geographical data
        fichero = open("files/apikeys/namsorpass.txt", "r+")
        contenido = fichero.readline().rstrip()
        url = 'https://v2.namsor.com/NamSorAPIv2/api2/json/genderGeo/'
        url = url + name + '/' + surname + '/' + locale
        headers = {'content-type': 'application/json',
                   'Accept-Charset': 'UTF-8',
                   'X-API-KEY': contenido}
        r = requests.get(url, headers=headers)
        d = json.loads(r.text)
        v = [d['likelyGender'], d['genderScale']]
        return v

    def guess(self, name, surname, gender_encoded=False, *args, **kwargs):
        # guess gender from name and surname
        # using get method
        standard = kwargs.get('standard', 'damegender')        
        v = self.get(name, surname)
        if ((v[0] == 'female') and gender_encoded):
            guess_damegender = 0
            guess_isoiec5218 = 2
            guess_rfc6350 = "f"
        elif ((v[0] == 'female') and not(gender_encoded)):
            guess_damegender = "female"
            guess_isoiec5218 = "female"
            guess_rfc6350 = "female"
        elif ((v[0] == 'male') and gender_encoded):
            guess_damegender = 1
            guess_isoiec5218 = 1
            guess_rfc6350 = "m"
        elif ((v[0] == 'male') and not(gender_encoded)):
            guess_damegender = "male"
            guess_isoiec5218 = "male"
            guess_rfc6350 = "male"                    
        elif ((v[0] == 'unknown') and gender_encoded):
            guess_damegender = 2
            guess_isoiec5218 = 9
            guess_rfc6350 = "u"
        elif ((v[0] == 'unknown') and not(gender_encoded)):
            guess_damegender = "unknow"
            guess_isoiec5218 = "not know"
            guess_rfc6350 = "undefined"
        else:
            guess_damegender, guess_isoiec5218, guess_rfc6350 = v[0]
        if (standard == "damegender"):
            guess = guess_damegender
        elif (standard == "isoiec5218"):
            guess = guess_isoiec5218
        elif (standard == "rfc6350"):
            guess = guess_rfc6350            
        return guess

    def scale(self, name, surname):
        # scale is a probability measure
        v = self.get(name, surname)
        return v[1]

    def guess_list(self, path='files/partial.csv', gender_encoded=False):
        # returns a guess list from a CSV file
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                surname = row[2].title()
                surname = surname.replace('\"', '')
                slist.append(self.guess(name, surname, gender_encoded))
        return slist

    def download(self, path="files/names/min.csv"):
        # A JSON file is created from a CSV file.
        # It takes the first and last names from the CSV
        # file and uses them to get the gender and scale of each name.
        namsorpath = "files/names/namsor" + du.path2file(path) + ".json"
        namsorjson = open(namsorpath, "w+")
        surnames = True
        names = self.csv2names(path, surnames=surnames)
        namsorjson.write("[")
        length = len(names)
        i = 0
        while (i < length):
            name = names[i][0]
            namsorjson.write('{"name":"' + str(names[i][0]) + '",\n')
            surname = names[i][1]
            namsorjson.write('"surname":"' + str(names[i][1]) + '",\n')
            dnget = self.get(name=name, surname=surname, gender_encoded=True)
            namsorjson.write('"gender":"' + str(dnget[0]) + '",\n')
            namsorjson.write('"scale":' + str(dnget[1]) + '\n')
            if ((length - 1) == i):
                namsorjson.write('} \n')
            else:
                namsorjson.write('}, \n')
            i = i + 1
        namsorjson.write("]")
        namsorjson.close()

    def download_csv(self, path="files/names/min.csv", *args, **kwargs):
        # A CSV file is created from a CSV file.
        # It takes the first and last names from the CSV
        # file and uses them to get the gender and scale of each name.
        dir0 = "files/tmp/"
        backup_all = kwargs.get('backup_all',
                                dir0 + 'namsorall.csv')
        backup_females = kwargs.get('backup_females',
                                    dir0 + 'namsorfemales.csv')
        backup_males = kwargs.get('backup_males',
                                  dir0 + 'namsormales.csv')
        name_position = kwargs.get('name_position', 0)
        names = self.csv2names(path, name_position=name_position,
                               surname_position=surname_position,
                               surnames=True)
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
