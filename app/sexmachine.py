#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: David Arroyo Menéndez.
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

from pprint import pprint
from perceval.backends.core.mbox import MBox
from perceval.backends.core.git import Git
from nltk.corpus import names
import csv
import nltk
import re
#from app.gendergit import GenderGit
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import pdb
from pprint import pprint

class Sexmachine(object):
    def features(self, name):
        features = {}
        features["first_letter"] = name[0].lower()
        features["last_letter"] = name[-1].lower()
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features["count({})".format(letter)] = name.lower().count(letter)
            features["has({})".format(letter)] = (letter in name.lower())
        return features

    def features_int(self, name):
        features_int = {}
        features_int["first_letter"] = ord(name[0].lower())
        features_int["last_letter"] = ord(name[-1].lower())
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features_int["count({})".format(letter)] = name.lower().count(letter)
        features_int["vocals"] = 0
        for letter in 'aeiou':
            features_int["vocals"] = features_int["vocals"] + 1
        features_int["consonants"] = 0
        for letter in 'bcdfghjklmnpqrstvwxyz':
            features_int["consonants"] = features_int["consonants"] + 1
        if (chr(features_int["first_letter"]) in 'aeiou'):
            features_int["first_letter_vocal"] = 1
        else:
            features_int["first_letter_vocal"] = 0
        if (chr(features_int["last_letter"]) in 'aeiou'):
            features_int["last_letter_vocal"] = 1
        else:
            features_int["last_letter_vocal"] = 0
        return features_int

    # TODO: Reescribir el clasificador
    def classifier(self):
        labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                         [(name, 'female') for name in names.words('female.txt')])
        featuresets = [(self.features(n), gender) for (n, gender) in labeled_names]
        train_set, test_set = featuresets[500:], featuresets[:500]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        return classifier

    def gaussianNB(self):
        x = np.array(self.features_list())
        y = np.array(self.gender_list())
        #Create a Gaussian Classifier
        model = GaussianNB()
        # Train the model using the training sets
        model.fit(x, y)
        return model

    def multinomialNB(self):
        X = np.array(self.features_list())
        y = np.array(self.gender_list())
        model = MultinomialNB()
        model.fit(X, y)
        return model

    def guess(self, name):
        guess = ''
        if name in names.words('male.txt'):
            guess = 'male'
        elif name in names.words('female.txt'):
            guess = 'female'
        else:
            classifier = self.classifier()
            guess = classifier.classify(self.features(name))
        return guess

    # TODO: renombrar a guess_list
    def list(self):
        slist = []
        with open('files/partial.csv') as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                slist.append((name, self.guess(name)))
        return slist

    def features_list(self):
        flist = []
        with open('files/partial.csv') as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                flist.append(list(self.features_int(name).values()))
        return flist

    def gender_list(self):
        glist = []
        with open('files/partial.csv') as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(sexreader, None)
            for row in sexreader:
                gender = row[4]
                if (gender == 'f'):
                    g = 0
                elif (gender == 'm'):
                    g = 1
                else:
                    g = 2
                glist.append(g)
        return glist

    def num_females(self, url, directory):
        gg = GenderGit()
        r = gg.repo("https://github.com/grimoirelab/perceval.git", "/tmp/clonedir")
        count = 0
        for user in r.fetch():
            name = gg.removeMail(user['data']['Author'])
            sm = self.guess(name)
            if (sm == 'female'):
                count = count + 1
        return count

    def num_males(self, url, directory):
        gg = GenderGit()
        r = gg.repo("https://github.com/grimoirelab/perceval.git", "/tmp/clonedir")
        count = 0
        for user in r.fetch():
            name = gg.removeMail(user['data']['Author'])
            sm = self.guess(name)
            if (sm == 'male'):
                count = count + 1
        return count


# s = Sexmachine()
# m = s.multinomial_NB()
# array = [[ 0,  0,  1,  0, 21,  0,  0,  0,  0, 34,  2,  0,  0,  0,  0,  0,
#            0,  0,  0,  5,  0,  0,  0,  0,  0,  2,  0,  0,  0, 34,  1,  0],
#          [ 0,  0,  0,  0, 21,  0,  0,  0,  0, 34,  0,  0,  0,  0,  0,  1,
#            0,  0,  0,  5,  0,  0,  1,  0,  0,  1,  0,  0,  1, 34,  0,  0]]
# predicted= m.predict(array)
# print(predicted)
# n = np.array([1, 1])
