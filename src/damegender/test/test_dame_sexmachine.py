#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import unittest
import numpy as np
import pickle
import os.path

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
#from xgboost import XGBClassifier
from sklearn import svm
from app.dame_sexmachine import DameSexmachine


class TddInPythonExample(unittest.TestCase):

    def test_sexmachine_features(self):
        s = DameSexmachine()
        f = s.features("David")
        self.assertEqual(f['has(a)'], True)
        self.assertEqual(f['count(i)'], 1)
        self.assertEqual(f['count(v)'], 1)
        self.assertEqual(f['last_letter'], 'd')
        self.assertEqual(f['first_letter'], 'd')

    def test_dame_sexmachine_features_int(self):
        s = DameSexmachine()
        f = s.features_int("David")
        self.assertTrue(len(f) > 0)

    def test_dame_sexmachine_guess(self):
        s = DameSexmachine()
        self.assertEqual(s.guess("David"), 'male')
        self.assertEqual(s.guess("Laura"), 'female')
        self.assertEqual(s.guess("David", binary=True), 1)
        self.assertEqual(s.guess("Laura", binary=True), 0)        
        self.assertEqual(s.guess("David", binary=True, ml="svc"), 1)
        self.assertEqual(s.guess("Laura", binary=True, ml="svc"), 0)
        self.assertEqual(s.guess("Laura", binary=True, ml="sgd"), 0)
        self.assertEqual(s.guess("David", binary=True, ml="gaussianNB"), 1)
        self.assertEqual(s.guess("David", binary=True, ml="multinomialNB"), 1)
        self.assertEqual(s.guess("David", binary=True, ml="bernoulliNB"), 1)        
        self.assertEqual(s.guess("Palabra", binary=True, ml="svc"), 1)
        self.assertEqual(s.guess("Nodiccionario", ml="nltk"), 'male')
        self.assertEqual(s.guess("Nodiccionaria", ml="nltk"), 'female')
        self.assertEqual(s.guess("Nadiccionaria", binary=True), 0)
        self.assertEqual(s.guess("Nadiccionaria"), 'female')        
#        With accents:
        self.assertEqual(s.guess("Inés"), 'female')
