#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

#from nltk.corpus import names
#import nltk
import csv
import unidecode
import unicodedata
import numpy as np
import configparser
import os
import re
import sys
import json
import datetime

from collections import OrderedDict
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from app.dame_utils import DameUtils
from app.dame_statistics import DameStatistics

csv.field_size_limit(3000000)

du = DameUtils()
dst = DameStatistics()

class Gender(object):
    # That's the root class in the heritage,
    # apis classes and sexmachine is a gender
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read('config.cfg')
        self.males = 0
        self.females = 0
        self.unknown = 0

    def in_dict(self, name):
        f = os.popen('dict '+name)
        in_dict = False
        for line in f:
            if (re.match(r'[0-9]+ definitions found', line)):
                in_dict = True
        return in_dict

# FEATURES METHODS #

    def features(self, name):
        # features method created to check the nltk classifier
        features = {}
        features["first_letter"] = name[0].lower()
        features["last_letter"] = name[-1].lower()
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features["count({})".format(letter)] = name.lower().count(letter)
            features["has({})".format(letter)] = (letter in name.lower())
        return features

    def features_int(self, name):
        # features method created to check the scikit classifiers
        features_int = {}
        features_int["first_letter"] = ord(name[0].lower())
        features_int["last_letter"] = ord(name[-1].lower())
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            num = name.lower().count(letter)
            features_int["count({})".format(letter)] = num
        features_int["vocals"] = 0
        for letter1 in 'aeiou':
            for letter2 in name:
                if (letter1 == letter2):
                    features_int["vocals"] = features_int["vocals"] + 1
        features_int["consonants"] = 0
        for letter1 in 'bcdfghjklmnpqrstvwxyz':
            for letter2 in name:
                if (letter1 == letter2):
                    features_int["consonants"] = features_int["consonants"] + 1
        # FIRST LETTER
        if (name[0].lower() in 'aeiou'):
            features_int["first_letter_vocal"] = 1
        else:
            features_int["first_letter_vocal"] = 0
        if (name[0].lower() in 'bcdfghjklmnpqrstvwxyz'):
            features_int["first_letter_consonant"] = 1
        else:
            features_int["first_letter_consonant"] = 0
        # LAST LETTER
        if (name[-1].lower() in 'aeiou'):
            features_int["last_letter_vocal"] = 1
        else:
            features_int["last_letter_vocal"] = 0
        if (name[-1].lower() in 'bcdfghjklmnpqrstvwxyz'):
            features_int["last_letter_consonant"] = 1
        else:
            features_int["last_letter_consonant"] = 0
        # h = hyphen.Hyphenator('en_US')
        # features_int["syllables"] = len(h.syllables(name))
        if (name[-1].lower() == "a"):
            features_int["last_letter_a"] = 1
        else:
            features_int["last_letter_a"] = 0
        if (name[-1].lower() == "o"):
            features_int["last_letter_o"] = 1
        else:
            features_int["last_letter_o"] = 0
        return features_int

    def features_list(self, path='files/names/partial.csv', sexdataset=''):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                flist.append(list(self.features_int(name).values()))
        return flist

    def features_list_categorical(self, path='files/names/partial.csv'):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                l = list([self.features_int(name)["first_letter"],
                          self.features_int(name)["last_letter"],
                          self.features_int(name)["last_letter_a"],
                          self.features_int(name)["first_letter_vocal"],
                          self.features_int(name)["last_letter_vocal"],
                          self.features_int(name)["last_letter_consonant"]])
                flist.append(l)
        return flist

    def features_list_no_categorical(self, path='files/names/partial.csv'):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                l = list([self.features_int(name)["count(a)"],
                          self.features_int(name)["count(b)"],
                          self.features_int(name)["count(c)"],
                          self.features_int(name)["count(d)"],
                          self.features_int(name)["count(e)"],
                          self.features_int(name)["count(f)"],
                          self.features_int(name)["count(g)"],
                          self.features_int(name)["count(h)"],
                          self.features_int(name)["count(i)"],
                          self.features_int(name)["count(j)"],
                          self.features_int(name)["count(k)"],
                          self.features_int(name)["count(l)"],
                          self.features_int(name)["count(m)"],
                          self.features_int(name)["count(n)"],
                          self.features_int(name)["count(o)"],
                          self.features_int(name)["count(p)"],
                          self.features_int(name)["count(q)"],
                          self.features_int(name)["count(r)"],
                          self.features_int(name)["count(s)"],
                          self.features_int(name)["count(t)"],
                          self.features_int(name)["count(u)"],
                          self.features_int(name)["count(v)"],
                          self.features_int(name)["count(w)"],
                          self.features_int(name)["count(x)"],
                          self.features_int(name)["count(y)"],
                          self.features_int(name)["count(z)"],
                          self.features_int(name)["vocals"],
                          self.features_int(name)["consonants"]])
                flist.append(l)
        return flist

    def features_list_no_letters(self, path='files/names/partial.csv'):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                l = list([self.features_int(name)["first_letter"],
                          self.features_int(name)["last_letter"],
                          self.features_int(name)["vocals"],
                          self.features_int(name)["consonants"],
                          self.features_int(name)["first_letter_vocal"],
                          self.features_int(name)["last_letter_vocal"],
                          self.features_int(name)["first_letter_consonant"],
                          self.features_int(name)["last_letter_consonant"],
                          self.features_int(name)["last_letter_a"],
                          self.features_int(name)["last_letter_o"]])
                flist.append(l)
        return flist

    def features_list_no_undefined(self, path=''):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                g = row[4].replace('\"', '')
                if ((g == "m") | (g == "f")):
                    flist.append(list(self.features_int(name).values()))
        return flist

    def features_list2csv(self, path, categorical="both"):
        if (categorical == "categorical"):
            fl = self.features_list_categorical(path)
            first_line = "first_letter, last_letter, last_letter_a, " \
                         "first_letter_vocal, last_letter_vocal, " \
                         "last_letter_consonant"
            f = open('files/features_list_cat.csv', 'w')
        elif (categorical == "nocategorical"):
            fl = self.features_list_no_categorical(path)
            first_line = "a, b, c, d, e, f, g, h, i, j, k, l, m, " \
                         "n, o, p, q, r, s, t, u, v, w, x, y, z, " \
                         "vocals, consonants"
            f = open('files/features_list_no_cat.csv', 'w')
        elif (categorical == "noletters"):
            fl = self.features_list_no_letters(path)
            first_line = "first_letter, last_letter, vocals, " \
                         "consonants, first_letter_vocal," \
                         "last_letter_vocal, first_letter_consonant, " \
                         "last_letter_consonant," \
                         "last_letter_a, last_letter_o"
            f = open('files/features_list_no_letters.csv', 'w')
        elif (categorical == "noundefined"):
            fl = self.features_list_no_undefined(path)
            first_line = "first_letter, last_letter, a, b, c, d, e, " \
                         "f, g, h, i, j, k, l, m, n, o, p, q, r, s, " \
                         "t, u, v, w, x, y, z, vocals, consonants, " \
                         "first_letter_vocal, last_letter_vocal, " \
                         "first_letter_consonant, last_letter_consonant, " \
                         "last_letter_a, last_letter_o"
            f = open('files/features_list_no_undefined.csv', 'w')
        else:
            fl = self.features_list(path)
            first_line = "first_letter, last_letter, a, b, c, d, e, f, " \
                         "g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, " \
                         "v, w, x, y, z, vocals, consonants, " \
                         "first_letter_vocal, last_letter_vocal, " \
                         "first_letter_consonant, last_letter_consonant, " \
                         "last_letter_a, last_letter_o"
            f = open('files/features_list.csv', 'w')
        f.write(first_line+"\n")
        for i in fl:
            line = ""
            count = 0
            while (count < (len(i) - 1)):
                line = line + str(i[count]) + ", "
                count = count + 1
            f.write(line+str(i[count])+"\n")
        f.close()
    
    
    # DATASETS METHODS #

    def ukfile(self):
        # create a file with name and prob from uk births
        total = 0
        for i in range(1880, 2018):
            # first we acquire the total of births from 1880 to 2017
            dataset = "files/names/uk/yob" + str(i) + ".txt"
            with open(dataset) as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                totali = 0
                for row in sexreader:
                    datasetcount = row[2]
                    totali = totali + int(datasetcount)
            total = total + totali

        # now we are going to start the json file with 1880
        jsonuk = "files/names/uk/jsonuk.json"
        file = open(jsonuk, "w")
        dataset = "files/names/uk/yob1880.txt"
        with open(dataset) as csvfile:
            sexreader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader1, None)
            cnt = 0
            for row in sexreader1:
                cnt = cnt + 1
        end = cnt
        lines = []
        lines.append('[')
        with open(dataset) as csvfile:
            sexreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader2, None)
            cnt = 1
            for row in sexreader2:
                lines.append('{"name": "' + row[0] + '",')
                lines.append('"gender": "' + row[1] + '",')
                if (end == cnt):
                    lines.append('"count": ' + row[2] + '}')
                    print('"count": ' + row[2] + '}')
                else:
                    lines.append('"count": ' + row[2] + '},')
                    print('"count": ' + row[2] + '},')
                cnt = cnt + 1
            lines.append(']')
        fo = open(jsonuk, "w")
        fo.writelines(lines)
        # Cerramos el archivo
        for i in range(1881, 2018):
            dataset = "files/names/uk/yob" + str(i) + ".txt"
            with open(dataset) as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                lines = []
                for row in sexreader:
                    print(row)
                #         Cerramos el archivo
        fo.close()
        return 1

    def males_list(self, corpus='es'):
        au_path = 'files/names/names_au/baby-names-1944-2013/aumales.csv'
        ca_path = 'files/names/names_ca/camales.csv'        
        ine_path = 'files/names/names_es/masculinos.txt'
        nz_path = 'files/names/names_nz/nzmales.csv'
