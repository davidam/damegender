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



"""
================================
ROC Curve with Visualization API
================================
Scikit-learn defines a simple API for creating visualizations for machine
learning. The key features of this API is to allow for quick plotting and
visual adjustments without recalculation. In this example, we will demonstrate
how to use the visualization API by comparing ROC curves.
"""
print(__doc__)

##############################################################################
# Load Data and Train a SVC
# -------------------------
# First, we load the wine dataset and convert it to a binary classification
# problem. Then, we train a support vector classifier on a training dataset.
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import plot_roc_curve
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier


from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_utils import DameUtils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ml', choices=['svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--noshow', dest='noshow', action='store_true')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()


ds = DameSexmachine()
X = np.array(ds.features_list(path="files/names/allnoundefined.csv"))
y = ds.gender_list(path="files/names/allnoundefined.csv")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

if (args.verbose):
    print(X)
    print(y)

if (args.ml == "svc"):
    svc = SVC(random_state=42)
    svc.fit(X_train, y_train)
    svc_disp = plot_roc_curve(svc, X_test, y_test)

elif (args.ml == "forest"):
    rfc = RandomForestClassifier(n_estimators=10, random_state=42)
    rfc.fit(X_train, y_train)
    ax = plt.gca()
    rfc_disp = plot_roc_curve(rfc, X_test, y_test, ax=ax, alpha=0.8)
    rfc_disp.plot(ax=ax, alpha=0.8)

elif (args.ml == "sgd"):
    clf = SGDClassifier(loss="log").fit(X_train, y_train)
    sgd_disp = plot_roc_curve(clf, X_test, y_test)

elif (args.ml == "gaussianNB"):
    # Create a Gaussian Classifier
    model = GaussianNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)
    disp = plot_roc_curve(model, X_test, y_test)

elif (args.ml == "multinomialNB"):
    # Create a Multinomial Classifier
    model = MultinomialNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)
    disp = plot_roc_curve(model, X_test, y_test)

elif (args.ml == "bernoulliNB"):
    # Create a Bernoulli Classifier
    model = BernoulliNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)
    disp = plot_roc_curve(model, X_test, y_test)

elif (args.ml == "tree"):
    # Create a tree Classifier
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    disp = plot_roc_curve(clf, X_test, y_test)

elif (args.ml == "mlp"):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(X_test, y_test)
    disp = plot_roc_curve(clf, X_test, y_test)

if (args.noshow):
    plt.savefig('files/images/roc_'+ args.ml + '.png')
else:
    plt.savefig('files/images/roc_'+ args.ml + '.png')
    plt.show()
