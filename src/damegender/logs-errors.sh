#!/usr/bin/bash
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
# along with Damegender in the file GPL.txt.  If not, see
# <https://www.gnu.org/licenses/>.




#### ADABOOST ALGORITHM
echo "python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.adaboost.json > files/logs/errors-adaboost-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-adaboost-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.adaboost.json >> files/logs/errors-adaboost-$(date "+%Y-%m-%d").txt

#### MLP ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.mlp.json > files/logs/errors-mlp-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-mlp-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.mlp.json >> files/logs/errors-mlp-$(date "+%Y-%m-%d").txt

#### SGD ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.sgd.json > files/logs/errors-sgd-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-sgd-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.sgd.json >> files/logs/errors-sgd-$(date "+%Y-%m-%d").txt

#### SVC ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.svc.json  > files/logs/errors-svc-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-svc-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.svc.json  >> files/logs/errors-svc-$(date "+%Y-%m-%d").txt

#### TREE ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.tree.json  > files/logs/errors-tree-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-tree-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined+header.csv --jsondownloaded=files/names/allnoundefined.csv.tree.json  >> files/logs/errors-tree-$(date "+%Y-%m-%d").txt

#### NLTK ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.nltk.json > files/logs/errors-nltk-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-nltk-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.nltk.json >> files/logs/errors-nltk-$(date "+%Y-%m-%d").txt

#### BERNOULLINB ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.bernoulliNB.json > files/logs/errors-bernoulliNB-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-bernoulliNB-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.bernoulliNB.json >> files/logs/errors-bernoulliNB-$(date "+%Y-%m-%d").txt

#### MULTINOMIALNB ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.multinomialNB.json > files/logs/errors-multinomialNB-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-multinomialNB-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.multinomialNB.json >> files/logs/errors-multinomialNB-$(date "+%Y-%m-%d").txt

#### GAUSSIANNB ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.gaussianNB.json > files/logs/errors-gaussianNB-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-gaussianNB-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.gaussianNB.json >> files/logs/errors-gaussianNB-$(date "+%Y-%m-%d").txt

#### FOREST ALGORITHM

echo "python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.forest.json > files/logs/errors-forest-"$(date "+%Y-%m-%d")".txt " > files/logs/errors-forest-$(date "+%Y-%m-%d").txt

python3 errors.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.forest.json >> files/logs/errors-forest-$(date "+%Y-%m-%d").txt