#        pt_path = 'files/names/names_pt/ptmales.csv'        
        uy_path = 'files/names/names_uy/uymasculinos.txt'
        uk_path = 'files/names/names_uk/ukmales.txt'
        us_path = 'files/names/names_us/usmales.txt'

        m = []
        if (corpus == 'au'):
            m = du.csvcolumn2list(ine_path)
        elif ((corpus == 'es') or (corpus == 'ine')):
            m = du.csvcolumn2list(ine_path)
        elif (corpus == 'ca'):
            m = du.csvcolumn2list(ca_path)
        elif (corpus == 'nz'):
            m = du.csvcolumn2list(nz_path)
        # elif (corpus == 'pt'):
        #     m = du.csvcolumn2list(pt_path)            
        elif (corpus == 'uk'):
            m = du.csvcolumn2list(uk_path)
        elif (corpus == 'us'):
            m = du.csvcolumn2list(us_path)
        elif (corpus == 'uy'):
            m = du.csvcolumn2list(uy_path)
        elif (corpus == 'all'):
            m = du.csvcolumn2list(au_path) + du.csvcolumn2list(ca_path) + du.csvcolumn2list(ine_path) + du.csvcolumn2list(nz_path) + du.csvcolumn2list(uk_path) + du.csvcolumn2list(us_path) + du.csvcolumn2list(uy_path) 
        m = du.delete_duplicated(m)
        return m

    def females_list(self, corpus='es'):
        au_path = 'files/names/names_au/baby-names-1944-2013/aufemales.csv'
        ca_path = 'files/names/names_ca/cafemales.csv'        
        ine_path = 'files/names/names_es/femeninos.txt'
        nz_path = 'files/names/names_nz/nzfemales.csv'
