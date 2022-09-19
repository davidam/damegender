#!/bin/sh
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

#### INTER DATASET

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=accuracy --api=damegender > files/logs/accuracy-inter-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-inter-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=accuracy --api=damegender > files/logs/accuracy-inter-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=precision --api=damegender > files/logs/precision-inter-"$(date "+%Y-%m-%d")".txt " > files/logs/precision-inter-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=precision --api=damegender > files/logs/precision-inter-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=recall --api=damegender > files/logs/recall-inter-"$(date "+%Y-%m-%d")".txt " > files/logs/recall-inter-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=recall --api=damegender > files/logs/recall-inter-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=f1score --api=damegender > files/logs/f1score-inter-"$(date "+%Y-%m-%d")".txt " > files/logs/f1score-inter-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=f1score --api=damegender > files/logs/f1score-inter-$(date "+%Y-%m-%d").txt


#### MLP ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --api=damegender > files/logs/accuracy-mlp-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=f1score --api=damegender >> files/logs/accuracy-mlp-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=accuracy --api=damegender > files/logs/accuracy-mlp-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-mlp-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=accuracy --api=damegender >> files/logs/accuracy-mlp-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=precision --api=damegender > files/logs/accuracy-mlp-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-mlp-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=precision --api=damegender >> files/logs/accuracy-mlp-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=recall --api=damegender > files/logs/accuracy-mlp-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-mlp-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=recall --api=damegender >> files/logs/accuracy-mlp-recall-$(date "+%Y-%m-%d").txt

#### SGD ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=f1score --api=damegender > files/logs/accuracy-sgd-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=f1score --api=damegender >> files/logs/accuracy-sgd-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=accuracy --api=damegender > files/logs/accuracy-sgd-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=accuracy --api=damegender >> files/logs/accuracy-sgd-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=precision --api=damegender > files/logs/accuracy-sgd-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=precision --api=damegender >> files/logs/accuracy-sgd-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=recall --api=damegender > files/logs/accuracy-sgd-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=recall --api=damegender >> files/logs/accuracy-sgd-recall-$(date "+%Y-%m-%d").txt

#### SVC ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=f1score --api=damegender > files/logs/accuracy-svc-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=f1score --api=damegender >> files/logs/accuracy-svc-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=accuracy --api=damegender > files/logs/accuracy-svc-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=accuracy --api=damegender >> files/logs/accuracy-svc-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=precision --api=damegender > files/logs/accuracy-svc-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=precision --api=damegender >> files/logs/accuracy-svc-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=recall --api=damegender > files/logs/accuracy-svc-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=recall --api=damegender >> files/logs/accuracy-svc-recall-$(date "+%Y-%m-%d").txt

#### TREE ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=f1score --api=damegender > files/logs/accuracy-tree-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=f1score --api=damegender >> files/logs/accuracy-tree-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=accuracy --api=damegender > files/logs/accuracy-tree-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=accuracy --api=damegender >> files/logs/accuracy-tree-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=precision --api=damegender > files/logs/accuracy-tree-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=precision --api=damegender >> files/logs/accuracy-tree-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=recall --api=damegender > files/logs/accuracy-tree-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=recall --api=damegender >> files/logs/accuracy-tree-recall-$(date "+%Y-%m-%d").txt


#### NLTK ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=f1score --api=damegender > files/logs/accuracy-nltk-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=f1score --api=damegender >> files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=accuracy --api=damegender > files/logs/accuracy-nltk-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=accuracy --api=damegender >> files/logs/accuracy-nltk-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=precision --api=damegender > files/logs/accuracy-nltk-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=precision --api=damegender >> files/logs/accuracy-nltk-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=recall --api=damegender > files/logs/accuracy-nltk-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=recall --api=damegender >> files/logs/accuracy-nltk-recall-$(date "+%Y-%m-%d").txt


#### BERNOULLINB ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=f1score --api=damegender > files/logs/accuracy-bernoulliNB-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=f1score --api=damegender >> files/logs/accuracy-bernoulliNB-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=accuracy --api=damegender > files/logs/accuracy-bernoulliNB-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=accuracy --api=damegender >> files/logs/accuracy-bernoulliNB-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=precision --api=damegender > files/logs/accuracy-bernoulliNB-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=precision --api=damegender >> files/logs/accuracy-bernoulliNB-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=recall --api=damegender > files/logs/accuracy-bernoulliNB-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=recall --api=damegender >> files/logs/accuracy-bernoulliNB-recall-$(date "+%Y-%m-%d").txt


#### MULTINOMIALNB ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=f1score --api=damegender > files/logs/accuracy-multinomialNB-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=f1score --api=damegender >> files/logs/accuracy-multinomialNB-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=accuracy --api=damegender > files/logs/accuracy-multinomialNB-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=accuracy --api=damegender >> files/logs/accuracy-multinomialNB-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=precision --api=damegender > files/logs/accuracy-multinomialNB-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=precision --api=damegender >> files/logs/accuracy-multinomialNB-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=recall --api=damegender > files/logs/accuracy-multinomialNB-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=recall --api=damegender >> files/logs/accuracy-multinomialNB-recall-$(date "+%Y-%m-%d").txt


#### GAUSSIANNB ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=f1score --api=damegender > files/logs/accuracy-gaussianNB-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=f1score --api=damegender >> files/logs/accuracy-gaussianNB-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=accuracy --api=damegender > files/logs/accuracy-gaussianNB-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=accuracy --api=damegender >> files/logs/accuracy-gaussianNB-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=precision --api=damegender > files/logs/accuracy-gaussianNB-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=precision --api=damegender >> files/logs/accuracy-gaussianNB-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=recall --api=damegender > files/logs/accuracy-gaussianNB-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=recall --api=damegender >> files/logs/accuracy-gaussianNB-recall-$(date "+%Y-%m-%d").txt

#### FOREST ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=f1score --api=damegender > files/logs/accuracy-forest-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=f1score --api=damegender >> files/logs/accuracy-forest-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=accuracy --api=damegender > files/logs/accuracy-forest-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=accuracy --api=damegender >> files/logs/accuracy-forest-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=precision --api=damegender > files/logs/accuracy-forest-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=precision --api=damegender >> files/logs/accuracy-forest-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=recall --api=damegender > files/logs/accuracy-forest-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=recall --api=damegender >> files/logs/accuracy-forest-recall-$(date "+%Y-%m-%d").txt

#### ADABOOST ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=f1score --api=damegender > files/logs/accuracy-forest-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-adaboost-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=f1score --api=damegender >> files/logs/accuracy-adaboost-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=accuracy --api=damegender > files/logs/accuracy-adaboost-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-adaboost-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=accuracy --api=damegender >> files/logs/accuracy-adaboost-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=precision --api=damegender > files/logs/accuracy-adaboost-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-adaboost-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=precision --api=damegender >> files/logs/accuracy-adaboost-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=recall --api=damegender > files/logs/accuracy-adaboost-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-adaboost-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=recall --api=damegender >> files/logs/accuracy-adaboost-recall-$(date "+%Y-%m-%d").txt
