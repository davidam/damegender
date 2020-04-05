#!/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez

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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

#### MLP ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.mlp.json --reverse --api=damegender > files/logs/confusion-mlp-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-mlp-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.mlp.json --reverse --api=damegender >> files/logs/confusion-mlp-$(date "+%Y-%m-%d").txt

#### SGD ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.sgd.json --reverse --api=damegender > files/logs/confusion-sgd-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.sgd.json --reverse --api=damegender >> files/logs/confusion-sgd-$(date "+%Y-%m-%d").txt

#### SVC ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.svc.json --reverse --api=damegender > files/logs/confusion-svc-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-svc-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.svc.json --reverse --api=damegender >> files/logs/confusion-svc-$(date "+%Y-%m-%d").txt

#### TREE ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.tree.json --reverse --api=damegender > files/logs/confusion-tree-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-tree-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.tree.json --reverse --api=damegender >> files/logs/confusion-tree-$(date "+%Y-%m-%d").txt

#### NLTK ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.nltk.json --reverse --api=damegender > files/logs/confusion-nltk-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-nltk-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.nltk.json --reverse --api=damegender >> files/logs/confusion-nltk-$(date "+%Y-%m-%d").txt

#### BERNOULLINB ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.bernoulliNB.json --reverse --api=damegender > files/logs/confusion-bernoulliNB-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-bernoulliNB-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.bernoulliNB.json --reverse --api=damegender >> files/logs/confusion-bernoulliNB-$(date "+%Y-%m-%d").txt

#### MULTINOMIALNB ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.multinomialNB.json --reverse --api=damegender > files/logs/confusion-multinomialNB-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-multinomialNB-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.multinomialNB.json --reverse --api=damegender >> files/logs/confusion-multinomialNB-$(date "+%Y-%m-%d").txt

#### GAUSSIANNB ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.gaussianNB.json --reverse --api=damegender > files/logs/confusion-gaussianNB-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-gaussianNB-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.gaussianNB.json --reverse --api=damegender >> files/logs/confusion-gaussianNB-$(date "+%Y-%m-%d").txt

#### FOREST ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.forest.json --reverse --api=damegender > files/logs/confusion-forest-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-forest-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.forest.json --reverse --api=damegender >> files/logs/confusion-forest-$(date "+%Y-%m-%d").txt

