#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.





#### ADABOOST ALGORITHM

echo "python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.adaboost.json --reverse --api=damegender > files/logs/confusion-adaboost-"$(date "+%Y-%m-%d")".txt " > files/logs/confusion-adaboost-$(date "+%Y-%m-%d").txt

python3 confusion.py --csv=files/names/allnoundefined.csv --jsondownloaded=files/names/allnoundefined.csv.adaboost.json --reverse --api=damegender >> files/logs/confusion-adaboost-$(date "+%Y-%m-%d").txt

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

