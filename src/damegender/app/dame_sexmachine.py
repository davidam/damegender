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

from pprint import pprint
#from nltk.corpus import names
import json
import os
import csv
import nltk
import re
import unidecode
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree
from sklearn.neural_network import MLPClassifier

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
#from xgboost import XGBClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pickle
from app.dame_gender import Gender
from app.dame_utils import DameUtils
from app.dame_statistics import DameStatistics

class DameSexmachine(Gender):
    def __init__(self):
        self.males = 0
        self.females = 0
        self.unknown = 0
        self.ds = DameStatistics()
        
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
            n = name.lower().count(letter)
            features_int["count({})".format(letter)] = n
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
        # h = hyphen.Hyphenator('en_US')
        # features_int["syllables"] = len(h.syllables(name))
        if (ord(name[-1].lower()) == "a"):
            features_int["last_letter_a"] = 1
        else:
            features_int["last_letter_a"] = 0
        return features_int

    def classifier(self, locale='us'):
        # NLTK bayesian classifier

        labeled_names = []
#        for name in names.words('male.txt'):
        for name in self.males_list(locale):
            elem = [(name, 'male')]
            labeled_names = labeled_names + elem

#        for name in names.words('female.txt'):
        for name in self.females_list(locale):
            elem = [(name, 'female')]
            labeled_names = labeled_names + elem

        featuresets = [(self.features(n), gender) for (n, gender) in
                       labeled_names]
        train_set, test_set = featuresets[500:], featuresets[:500]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        filename = 'files/datamodels/nltk_model.sav'
        pickle.dump(classifier, open(filename, 'wb'))
        return classifier

    def classifier_load(self):
        pkl_file = open('files/datamodels/nltk_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def adaboost(self):
        X = np.array(self.ds.features_list(path="files/names/all.csv"))
        y = self.gender_list(path="files/names/all.csv")
        clf = AdaBoostClassifier(n_estimators=100)
        clf.fit(X, y)
        filename = 'files/datamodels/adaboost_model.sav'
        pickle.dump(clf, open(filename, 'wb'))
        return clf

    def adaboost_load(self):
        pkl_file = open('files/datamodels/adaboost_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def svc(self):
        # Scikit svc classifier
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = self.gender_list(path="files/names/all.csv")
        clf = svm.SVC()
        clf.fit(X, y)
        filename = 'files/datamodels/svc_model.sav'
        pickle.dump(clf, open(filename, 'wb'))
        return clf

    def svc_load(self):
        pkl_file = open('files/datamodels/svc_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def sgd(self):
        # Scikit classifier
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = self.gender_list("files/names/all.csv")
        clf = SGDClassifier(loss="log").fit(X, y)
        filename = 'files/datamodels/sgd_model.sav'
        pickle.dump(clf, open(filename, 'wb'))
        return clf

    def sgd_load(self):
        pkl_file = open('files/datamodels/sgd_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def gaussianNB(self):
        # Scikit bayesian classifier
        x = np.array(self.features_list(path="files/names/all.csv"))
        y = np.array(self.gender_list(path="files/names/all.csv"))
        # Create a Gaussian Classifier
        model = GaussianNB()
        # Train the model using the training sets
        model.fit(x, y)
        filename = 'files/datamodels/gaussianNB_model.sav'
        pickle.dump(model, open(filename, 'wb'))
        return model

    def gaussianNB_load(self):
        pkl_file = open('files/datamodels/gaussianNB_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def multinomialNB(self):
        # Scikit bayesian classifier
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = np.array(self.gender_list(path="files/names/all.csv"))
        model = MultinomialNB()
        model.fit(X, y)
        filename = 'files/datamodels/multinomialNB_model.sav'
        pickle.dump(model, open(filename, 'wb'))
        return model

    def multinomialNB_load(self):
        pkl_file = open('files/datamodels/multinomialNB_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def bernoulliNB(self):
        # Scikit bayesian classifier
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = np.array(self.gender_list(path="files/names/all.csv"))
        model = BernoulliNB()
        model.fit(X, y)
        filename = 'files/datamodels/bernoulliNB_model.sav'
        pickle.dump(model, open(filename, 'wb'))
        return model

    def bernoulliNB_load(self):
        pkl_file = open('files/datamodels/bernoulliNB_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def forest(self):
        # Scikit forest classifier
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = np.array(self.gender_list(path="files/names/all.csv"))
        X, y = make_classification(n_samples=7000,
                                   n_features=33,
                                   n_informative=33,
                                   n_redundant=0,
                                   random_state=0,
                                   shuffle=False)
        rf = RandomForestRegressor(n_estimators=20, random_state=0)
        rf.fit(X, y)
        filename = 'files/datamodels/forest_model.sav'
        pickle.dump(rf, open(filename, 'wb'))
        return rf

    def forest_load(self):
        pkl_file = open('files/datamodels/forest_model.sav', 'rb')
        clf = pickle.load(pkl_file)
        pkl_file.close()
        return clf

    def tree(self):
        # Scikit forest classifier
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = np.array(self.gender_list(path="files/names/all.csv"))
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, y)
        filename = 'files/datamodels/tree_model.sav'
        pickle.dump(clf, open(filename, 'wb'))
        return clf

    def tree_load(self):
        clf_file = open('files/datamodels/tree_model.sav', 'rb')
        clf = pickle.load(clf_file)
        clf_file.close()
        return clf

    def mlp(self):
        X = np.array(self.features_list(path="files/names/all.csv"))
        y = np.array(self.gender_list(path="files/names/all.csv"))
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
        clf.fit(X, y)
        filename = 'files/datamodels/mlp_model.sav'
        pickle.dump(clf, open(filename, 'wb'))
        return clf

    def mlp_load(self):
        clf_file = open('files/datamodels/mlp_model.sav', 'rb')
        clf = pickle.load(clf_file)
        clf_file.close()
        return clf

    # def xgboost(self):
    #     # Scikit xgboost classifier
    #     X = np.array(self.features_list(path="files/names/all.csv"))
    #     y = np.array(self.gender_list(path="files/names/all.csv"))
    #     model = XGBClassifier()
    #     model.fit(X, y)
    #     filename = 'files/datamodels/xgboost_model.sav'
    #     pickle.dump(model, open(filename, 'wb'))
    #     return model

    # def xgboost_load(self):
    #     pkl_file = open('files/datamodels/xgboost_model.sav', 'rb')
    #     clf = pickle.load(pkl_file)
    #     pkl_file.close()
    #     return clf

    def guess(self, name, binary=False, ml="nltk"):
        # guess method to check names dictionary and nltk classifier
        guess = 2
        guess = super().guess(name, binary)
        vector = self.features_int(name)
        if ((guess == 'unknown') | (guess == 2)):
            classifier = self.classifier()
            vector = list(self.features_int(name).values())
            if (ml == "nltk"):
                guess = classifier.classify(self.features(name))
            elif (ml == "svc"):
                m = self.svc_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            elif (ml == "sgd"):
                m = self.sgd_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            elif (ml == "gaussianNB"):
                m = self.gaussianNB_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            elif (ml == "multinomialNB"):
                m = self.multinomialNB_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            elif (ml == "bernoulliNB"):
                m = self.bernoulliNB_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            elif (ml == "forest"):
                m = self.forest_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            # elif (ml == "xgboost"):
            #     m = s.xgboost_load()
            #     predicted = m.predict([vector])
            #     guess = predicted[0]
            elif (ml == "tree"):
                m = self.tree_load()
                predicted = m.predict([vector])
                guess = predicted[0]
            elif (ml == "mlp"):
                m = self.mlp_load()
                predicted = m.predict([vector])
                guess = predicted[0]

            if binary:
                if (guess == 'female'):
                    guess = 0
                elif (guess == 'male'):
                    guess = 1
                elif (guess == 'unkwnon'):
                    guess = 2
            else:
                if (guess == 0):
                    guess = 'female'
                elif (guess == 1):
                    guess = 'male'
                elif (guess == 2):
                    guess = 'unknown'
        return guess

    def guess_list(self, path='files/names/partial.csv',
                   binary=False, ml="nltk"):
        # guess list method
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                slist.append(self.guess(name, binary, ml=ml))
        return slist

    def confusion_matrix_gender(self, path='', jsonf='', ml='nltk'):
        # this method is an interfaz to confusion_matrix_table allowing introduce a json file
        # in dame_sexmachine we must rewrite it to allow machine learning algorithm
        truevector = self.gender_list(path)
        if (os.path.isfile(jsonf)):
            guessvector = self.json2guess_list(jsonf=jsonf, binary=True)
        else:
            guessvector = self.guess_list(path,
                                          binary=True,
                                          ml=ml)

        res = self.ds.confusion_matrix_table(truevector, guessvector)
        return res


    def num_females(self, url, directory):
        # Extracting females with perceval
        gg = GenderGit()
        r = gg.repo("https://github.com/grimoirelab/perceval.git",
                    "/tmp/clonedir")
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
        r = gg.repo("https://github.com/grimoirelab/perceval.git",
                    "/tmp/clonedir")
        count = 0
        for user in r.fetch():
            name = gg.removeMail(user['data']['Author'])
            sm = self.guess(name)
            if (sm == 'male'):
                count = count + 1
        return count