#        Without accents:
        self.assertEqual(s.guess("Ines"), 'female')


    def test_dame_sexmachine_guess_list(self):
        ds = DameSexmachine()
        self.assertEqual(['male', 'male', 'male', 'male', 'male', 'male',
                          'female', 'female', 'male', 'male', 'male',
                          'male', 'male', 'male', 'male', 'male', 'male',
                          'male', 'female', 'male', 'male'],
                         ds.guess_list(path="files/names/partial.csv",
                                       binary=False))
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                         ds.guess_list(path="files/names/partial.csv",
                                       binary=True))
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                         ds.guess_list(path="files/names/partial.csv",
                                       binary=True,
                                       ml="nltk"))
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                         ds.guess_list(path="files/names/partial.csv",
                                       binary=True,
                                      ml="svc"))

    def test_sexmachine_features_int(self):
        s = DameSexmachine()
        dicc = s.features_int("David")
        self.assertEqual(chr(dicc['last_letter']), 'd')
        self.assertEqual(chr(dicc['first_letter']), 'd')
        self.assertEqual(dicc['count(a)'], 1)
        self.assertEqual(dicc['count(b)'], 0)
        self.assertEqual(dicc['count(c)'], 0)
        self.assertEqual(dicc['count(d)'], 2)
        self.assertEqual(dicc['count(e)'], 0)
        self.assertEqual(dicc['count(f)'], 0)
        self.assertEqual(dicc['count(h)'], 0)
        self.assertEqual(dicc['count(i)'], 1)
        self.assertEqual(dicc['count(v)'], 1)
        self.assertTrue(dicc['count(a)'] > 0)
        self.assertTrue(dicc['vocals'], 2)
        self.assertTrue(dicc['consonants'], 3)
        self.assertEqual(dicc['first_letter_vocal'], 0)
        self.assertEqual(dicc['last_letter_vocal'], 0)
        self.assertTrue(len(dicc.values()) > 30)

    def test_sexmachine_features_list(self):
        s = DameSexmachine()
        fl = s.features_list()
        self.assertTrue(len(fl) > 20)

    def test_sexmachine_features_list_all(self):
        s = DameSexmachine()
        fl = s.features_list(path="files/names/all.csv")
        self.assertTrue(len(fl) > 1000)

    def test_sexmachine_gender_list(self):
        s = DameSexmachine()
        gl = s.gender_list(path="files/names/partial.csv")
        self.assertEqual(gl, [1, 1, 1, 1, 2, 1, 0, 0, 1, 1,
                              2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(len(gl), 21)
        self.assertEqual(s.females, 3)
        self.assertEqual(s.males, 16)
        self.assertEqual(s.unknown, 2)

    def test_sexmachine_gender_list_all(self):
        s = DameSexmachine()
        gl = s.gender_list(path="files/names/all.csv")
        self.assertTrue(len(gl) > 1000)

    def test_sexmachine_classifier(self):
        s = DameSexmachine()
        classifier = s.classifier(locale="us")
        n = s.features("David")
        guess = classifier.classify(n)
        self.assertTrue(1, n)

    def test_sexmachine_classifier_model_exists(self):
        self.assertTrue(os.path.isfile("files/datamodels/nltk_model.sav"))

    def test_sexmachine_classifier_load(self):
        s = DameSexmachine()
        m = s.classifier_load()
        n = s.features("David")
        guess = m.classify(n)
        self.assertTrue(1, n)

    # def test_sexmachine_accuracy(self):
    #     s = DameSexmachine()
    #     self.assertTrue(s.accuracy(path="files/names/partial.csv") > 0.5)

    def test_sexmachine_forest(self):
        self.assertTrue(os.path.isfile("files/datamodels/forest_model.sav"))

    def test_sexmachine_forest_load(self):
        s = DameSexmachine()
        m = s.forest_load()
        predicted = m.predict([[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
                                2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
                                0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
                                1,  0, 1]])
        a = np.array([0.65])
        self.assertEqual(predicted, a)

    def test_sexmachine_tree(self):
        self.assertTrue(os.path.isfile("files/datamodels/tree_model.sav"))

    def test_sexmachine_tree_load(self):
        s = DameSexmachine()
        m = s.tree_load()
        predicted = m.predict([[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
                                2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
                                0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
                                1,  0, 1]])
        a = np.array([0])
        self.assertEqual(predicted, a)

    def test_sexmachine_sgd_model_exists(self):
        self.assertTrue(os.path.isfile("files/datamodels/sgd_model.sav"))

    def test_sexmachine_sgd_load(self):
        s = DameSexmachine()
        m = s.sgd_load()
        predicted = m.predict([[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
                                2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
                                0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
                                1,  0, 1]])
        n = np.array([1])
        self.assertEqual(n, predicted)

    def test_sexmachine_svc_load(self):
        s = DameSexmachine()
        m = s.svc_load()
        predicted = m.predict([[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
                                2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
                                0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
                                1,  0, 1]])
        n = np.array([1])
        self.assertTrue(np.array_equal(predicted, n))

    def test_sexmachine_multinomialNB_load(self):
        s = DameSexmachine()
        m = s.multinomialNB_load()
        array = [[0,  0,  1,  0, 21,  0,  0,  0,  0,
                  34,  2,  0,  0,  0,  0,  0, 0, 0,
                  0,  0,  5,  0,  0,  0,  0,  0,  2,
                  0,  0,  0, 34,  1,  0],
                 [0,  0,  0,  0, 21,  0,  0,  0,  0,
                  34,  0,  0,  0,  0,  0,  1, 0, 0,
                  0,  0,  5,  0,  0,  1,  0,  0,  1,
                  0,  0,  1, 34,  0,  0]]
        predicted = m.predict(array)
        n = np.array([1, 1])
        self.assertTrue(np.array_equal(predicted, n))

    def test_sexmachine_bernoulliNB_load(self):
        s = DameSexmachine()
        m = s.bernoulliNB_load()
        predicted = m.predict(
            [[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
              2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
              0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
              1,  0, 1]])
        n = np.array([2])
        self.assertTrue(np.array_equal(predicted, n))

    def test_sexmachine_mlp_load(self):
        s = DameSexmachine()
        m = s.mlp_load()
        predicted = m.predict(
            [[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
              2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
              0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
              1,  0, 1]])
        n = np.array([0])
        self.assertTrue(np.array_equal(predicted, n))

    def test_sexmachine_adaboost_model_exists(self):
        self.assertTrue(os.path.isfile("files/datamodels/adaboost_model.sav"))

    # def test_sexmachine_adaboost_load(self):
    #     s = DameSexmachine()
    #     m = s.adaboost_load()
    #     predicted = m.predict(
    #         [[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
    #           2,  0,  0,  0,  0,  0, 0,  0,  0,  5,
    #           0,  0,  0,  0,  0,  2,  0,  0,  0, 34,
    #           1,  0, 1]])
    #     n = np.array([1])
    #     self.assertTrue(np.array_equal(predicted, n))

    def test_dame_gender_confusion_matrix_gender(self):
        ds = DameSexmachine()
        cm = ds.confusion_matrix_gender(path="files/names/min.csv")
        am = [[1, 0, 0], [0, 5, 0], [0, 5, 0]]
        self.assertEqual(cm, am)
        cm = ds.confusion_matrix_gender(path="files/names/min.csv", ml="nltk")
        am = [[1, 0, 0], [0, 5, 0], [0, 5, 0]]
        self.assertEqual(cm, am)
        cm = ds.confusion_matrix_gender(path="files/names/min.csv", jsonf="files/names/min.csv.json", ml="nltk")
        am = [[1, 0, 0], [0, 5, 0], [0, 5, 0]]
        self.assertEqual(cm, am)



    def test_dame_sexmachine_json2guess_list(self):
        ds = DameSexmachine()
        j2gl = ds.json2guess_list(jsonf="files/names/namsorfiles_names_min.csv.json", binary=False)
        self.assertEqual(['male', 'male', 'male', 'male', 'male', 'female'], j2gl)
        j2gl = ds.json2guess_list(jsonf="files/names/namsorfiles_names_min.csv.json", binary=True)
        self.assertEqual([1, 1, 1, 1, 1, 0], j2gl)
        j2gl = ds.json2guess_list(jsonf="files/names/min.csv.json", binary=False)
        self.assertEqual(['male', 'male', 'male', 'male', 'male', 'female'], j2gl)
        j2gl = ds.json2guess_list(jsonf="files/names/min.csv.json", binary=True)
        self.assertEqual([1, 1, 1, 1, 1, 0], j2gl)


    # # def test_sexmachine_xgboost(self):
    # #     self.assertTrue(os.path.isfile("files/datamodels/xgboost_model.sav"))

    # # def test_sexmachine_xgboost_load(self):
    # #     s = DameSexmachine()
    # #     m = s.xgboost_load()
    # #     predicted = m.predict(
    # #         [[0,  0,  1,  0, 21,  0,  0,  0,  0, 34,
    # #           2,  0,  0,  0, 0,  0, 0,  0,  0,  5,
    # #           0,  0,  0,  0,  0,  2,  0,  0, 0, 34,
    # #           1,  0, 1]])
    # #     n = np.array([0])
    # #     self.assertTrue(np.array_equal(predicted, n))