#        pt_path = 'files/names/names_pt/ptfemales.csv'        
        uk_path = 'files/names/names_uk/ukfemales.txt'
        us_path = 'files/names/names_us/usfemales.txt'
        uy_path = 'files/names/names_uy/uyfemeninos.txt'

        f = []
        if (corpus == 'au'):
            f = du.csvcolumn2list(ine_path)
        elif (corpus == 'ca'):
            f = du.csvcolumn2list(nz_path)                        
        elif ((corpus == 'es') or (corpus == 'ine')):
            f = du.csvcolumn2list(ine_path)
        elif (corpus == 'nz'):
            f = du.csvcolumn2list(nz_path)
        # elif (corpus == 'pt'):
        #     f = du.csvcolumn2list(pt_path)                        
        elif (corpus == 'uk'):
            f = du.csvcolumn2list(uk_path)
        elif (corpus == 'us'):
            f = du.csvcolumn2list(us_path)
        elif (corpus == 'uy'):
            f = du.csvcolumn2list(uy_path)
        elif (corpus == 'all'):
            f = du.csvcolumn2list(au_path) + du.csvcolumn2list(ca_path) + du.csvcolumn2list(ine_path) + du.csvcolumn2list(nz_path) + du.csvcolumn2list(us_path) + du.csvcolumn2list(us_path) + du.csvcolumn2list(uy_path) 
        f = du.delete_duplicated(f)
        return f


    def csv2names(self, path='files/names/partial.csv', *args, **kwargs):
        # make a list from a csv file
        surnames = kwargs.get('surnames', False)
        header = kwargs.get('header', True)
        csvlist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            if (header == True):
                next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                # middlename = row[1].replace(' ', '')
                # middlename = row[1].replace('\"', '')

                # if (name_and_middlename == True):
                #     name = name + " " + middlename
                #     name = name.title()

                if (surnames == True):
                    surname = row[2].title()
                    surname = row[2].replace('\"', '')
                    elem = [name, surname]
                    csvlist.append(elem)
                else:
                    csvlist.append(name)
        return csvlist


    def csv2json(self, path="", *args, **kwargs):
        # csv to json file
        surnames = kwargs.get('surnames', False)
        header = kwargs.get('header', True)
        l = kwargs.get('l', [ ]) # l is a list, such as, guess_list or gender_list
        jsonf = kwargs.get('jsonf', 'files/names/csv2json.json')
        csv2names = self.csv2names(path=path, surnames=surnames, header=header)
        string = ""
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            if (header == True):
                next(sexreader, None)
            string = '['
            i = 0
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')

                middlename = row[1].replace(' ', '')
                middlename = row[1].replace('\"', '')

                lastname = row[2].title()
                lastname = row[2].replace('\"', '')

                gender = row[4]
                if surnames:
                    string = string + '{"name":"'+ name + ' ' + middlename +'", \n'
                else:
                    string = string + '{"name":"'+ name + '", \n'
                string = string + '"surname":"'+ lastname +'", \n'
                string = string + '"probability": 1, \n'
                if (l == [ ] ):
                    string = string + '"gender":"'+ gender +'"}, \n'
                elif (len(l) <= i + 1):
                    string = string + '"gender":"'+str(l[i])+'"} \n'
                else:
                    string = string + '"gender":"'+str(l[i])+'"}, \n'
                i = i + 1
            string = string + ']'
        file = open(jsonf, "w")
        file.writelines(str(string))
        file.close()


    def name2gender_in_dataset(self, name, dataset=''):
        guess = 2
        if (dataset == "names_es"):
            with open(dataset+"/"+"femeninos.txt") as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                for row in sexreader:
                    datasetname = row.title()
                    if (datasetname == name):
                        guess = 0
            with open(dataset+"/"+"masculinos.txt") as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                for row in sexreader:
                    datasetname = row.title()
                    if (datasetname == name):
                        guess = 1
        if (dataset == "files/names/nam_dict.txt"):
            cmd = 'grep -i "' + name
            cmd = cmd + ' " files/names/nam_dict.txt > files/logs/grep.tmp'
            os.system(cmd)
            results = [i for i in open('files/logs/grep.tmp', 'r').readlines()]
            for row in results:
                datasetname = row[1].title()
                if (datasetname == name):
                    guess = row[0].title()
                    if ((guess == 'F') | (guess == '?F')):
                        guess = 0
                    elif ((guess == 'M') | (guess == '?M')):
                        guess = 1
                    elif (guess == '='):
                        guess = 2
        if (dataset == "files/names/all.csv"):
            with open(dataset) as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                for row in sexreader:
                    datasetname = row[0].title()
                    if (datasetname == name):
                        guess = row[4]
                        if (guess == 'm'):
                            guess = 1
                        elif (guess == 'f'):
                            guess = 0
                        elif (guess == 'u'):
                            guess = 2
        if (dataset == "files/names/yob2017.txt"):
            with open(dataset) as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                for row in sexreader:
                    datasetname = row[0].title()
                    if (datasetname == name):
                        guess = row[1]
                        if (guess == 'M'):
                            guess = 1
                        elif (guess == 'F'):
                            guess = 0
        return guess

    def dataset2genderlist(self, dataset=''):
        genderlist = []
        path_all = "files/names/all.csv"
        path_allnoun = "files/names/allnoundefined.csv"
        if ((dataset == path_all) or (dataset == path_allnoun)):
            with open(dataset) as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                for row in sexreader:
                    datasetname = row[0].title()
                    guess = row[4]
                    guess = guess.replace('\"', '')
                    if (guess == 'm'):
                        guess = 1
                    elif (guess == 'f'):
                        guess = 0
                    elif (guess == 'u'):
                        guess = 2
                    genderlist.append(guess)
        if (dataset == "files/names/names_uk/orig/yob2017.txt"):
            with open(dataset) as csvfile:
                sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(sexreader, None)
                for row in sexreader:
                    datasetname = row[0].title()
                    guess = row[1]
                    guess = guess.replace('\"', '')
                    if (guess == 'M'):
                        guess = 1
                    elif (guess == 'F'):
                        guess = 0
                    genderlist.append(guess)
        return genderlist


    def name_frec(self, name, *args, **kwargs):
        # guess list method
        dataset = kwargs.get('dataset',"us")
        du = DameUtils()
        name = du.drop_accents(name)
        path_males = 'files/names/names_es/esmasculinos.csv'
        if ((dataset == 'ine') or (dataset == 'es')):
            path_males = 'files/names/names_es/esmasculinos.csv'
        elif (dataset == 'ie'):
            path_males = 'files/names/names_ie/iemales.csv'            
        elif (dataset == 'is'):
            path_males = 'files/names/names_is/ismales.csv'            
        elif (dataset == 'uy'):
            path_males = 'files/names/names_uy/uymasculinos.csv'
        elif (dataset == 'uk'):
            path_males = 'files/names/names_uk/ukmales.csv'
        elif ((dataset == 'us') or (dataset=='usa')):
            path_males = 'files/names/names_us/usmales.csv'
        elif (dataset == 'nz'):
            path_males = 'files/names/names_nz/nzmales.csv'            
        elif (dataset == 'ca'):
            path_males = 'files/names/names_ca/camales.csv'
        elif (dataset == 'fi'):
            path_males = 'files/names/names_fi/fimales.csv'            
        elif (dataset == 'au'):
            path_males = 'files/names/names_au/baby-names-1944-2013/aumales.csv'            
        elif (dataset == 'pt'):
            path_males = 'files/names/names_pt/ptmales.csv'            
            
        file_males = open(path_males, 'r')
        readerm = csv.reader(file_males, delimiter=',', quotechar='|')
        males = 0
        for row in readerm:
            if ((len(row) > 1) and (row[0].lower() == name.lower())):
                males = row[1]
                males = du.drop_dots(males)
        path_females = 'files/names/names_es/esfemeninos.csv'
        if ((dataset == 'ine') or (dataset == 'es')):
            path_females = 'files/names/names_es/esfemeninos.csv'
        elif (dataset == 'ie'):
            path_females = 'files/names/names_ie/iefemales.csv'
        elif (dataset == 'is'):
            path_females = 'files/names/names_is/isfemales.csv'                        
        elif (dataset == 'uy'):
            path_females = 'files/names/names_uy/uyfemeninos.csv'
        elif (dataset == 'uk'):
            path_females = 'files/names/names_uk/ukfemales.csv'
        elif ((dataset == 'us') or (dataset=='usa')):
            path_females = 'files/names/names_us/usfemales.csv'
        elif (dataset == 'nz'):
            path_females = 'files/names/names_nz/nzfemales.csv'            
        elif (dataset == 'ca'):
            path_females = 'files/names/names_ca/cafemales.csv'
        elif (dataset == 'fi'):
            path_females = 'files/names/names_fi/fifemales.csv'                        
        elif (dataset == 'au'):
            path_females = 'files/names/names_au/baby-names-1944-2013/aufemales.csv'            
        elif (dataset == 'pt'):
            path_females = 'files/names/names_pt/ptfemales.csv'            

        file_females = open(path_females, 'r')
        readerf = csv.reader(file_females, delimiter=',', quotechar='|')
        females = 0
        for row in readerf:
            if ((len(row) > 1) and (row[0].lower() == name.lower())):
                females = row[1]
                females = du.drop_dots(females)
        dicc = {"females": females, "males": males}
        return dicc

    def inesurname_province_and_frec(self, surname, *args, **kwargs):
        # guess list method
        province = kwargs.get('province', 'madrid')
        du = DameUtils()
        
        if (province == 'acorugna'):
            path_surnames = 'files/inesurnames/provincias/residencia/acorugna.csv'
        elif (province == 'alava'):
            path_surnames = 'files/inesurnames/provincias/residencia/alava.csv'            
        elif (province == 'albacete'):
            path_surnames = 'files/inesurnames/provincias/residencia/albacete.csv'
        elif (province == 'alicante'):
            path_surnames = 'files/inesurnames/provincias/residencia/alicante.csv'
        elif (province == 'almeria'):
            path_surnames = 'files/inesurnames/provincias/residencia/almeria.csv'
        elif (province == 'asturias'):
            path_surnames = 'files/inesurnames/provincias/residencia/asturias.csv'
        elif (province == 'avila'):
            path_surnames = 'files/inesurnames/provincias/residencia/avila.csv'
        elif (province == 'badajoz'):
            path_surnames = 'files/inesurnames/provincias/residencia/badajoz.csv'
        elif (province == 'baleares'):
            path_surnames = 'files/inesurnames/provincias/residencia/baleares.csv'
        elif (province == 'barcelona'):
            path_surnames = 'files/inesurnames/provincias/residencia/barcelona.csv'
        elif (province == 'bizkaia'):
            path_surnames = 'files/inesurnames/provincias/residencia/bizkaia.csv'
        elif (province == 'burgos'):
            path_surnames = 'files/inesurnames/provincias/residencia/burgos.csv'
        elif (province == 'caceres'):
            path_surnames = 'files/inesurnames/provincias/residencia/caceres.csv'
        elif (province == 'cadiz'):
            path_surnames = 'files/inesurnames/provincias/residencia/cadiz.csv'
        elif (province == 'cantabria'):
            path_surnames = 'files/inesurnames/provincias/residencia/cantabria.csv'
        elif (province == 'castellon'):
            path_surnames = 'files/inesurnames/provincias/residencia/castellon.csv'
        elif (province == 'ceuta'):
            path_surnames = 'files/inesurnames/provincias/residencia/ceuta.csv'
        elif (province == 'ciudadreal'):
            path_surnames = 'files/inesurnames/provincias/residencia/ciudadreal.csv'
        elif (province == 'cordoba'):
            path_surnames = 'files/inesurnames/provincias/residencia/cordoba.csv'
        elif (province == 'cuenca'):
            path_surnames = 'files/inesurnames/provincias/residencia/cuenca.csv'
        elif (province == 'girona'):
            path_surnames = 'files/inesurnames/provincias/residencia/girona.csv'
        elif (province == 'granada'):
            path_surnames = 'files/inesurnames/provincias/residencia/granada.csv'
        elif (province == 'guadalajara'):
            path_surnames = 'files/inesurnames/provincias/residencia/guadalajara.csv'
        elif (province == 'guipuzkoa'):
            path_surnames = 'files/inesurnames/provincias/residencia/guipuzkoa.csv'
        elif (province == 'huelva'):
            path_surnames = 'files/inesurnames/provincias/residencia/huelva.csv'
        elif (province == 'huesca'):
            path_surnames = 'files/inesurnames/provincias/residencia/huesca.csv'
        elif (province == 'jaen'):
            path_surnames = 'files/inesurnames/provincias/residencia/jaen.csv'
        elif (province == 'larioja'):
            path_surnames = 'files/inesurnames/provincias/residencia/larioja.csv'
        elif (province == 'leon'):
            path_surnames = 'files/inesurnames/provincias/residencia/leon.csv'
        elif (province == 'lleida'):
            path_surnames = 'files/inesurnames/provincias/residencia/lleida.csv'
        elif (province == 'lugo'):
            path_surnames = 'files/inesurnames/provincias/residencia/lugo.csv'
        elif (province == 'madrid'):
            path_surnames = 'files/inesurnames/provincias/residencia/madrid.csv'
        elif (province == 'malaga'):
            path_surnames = 'files/inesurnames/provincias/residencia/malaga.csv'
        elif (province == 'melilla'):
            path_surnames = 'files/inesurnames/provincias/residencia/melilla.csv'
        elif (province == 'murcia'):
            path_surnames = 'files/inesurnames/provincias/residencia/murcia.csv'
        elif (province == 'navarra'):
            path_surnames = 'files/inesurnames/provincias/residencia/navarra.csv'
        elif (province == 'ourense'):
            path_surnames = 'files/inesurnames/provincias/residencia/ourense.csv'
        elif (province == 'palencia'):
            path_surnames = 'files/inesurnames/provincias/residencia/palencia.csv'
        elif (province == 'palencia'):
            path_surnames = 'files/inesurnames/provincias/residencia/palencia.csv'
        elif (province == 'pontevedra'):
            path_surnames = 'files/inesurnames/provincias/residencia/pontevedra.csv'
        elif (province == 'salamanca'):
            path_surnames = 'files/inesurnames/provincias/residencia/salamanca.csv'
        elif (province == 'segovia'):
            path_surnames = 'files/inesurnames/provincias/residencia/segovia.csv'
        elif (province == 'sevilla'):
            path_surnames = 'files/inesurnames/provincias/residencia/sevilla.csv'
        elif (province == 'soria'):
            path_surnames = 'files/inesurnames/provincias/residencia/soria.csv'
        elif (province == 'tarragona'):
            path_surnames = 'files/inesurnames/provincias/residencia/tarragona.csv'
        elif (province == 'tenerife'):
            path_surnames = 'files/inesurnames/provincias/residencia/tenerife.csv'
        elif (province == 'teruel'):
            path_surnames = 'files/inesurnames/provincias/residencia/teruel.csv'
        elif (province == 'toledo'):
            path_surnames = 'files/inesurnames/provincias/residencia/toledo.csv'
        elif (province == 'valencia'):
            path_surnames = 'files/inesurnames/provincias/residencia/valencia.csv'
        elif (province == 'valladolid'):
            path_surnames = 'files/inesurnames/provincias/residencia/valladolid.csv'
        elif (province == 'zamora'):
            path_surnames = 'files/inesurnames/provincias/residencia/zamora.csv'
        elif (province == 'zaragoza'):
            path_surnames = 'files/inesurnames/provincias/residencia/zaragoza.csv'
        file_surnames = open(path_surnames, 'r')
        readerf = csv.reader(file_surnames, delimiter=',', quotechar='|')
        quantity = 0
        for row in readerf:
            if ((len(row) > 1) and (row[0].lower() == surname.lower())):
                aux = row[1]
                quantity = int(du.drop_dots(aux))
        return quantity

            
    
    def name_prob_countries(self, name):
        du = DameUtils()
        es = self.name_frec(name,dataset="es")
        ie = self.name_frec(name,dataset="ie")
        isl = self.name_frec(name,dataset="is")        
        uy = self.name_frec(name,dataset="uy")
        uk = self.name_frec(name,dataset="uk")
        us = self.name_frec(name,dataset="us")
        nz = self.name_frec(name,dataset="nz")
        ca = self.name_frec(name,dataset="ca")                                        
        fi = self.name_frec(name,dataset="fi")
        au = self.name_frec(name,dataset="au")
        pt = self.name_frec(name,dataset="pt")    
        females = int(es["females"]) + int(ie["females"]) + int(isl["females"]) + int(uy["females"]) + int(uk["females"]) + int(us["females"]) + int(nz["females"]) + int(ca["females"]) + int(fi["females"]) + int(au["females"]) + int(pt["females"])
        males = int(es["males"]) + int(ie["males"]) + int(isl["males"]) + int(uy["males"]) + int(uk["males"]) + int(us["males"])  + int(nz["males"]) + int(ca["males"]) + int(fi["males"]) + int(au["males"]) + int(pt["males"])

        prob_females = {"es": du.round_and_not_zero_division(int(es["females"]), int(females)), "ie": du.round_and_not_zero_division(int(ie["females"]), int(females)), "is": du.round_and_not_zero_division(int(isl["females"]), int(females)), "uy": du.round_and_not_zero_division(int(uy["females"]), int(females)), "uk": du.round_and_not_zero_division(int(uk["females"]), int(females)), "us": du.round_and_not_zero_division(int(us["females"]), int(females)), "nz": du.round_and_not_zero_division(int(nz["females"]), int(females)), "ca": du.round_and_not_zero_division(int(ca["females"]), int(females)), "fi": du.round_and_not_zero_division(int(fi["females"]), int(females)), "au": du.round_and_not_zero_division(int(au["females"]), int(females)), "pt": du.round_and_not_zero_division(int(pt["females"]), int(females))}
        
        prob_males = {"es": du.round_and_not_zero_division(int(es["males"]), int(males)), "ie": du.round_and_not_zero_division(int(ie["males"]), int(males)), "is": du.round_and_not_zero_division(int(isl["males"]), int(males)), "uy": du.round_and_not_zero_division(int(uy["males"]), int(males)), "uk": du.round_and_not_zero_division(int(uk["males"]), int(males)), "us": du.round_and_not_zero_division(int(us["males"]), int(males)), "nz": du.round_and_not_zero_division(int(nz["males"]), int(males)), "ca": du.round_and_not_zero_division(int(ca["males"]), int(males)), "fi": du.round_and_not_zero_division(int(fi["males"]), int(males)), "au": du.round_and_not_zero_division(int(au["males"]), int(males)), "pt": du.round_and_not_zero_division(int(pt["males"]), int(males))}

        prob = [{"females": prob_females, "males": prob_males}]
        
        return prob

    
    def namdict2file(self):
        filepath = 'files/names/nam_dict.txt'
        mylist = []
        with open(filepath) as fp:
            for cnt, line in enumerate(fp):
                # From 3 to 25
                if (cnt > 292):
                    name = ""
                    for i in range(3, 25):
                        name = name + str(line[i])
                    mylist += [name]
        file = open("files/names/nam_dict_list.txt", "w")
        file.writelines(mylist)
        file.close()

    def filenamdict2list(self):
        names = []
        dataset = 'files/names/nam_dict_list.txt'
        with open(dataset, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                names = names + row[0].split()
        return names

# GUESS #

    def guess(self, name, binary=False, *args, **kwargs):
        # guess list method
        dataset = kwargs.get('dataset', 'es')
        # guess method to check names dictionary
        guess = ''
        name = unidecode.unidecode(name).title()
        name.replace(name, "")
        dicc = self.name_frec(name, dataset=dataset)
        m = int(dicc['males'])
        f = int(dicc['females'])
        if ((m == 0) and (f == 0)):
            if binary:
                guess = 2
            else:
                guess = "unknown"
        elif (m > f):
            if binary:
                guess = 1
            else:
                guess = "male"
        elif (f > m):
            if binary:
                guess = 0
            else:
                guess = "female"
        else:
            if binary:
                guess = 2
            else:
                guess = "unknown"
        return guess

    def guess_surname(self, string, locale):
        counter = 0
        if (locale == "us"):
            path = 'files/names/names_us/surnames.csv'
            surname_position = 0
            counter_position = 2
        elif ((locale == "es") or (locale == "ine")):
            path = 'files/inesurnames/apellidos_frecuencia.csv'
            surname_position = 1
            counter_position = 2
        boolean = False
        with open(path) as csvfile:
            surnamereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(surnamereader, None)
            for row in surnamereader:
                surname = row[surname_position]
                if (surname.lower() == du.drop_accents(string.lower())):
                    boolean = True
                    counter = int(row[counter_position])
        return [boolean, counter]

    def string2gender(self, string):
        # TODO: take care with trash strings before the name
        du = DameUtils()
        arr = du.string2array(string)
        name = ""
        i = 0
        features_int = self.features_int(string)
        while ((name == "") and (len(arr) > i)):
            if (not(self.guess_surname(arr[i], locale="us")[0]) and (len(string) > 0)):
                name = arr[i]
            i = i + 1
        return self.guess(name)

    def guess_list(self, path='files/names/partial.csv', binary=False, *args, **kwargs):
        # guess list method
        header = kwargs.get('header', True)
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            if (header == True):
                next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                slist.append(self.guess(name, binary))
        return slist

    def gender_list(self, path, *args, **kwargs):
        # counting males, females and unknown
        header = kwargs.get('header', True)
        glist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            if (header == True):
                next(sexreader, None)
            count_females = 0
            count_males = 0
            count_unknown = 0
            gender = ""
            for row in sexreader:
                if (row[4] != ""):
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


    def pretty_gg_list(self, path, jsonf, *args, **kwargs):
        measure = kwargs.get('measure', 'accuracy')
        binary = kwargs.get('binary', True)
        ml = kwargs.get('ml', 'nltk')
        api = kwargs.get('api', 'damegender')
        header = kwargs.get('header', True)
        gl = self.gender_list(path=path)

        if (os.path.isfile(jsonf)):
            if (self.json_eq_csv_in_names(jsonf=jsonf, path=path)):
                print("################### "+ api +"!!")
                print("Gender list: " + str(gl))
                sl = self.json2guess_list(jsonf=jsonf, binary=True)
                print("Guess list:  " +str(sl))
                dst.print_measures(gl, sl, measure, api)
            else:
                print("Names in json and csv are differents")
                print("%s names in csv" % len(self.csv2names(path=path, header=header)))
                print("%s names in json" % len(self.json2names(jsonf=jsonf, surnames=False)))
                v = self.first_uneq_json_and_csv_in_names(jsonf=jsonf, path=path)
                print("The first position finding unmatched names is %s and the name is %s" % (v[1], v[0]))
                print("Names in csv: %s:" % self.csv2names(path=path, header=header))
                print("Names in json: %s:" % self.json2names(jsonf=jsonf, surnames=False))
        else:
            print("In the path %s doesn't exist file" % jsonf)
            print("You can create one with:")
            print("$ python3 damegender2json.py --csv=%s --ml=%s --jsonoutput=files/names/partial.csv.%s.json" % (path, ml, ml))
        return 1

    def pretty_cm(self, path, jsonf, *args, **kwargs):
        api = kwargs.get('api', 'damegender')
        reverse = kwargs.get('reverse', False)
        dimensions = kwargs.get('dimensions', '3x2')
        gl = self.gender_list(path=path)
        print("%s confusion matrix:\n" % api)
#        self.print_confusion_matrix_gender(path=path, dimensions=dimensions)
        if (os.path.isfile(jsonf)):
            self.print_confusion_matrix_gender(path=path, dimensions=dimensions, jsonf=jsonf, reverse=reverse)
        elif (args.jsondownloaded == ''):
            self.print_confusion_matrix_gender(path=path, dimensions=dimensions, reverse=reverse)
        else:
            print("In the path %s doesn't exist file" % jsonf)


    def json2guess_list(self, jsonf="", binary=False):
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        guesslist = []

        for i in json_object:
            if binary:
                if ((i['gender'] == 'female') or (i['gender'] == 'f') or (i['gender'] == 0)):
                    guesslist.append(0)
                elif ((i['gender'] == 'male') or (i['gender'] == 'm') or (i['gender'] == 1)):
                    guesslist.append(1)
                else:
                    guesslist.append(2)
            else:
                guesslist.append(i['gender'])
        return guesslist


    def json2names(self, jsonf="", surnames=False):
        jsondata = open(jsonf).read()
        json_object = json.loads(jsondata)
        nameslist = []
        for i in json_object:
            if (i["name"] != ''):
                if (surnames == True):
                    nameslist.append([i["name"], i["surname"]])
                else:
                    nameslist.append(i["name"])
        return nameslist


    def json_eq_csv_in_names(self, jsonf="", path="", *args, **kwargs):
        header = kwargs.get('header', True)
        boolean = False
        json = self.json2names(jsonf=jsonf, surnames=False)
        json_lower = [element.lower() for element in json] ; json
        csv = self.csv2names(path=path, header=header)
        csv_lower = [element.lower() for element in csv] ; csv
        count = 0
        i = 0
        maxi = len(json_lower) -1
        if (maxi < len(csv_lower)):
            maxi = len(csv_lower) -1
        while (maxi > i):
            if (json_lower[i] == csv_lower[i]):
                count = count +1
            i = i+1
        boolean = ((len(json_lower) == len(csv_lower)) and ((len(json_lower) -1) == count))
        return boolean

    def first_uneq_json_and_csv_in_names(self, jsonf="", path="", *args, **kwargs):
        header = kwargs.get('header', True)
        json = self.json2names(jsonf=jsonf, surnames=False)
        csv = self.csv2names(path=path, header=header)
        i = 0
        maxi_json = len(json) -1
        maxi_csv = len(csv) - 1
        while ((i < maxi_json) and (i < maxi_csv) and (json[i].lower() == csv[i].lower())):
            i = i + 1
        ret = json[i].lower()
        if ((i > maxi_json) and (i > maxi_csv)):
            ret = ""
        elif (i > maxi_json):
            ret = csv[i].lower()
        elif (i > maxi_csv):
            ret = json[i].lower()
        return [ret, i]

    def accuracy(self, path):
        gl = self.gender_list(path)
        sl = self.guess_list(path, binary=True)
        return self.accuracy_score_dame(gl, sl)

    def confusion_matrix_gender(self, path='', jsonf=''):
        # this method is an interfaz to confusion_matrix_table allowing introduce a json file
        # in dame_sexmachine we must rewrite it to allow machine learning algorithm
        truevector = self.gender_list(path)
        if (os.path.isfile(jsonf)):
            guessvector = self.json2guess_list(jsonf=jsonf, binary=True)
        else:
            guessvector = self.guess_list(path, binary=True)
        res = dst.confusion_matrix_table(truevector, guessvector)
        return res

    def print_confusion_matrix_gender(self, path='', dimensions='', *args, **kwargs):
        reverse = kwargs.get('reverse', False)
        jsonf = kwargs.get('jsonf', '')
        jf = os.getcwd() + "/" +  jsonf
        if (os.path.isfile(jf)):
            cmd = self.confusion_matrix_gender(path, jsonf=jf)
        else:
            cmd = self.confusion_matrix_gender(path)
        if (dimensions == "1x1"):
            if (reverse == False):
                print("      M    ")                
                print("M  [[ %s ]]" % (cmd[1][1]))
            elif (reverse == True):
                print("      F    ")
                print("F  [[ %s ]]" % (cmd[0][0]))
        elif (dimensions == "1x2"):
            if (reverse == False):
                print("      M    F   ")
                print("M  [[ %s,   %s ]]" % (cmd[1][1], cmd[1][0]))
            elif (reverse == True):
                print("      F    M   ")                
                print("F  [[ %s,   %s ]]" % (cmd[0][0], cmd[0][1]))
        elif (dimensions == "1x3"):
            if (reverse == False):
                print("      M    F   U   ")                
                print("M  [[ %s, %s, %s ]]" % (cmd[1][1], cmd[1][0], cmd[1][2]))
            elif (reverse == True):
                print("     F  M  U   ")                                
                print("F [[ %s, %s, %s ]]" % (cmd[0][0], cmd[0][1], cmd[0][2]))
        elif (dimensions == "2x1"):
            if (reverse == False):
                print("      M  ")
                print("M  [[ %s ]" % (cmd[1][1]))
                print("F   [ %s ]]" % (cmd[1][0]))
            elif (reverse == True):
                print("      F   ")
                print("F  [[ %s ] " % (cmd[0][0]))
                print("M   [ %s ]]" % (cmd[0][1]))
        elif (dimensions == "2x2"):
            if (reverse == False):
                print("      M    F  ")
                print("M  [[ %s , %s ]" % (cmd[1][1], cmd[1][0]))
                print("F   [ %s , %s ]]" % (cmd[0][1], cmd[0][0]))
            if (reverse == True):
                print("      F   M  ")
                print("F  [[ %s , %s ]" % (cmd[0][0], cmd[0][1]))
                print("M   [ %s , %s ]]" % (cmd[1][0], cmd[1][1]))
        elif (dimensions == "2x3"):
            if (reverse == False):
                print("      M   F   U  ")
                print("M  [[ %s,  %s,  %s ]" % (cmd[1][1], cmd[1][0], cmd[1][2]))
                print("F   [ %s,  %s,  %s ]]" % (cmd[0][1], cmd[0][0], cmd[0][2]))
            if (reverse == True):
                print("      F   M   U  ")
                print("F  [[ %s,  %s,  %s ]" % (cmd[0][0], cmd[0][1], cmd[0][2]))
                print("M   [ %s,  %s,  %s ]]" % (cmd[1][0], cmd[1][1], cmd[1][2]))
        elif (dimensions == "3x1"):
            if (reverse == False):
                print("       M   ")
                print("M  [[ %s ]" % (cmd[1][1]))
                print("F   [ %s ]" % (cmd[0][1]))
                print("U   [ %s ]]" % (cmd[2][1]))
            elif (reverse == True):
                print("       F   ")                
                print("F   [[ %s ]" % (cmd[0][0]))
                print("M    [ %s ]" % (cmd[1][0]))
                print("U    [ %s ]]" % (cmd[2][0]))
        elif (dimensions == "3x2"):
            if (reverse == False):
                print("      M    F  ")
                print("M  [[ %s ,  %s ]" % (cmd[1][1], cmd[1][0]))
                print("F   [ %s ,  %s ]" % (cmd[0][1], cmd[0][0]))
                print("U   [ %s ,  %s ]]" % (cmd[2][1], cmd[2][0]))
            if (reverse == True):
                print("      F   M  ")                
                print("F  [[ %s,  %s ]" % (cmd[0][0], cmd[0][1]))
                print("M   [ %s,  %s ]" % (cmd[1][0], cmd[1][1]))
                print("U   [ %s,  %s ]]" % (cmd[2][0], cmd[2][1]))
        elif (dimensions == "3x3"):
            if (reverse == False):
                print("      M  F  U   ")
                print("M  [[ %s, %s, %s ]" % (cmd[1][1], cmd[1][0], cmd[1][2]))
                print("F   [ %s, %s, %s ]" % (cmd[0][1], cmd[0][0], cmd[0][2]))
                print("U   [ %s, %s, %s ]]" % (cmd[2][1], cmd[2][0], cmd[2][2]))
            if (reverse == True):
                print("      F   M   U   ")
                print("F  [[ %s, %s, %s ]" % (cmd[0][0], cmd[0][1], cmd[0][2]))
                print("M   [ %s, %s, %s ]" % (cmd[1][0], cmd[1][1], cmd[1][2]))
                print("U   [ %s, %s, %s ]]" % (cmd[2][0], cmd[2][1], cmd[2][2]))
        return ""
    
