#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv
import requests
import json
import os
from app.dame_gender import Gender
from app.dame_utils import DameUtils


class DameGenderApi(Gender):

    def get(self, name):
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            fichero = open("files/apikeys/genderapipass.txt", "r+")
            contenido = fichero.readline()
            contenido = contenido.replace('\n', '')
            string = 'https://gender-api.com/get?name=' + name
            string = string + '&key=' + contenido
            r = requests.get(string)
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

    def download(self, path="files/names/partial.csv"):
        du = DameUtils()
        fichero = open("files/apikeys/genderapipass.txt", "r+")
        backup = open("files/names/genderapi"+du.path2file(path)+".json", "w+")
        contenido = fichero.readline()
        contenido = contenido.replace('\n', '')
        string = ""
        names = self.csv2names(path)
        names_list = du.split(names, 20)
        jsondict = {'names': []}
        string = ""
        for l in names_list:
            # generating names string to include in url
            count = 1
            stringaux = ""
            for n in l:
                if (len(l) > count):
                    stringaux = stringaux + n + ";"
                else:
                    stringaux = stringaux + n
                count = count + 1
                #            string = string + ";" + stringaux
            url1 = 'https://gender-api.com/get?name=' + stringaux
            url1 = url1 + '&multi=true&key=' + contenido
            r = requests.get(url1)
            j = json.loads(r.text)
            jsondict['names'].append(j['result'])
        jsonv = json.dumps(jsondict)
        backup.write(jsonv)
        backup.close()
        return 1

    def json2guess_list(self, jsonf="", binary=False):
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        guesslist = []
        for i in json_object["names"][0]:
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

    def json2names(self, jsonf="", surnames=False):
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        nameslist = []
        for i in json_object["names"][0]:
            if (i["name"] != ''):
                if (surnames == True):
                    nameslist.append([i["name"], i["surname"]])
                else:
                    nameslist.append(i["name"])
        return nameslist



    def guess_list(self, path="files/names/partial.csv", binary=False):
        du = DameUtils()
        fichero = open("files/apikeys/genderapipass.txt", "r+")
        contenido = fichero.readline()
        string = ""
        names = self.csv2names(path)
        list_total = []
        names_list = du.split(names, 20)
        for l in names_list:
            count = 1
            string = ""
            for n in l:
                if (len(l) > count):
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
                if (((item['gender'] is None) or (item['gender'] == 'unknown')) & binary):
                    slist.append(2)
                elif (((item['gender'] is None) or (item['gender'] == 'unknown')) & (not binary)):
                    slist.append("unknown")
                elif ((item['gender'] == "male") & binary):
                    slist.append(1)
                elif ((item['gender'] == "male") & (not binary)):
                    slist.append("male")
                elif ((item['gender'] == "female") & binary):
                    slist.append(0)
                elif ((item['gender'] == "female") & (not binary)):
                    slist.append("female")
            # print("string: " + string)
            # print("slist: " + str(slist))
            # print("slist len:" + str(len(slist)))
            list_total = list_total + slist
        return list_total

    def apikey_limit_exceeded_p(self):
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
