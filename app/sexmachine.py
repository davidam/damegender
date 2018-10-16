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
from app.gendergit import GenderGit

class Sexmachine(object):
    def features(self, name):
        features = {}
        features["first_letter"] = name[0].lower()
        features["last_letter"] = name[-1].lower()
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features["count({})".format(letter)] = name.lower().count(letter)
            features["has({})".format(letter)] = (letter in name.lower())
        return features

    def featuresint(self, name):
        featuresint = {}
        featuresint["first_letter"] = ord(name[0].lower())
        featuresint["last_letter"] = ord(name[-1].lower())
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            featuresint["count({})".format(letter)] = name.lower().count(letter)
        featuresint["vocals"] = 0
        for letter in 'aeiou':
            featuresint["vocals"] = featuresint["vocals"] + 1
        featuresint["consonants"] = 0
        for letter in 'bcdfghjklmnpqrstvwxyz':
            featuresint["consonants"] = featuresint["consonants"] + 1
        if (chr(featuresint["first_letter"]) in 'aeiou'):
            featuresint["first_letter_vocal"] = 1
        else:
            featuresint["first_letter_vocal"] = 0
        if (chr(featuresint["last_letter"]) in 'aeiou'):
            featuresint["last_letter_vocal"] = 1
        else:
            featuresint["last_letter_vocal"] = 0
        return featuresint

    #["count({})".format(letter)] = name.lower().count(letter)
    # número de vocales y consonantes
    # vocales seguidas
    # empieza por vocal o consonante
    # k-fold

    # TODO: Reescribir el clasificador
    def classifier(self):
        labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                         [(name, 'female') for name in names.words('female.txt')])
        featuresets = [(self.features(n), gender) for (n, gender) in labeled_names]
        train_set, test_set = featuresets[500:], featuresets[:500]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        return classifier
#        return classifier.classify(self.features(name))


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

    def list(self):
        slist = []
        with open('files/partial.csv') as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0]
                slist.append((name, self.guess(name)))
        return slist

    def numFemales(self, url, directory):
        gg = GenderGit()
        r = gg.repo("https://github.com/grimoirelab/perceval.git", "/tmp/clonedir")
        count = 0
        for user in r.fetch():
            name = gg.removeMail(user['data']['Author'])
            sm = self.guess(name)
            if (sm == 'female'):
                count = count + 1
        return count

    def numMales(self, url, directory):
        gg = GenderGit()
        r = gg.repo("https://github.com/grimoirelab/perceval.git", "/tmp/clonedir")
        count = 0
        for user in r.fetch():
            name = gg.removeMail(user['data']['Author'])
            sm = self.guess(name)
            if (sm == 'male'):
                count = count + 1
        return count
