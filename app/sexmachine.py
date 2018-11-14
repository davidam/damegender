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
# from perceval.backends.core.mbox import MBox
# from perceval.backends.core.git import Git
from nltk.corpus import names
import csv
import nltk
import re
#from app.gendergit import GenderGit
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn import svm
import pdb
from pprint import pprint


class Sexmachine(object):

    def string2array(self, string):
        res = ""
        if re.search(r' ', string):
            res = re.sub(r' +', ' ', string)
        array = res.split(' ')
        return array

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
    # NLTK bayesian classifier
        labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                         [(name, 'female') for name in names.words('female.txt')])
        featuresets = [(self.features(n), gender) for (n, gender) in labeled_names]
        train_set, test_set = featuresets[500:], featuresets[:500]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        return classifier

    def svc(self):
    # Scikit classifier
        X = np.array(self.features_list(all=True))
        y = self.gender_list(all=True)
        clf = svm.SVC()
        clf.fit(X, y)
        return clf

    def sgd(self):
    # Scikit classifier
        X = np.array(self.features_list(all=True))
        y = self.gender_list(all=True)
        clf = SGDClassifier(loss="log").fit(X,y)
        return clf

    def gaussianNB(self):
    # Scikit bayesian classifier
        x = np.array(self.features_list(all=True))
        y = np.array(self.gender_list(all=True))
        #Create a Gaussian Classifier
        model = GaussianNB()
        # Train the model using the training sets
        model.fit(x, y)
        return model

    def multinomialNB(self):
    # Scikit bayesian classifier
        X = np.array(self.features_list(all=True))
        y = np.array(self.gender_list(all=True))
        model = MultinomialNB()
        model.fit(X, y)
        return model

    def bernoulliNB(self):
    # Scikit bayesian classifier
        X = np.array(self.features_list(all=True))
        y = np.array(self.gender_list(all=True))
        model = BernouilliNB()
        model.fit(X, y)
        return model

    def guess(self, name):
    # guess method to check names dictionary and nltk classifier
        guess = ''
        if name in names.words('male.txt'):
            guess = 'male'
        elif name in names.words('female.txt'):
            guess = 'female'
        else:
            classifier = self.classifier()
            guess = classifier.classify(self.features(name))
        return guess

    def guess_list(self, all=False):
        slist = []
        if all:
            path = 'files/all.csv'
        else:
            path = 'files/partial.csv'
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                slist.append((name, self.guess(name)))
        return slist

    def features_list(self, all=False):
        flist = []
        if all:
            path = 'files/all.csv'
        else:
            path = 'files/partial.csv'
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                flist.append(list(self.features_int(name).values()))
        return flist

    def gender_list(self, all=False):
        glist = []
        if all:
            path = 'files/all.csv'
        else:
            path = 'files/partial.csv'
        with open(path) as csvfile:
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
    # Extracting females with perceval
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
    # Extracting males with perceval
        gg = GenderGit()
        r = gg.repo("https://github.com/grimoirelab/perceval.git", "/tmp/clonedir")
        count = 0
        for user in r.fetch():
            name = gg.removeMail(user['data']['Author'])
            sm = self.guess(name)
            if (sm == 'male'):
                count = count + 1
        return count
