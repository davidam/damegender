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

#### GET 

cd ../../files/names
wget -c https://raw.githubusercontent.com/GenderGapSTEM-PublicationAnalysis/name_gender_inference/main/name_gender_inference/test_data/raw_data/all.csv
grep -v ',"u",' all.csv > allnoundefined+header.csv
grep -v '"first_name","middle_name","last_name","full_name","gender","origin"' allnoundefined+header.csv > allnoundefined.csv

cd ../..

#### INTER DATASET

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=accuracy --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=2 --dataset_test_position_gender=2 --dataset_test_gender_chars="female,male" > files/logs/accuracy-inter-"$(date "+%Y-%m-%d")".txt > files/logs/accuracy-inter-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=accuracy --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_position_gender=2 --dataset_test_position_gender=2 --dataset_test_gender_chars='female,male'" > files/logs/precision-inter-"$(date "+%Y-%m-%d")".txt 

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=precision --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="female,male" > files/logs/precision-inter-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=recall --api=damegender --dataset_guess_position_gender=4 --dataset_test_position_gender=2 --dataset_test_gender_chars='female,male' --dataset_guess_gender_chars='f,m'" > files/logs/recall-inter-"$(date "+%Y-%m-%d")".txt 

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=recall --api=damegender --dataset_guess_position_gender=4 --dataset_test_position_gender=2 --dataset_test_gender_chars="female,male" --dataset_guess_gender_chars="f,m" > files/logs/recall-inter-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=f1score --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_gender_chars='female,male' --dataset_test_position_gender=2 > files/logs/f1score-inter-$(date "+%Y-%m-%d").txt" 

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.inter.json --measure=f1score --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="female,male" --dataset_test_position_gender=2 > files/logs/f1score-inter-$(date "+%Y-%m-%d").txt

# echo "python3 accuracy.py --dataset_guess=files/names/names_inter/intermales.csv --dataset_test=files/names/names_tests/fifa.csv --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-inter-males-$(date "+%Y-%m-%d").txt"

mkdir -p files/tmp
sed "s/$/\;male/g" files/names/names_tests/fifa.csv > files/tmp/fifa+gender.csv
sed "s/$/\,male/g" files/names/names_inter/intermales.csv > files/tmp/intermales+gender.csv

python3 accuracy.py --dataset_guess=files/tmp/intermales+gender.csv --dataset_test=files/tmp/fifa+gender.csv --dataset_guess_position_name=3 --dataset_guess_position_gender=185 --dataset_guess_delimiter=";" --measure=accuracy --api=damegender > files/logs/accuracy-inter-males-$(date "+%Y-%m-%d").txt

#### MLP ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=f1score --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_position_gender=4 --dataset_test_gender_chars='female,male'" > files/logs/accuracy-mlp-f1score-'$(date "+%Y-%m-%d")'.txt   > files/logs/accuracy-mlp-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=f1score --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="female,male" > files/logs/accuracy-mlp-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=accuracy --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_position_gender=4 --dataset_test_gender_chars='female,male'"

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=accuracy --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="female,male" > files/logs/accuracy-mlp-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=precision --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_position_gender=4 --dataset_test_gender_chars='female,male'" > files/logs/accuracy-mlp-precision-'$(date "+%Y-%m-%d")'.txt  

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=precision --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="female,male" > files/logs/accuracy-mlp-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=recall --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_position_gender=4 --dataset_test_gender_chars='female,male'" > files/logs/accuracy-mlp-recall-'$(date "+%Y-%m-%d")'.txt  

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.mlp.json --measure=recall --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="female,male" > files/logs/accuracy-mlp-recall-$(date "+%Y-%m-%d").txt


#### SGD ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-sgd-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-sgd-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-sgd-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-sgd-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-sgd-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-sgd-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-sgd-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-sgd-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.sgd.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-sgd-recall-$(date "+%Y-%m-%d").txt

