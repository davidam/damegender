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
import nltk
import csv
import hyphen
import unidecode
import unicodedata
import numpy as np

from collections import OrderedDict
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


class Gender(object):
# That's the root class in the heritage, apis classes and sexmachine is inheriting from gender
    def __init__(self):
        self.males = 0
        self.females = 0
        self.unknown = 0

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
            features_int["count({})".format(letter)] = name.lower().count(letter)
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
        if (name[0].lower() in 'aeiou'):
            features_int["first_letter_vocal"] = 1
        else:
            features_int["first_letter_vocal"] = 0
        if (name[0].lower() in 'bcdfghjklmnpqrstvwxyz'):
            features_int["first_letter_consonant"] = 1
        else:
            features_int["first_letter_consonant"] = 0
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
        return features_int

    def remove_accents(self, s):
        aux = ""
        for c in unicodedata.normalize('NFD', s):
            if (unicodedata.category(c) != 'Mn'):
                aux = aux + c
        return aux

    def males_list(self):
        my_corpus = nltk.corpus.PlaintextCorpusReader('/home/davidam/git/damegender/files/names_es', '.*\.txt')
        m = names.words('male.txt') + my_corpus.sents('masculinos.txt')[1]
        m = list(OrderedDict.fromkeys(m))
        return m

    def females_list(self):
        my_corpus = nltk.corpus.PlaintextCorpusReader('/home/davidam/git/damegender/files/names_es', '.*\.txt')
        f = names.words('female.txt') + my_corpus.sents('femeninos.txt')[1]
        f = list(OrderedDict.fromkeys(f))
        return f

    def guess(self, name, binary=False):
    # guess method to check names dictionary
        guess = ''
        name = unidecode.unidecode(name).title()
        name.replace(name,"")
        m = self.males_list()
        f = self.females_list()
        if (name in m) and (name in f):
            if binary:
                guess = 2
            else:
                guess = 'unknown'
        elif name in m:
            if binary:
                guess = 1
            else:
                guess = 'male'
        elif name in f:
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

    def csv2names(self, path='files/partial.csv'):
    # make a list from a csv file
        csvlist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"','')
                csvlist.append(name)
        return csvlist

    def guess_list(self, path='files/partial.csv', binary=False):
    # guess list method
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"','')
                if binary:
                    slist.append(self.guess(name, binary=True))
                else:
                    slist.append(self.guess(name, binary=False))
        return slist


    def gender_list(self, path='files/partial.csv'):
    # counting males, females and unknown
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

    def accuracy(self, path):
        gl = self.gender_list(path)
        sl = self.guess_list(path, binary=True)
        return accuracy_score(gl, sl)

    def confusion_matrix(self, path='files/partial.csv'):
        gl = self.gender_list(path)
        sl = self.guess_list(path,binary=True)
        return confusion_matrix(gl, sl)

    def features_list(self, path='files/partial.csv'):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            features_list_file = open('files/features_list.csv','w')
            for row in sexreader:
                name = row[0]
                flist.append(list(self.features_int(name).values()))
                features_list_file.write(str(list(self.features_int(name).values())))
        return flist

    def features_list_categorical(self, path='files/partial.csv'):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                flist.append([self.features_int(name)["first_letter"], self.features_int(name)["last_letter"], self.features_int(name)["last_letter_a"], self.features_int(name)["first_letter_vocal"], self.features_int(name)["last_letter_vocal"], self.features_int(name)["last_letter_consonant"]])
        return flist
                                                                                                            
    def features_list_no_categorical(self, path='files/partial.csv'):
        flist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                l = list([self.features_int(name)["count(a)"], self.features_int(name)["count(b)"], self.features_int(name)["count(c)"], self.features_int(name)["count(d)"], self.features_int(name)["count(e)"], self.features_int(name)["count(f)"], self.features_int(name)["count(g)"], self.features_int(name)["count(h)"], self.features_int(name)["count(i)"], self.features_int(name)["count(j)"], self.features_int(name)["count(h)"], self.features_int(name)["count(i)"], self.features_int(name)["count(j)"], self.features_int(name)["count(k)"], self.features_int(name)["count(l)"], self.features_int(name)["count(m)"], self.features_int(name)["count(n)"], self.features_int(name)["count(o)"], self.features_int(name)["count(p)"], self.features_int(name)["count(q)"], self.features_int(name)["count(r)"], self.features_int(name)["count(s)"], self.features_int(name)["count(t)"], self.features_int(name)["count(u)"], self.features_int(name)["count(w)"], self.features_int(name)["count(x)"], self.features_int(name)["count(y)"], self.features_int(name)["count(z)"], self.features_int(name)["vocals"], self.features_int(name)["consonants"]])
                flist.append(l)
        return flist

    def features_list2csv(self):
        fl = self.features_list()
        f = open('files/features_list.csv', 'w')
        first_line = "first_letter, last_letter, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, vocals, consonants, first_letter, first_letter_vocal, last_letter_vocal, last_letter_consonant, last_letter_a"
        f.write(first_line+"\n")
        for i in fl:
            line = ""
            count = 0
            while (count < (len(i) -1)):
                line = line + str(i[count]) + ", "
                count = count + 1
            f.write(line+str(i[count])+"\n")
        f.close()


# g = Gender()
# print(g.confusion_matrix())
# am = np.array([[2, 1, 0],[0, 14, 2],[0, 0, 2]])
# print(am)

# g = Gender()
# print(g.accuracy(path='files/partial.csv'))