#### SVC ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-svc-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-svc-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-svc-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-svc-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-svc-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-svc-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-svc-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-svc-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.svc.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-svc-recall-$(date "+%Y-%m-%d").txt

#### TREE ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-tree-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-tree-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-tree-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-tree-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-tree-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-tree-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-tree-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-tree-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.tree.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-tree-recall-$(date "+%Y-%m-%d").txt


#### NLTK ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-nltk-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-nltk-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-nltk-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-nltk-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-nltk-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-nltk-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-nltk-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-nltk-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.nltk.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-nltk-recall-$(date "+%Y-%m-%d").txt


#### BERNOULLINB ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-bernoulliNB-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-bernoulliNB-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-bernoulliNB-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-bernoulliNB-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-bernoulliNB-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-bernoulliNB-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-bernoulliNB-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-bernoulliNB-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.bernoulliNB.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-bernoulliNB-recall-$(date "+%Y-%m-%d").txt


#### MULTINOMIALNB ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-multinomialNB-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-multinomialNB-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-multinomialNB-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-multinomialNB-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-multinomialNB-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-multinomialNB-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-multinomialNB-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-multinomialNB-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.multinomialNB.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-multinomialNB-recall-$(date "+%Y-%m-%d").txt


#### GAUSSIANNB ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-gaussianNB-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-gaussianNB-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-gaussianNB-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-gaussianNB-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-gaussianNB-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-gaussianNB-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-gaussianNB-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-gaussianNB-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.gaussianNB.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-gaussianNB-recall-$(date "+%Y-%m-%d").txt

#### FOREST ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-forest-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-forest-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-forest-accuracy-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-accuracy-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=accuracy --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-forest-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=precision --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-forest-precision-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-precision-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=precision --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-forest-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=recall --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-forest-recall-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-forest-recall-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined+header.csv --dataset_test=files/names/allnoundefined.csv.forest.json --measure=recall --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-forest-recall-$(date "+%Y-%m-%d").txt

#### ADABOOST ALGORITHM

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 > files/logs/accuracy-forest-f1score-"$(date "+%Y-%m-%d")".txt " > files/logs/accuracy-adaboost-f1score-$(date "+%Y-%m-%d").txt

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=f1score --api=damegender --dataset_guess_row_gender=4 >> files/logs/accuracy-adaboost-f1score-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=accuracy --dataset_guess_position_gender=4 --api=damegender --dataset_guess_gender_chars='f,m' --dataset_test_gender_chars='female,male' --dataset_test_position_gender=3 > files/logs/accuracy-adaboost-accuracy-$(date "+%Y-%m-%d").txt"

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=accuracy --dataset_guess_position_gender=4 --api=damegender --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="female,male" --dataset_test_position_gender=3 > files/logs/accuracy-adaboost-accuracy-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=precision --api=damegender --dataset_guess_position_gender=4 --dataset_guess_gender_chars='f,m' --dataset_test_gender_chars='female,male' --dataset_test_position_gender=3 > files/logs/accuracy-adaboost-precision-$(date "+%Y-%m-%d").txt"

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=precision --dataset_guess_position_gender=4 --api=damegender --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="female,male" --dataset_test_position_gender=3 > files/logs/accuracy-adaboost-precision-$(date "+%Y-%m-%d").txt

echo "python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=recall --dataset_guess_position_gender=4 --api=damegender --dataset_guess_gender_chars='f,m' --dataset_test_gender_chars='female,male' --dataset_test_position_gender=3 > files/logs/accuracy-adaboost-recall-$(date "+%Y-%m-%d").txt"

python3 accuracy.py --dataset_guess=files/names/allnoundefined.csv --dataset_test=files/names/allnoundefined.csv.adaboost.json --measure=recall --api=damegender --dataset_guess_position_gender=4 --api=damegender --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="female,male" --dataset_test_position_gender=3 > files/logs/accuracy-adaboost-recall-$(date "+%Y-%m-%d").txt
