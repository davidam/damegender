#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


echo "------------------------------------------------------------------------------------------"
echo "This process is so long. You can rest some days"
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           Creating SGD ML model                                                          "
echo "------------------------------------------------------------------------------------------"


python3 damegender2json.py --ml=sgd --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.sgd.json

echo "------------------------------------------------------------------------------------------"
echo "           SGD ML model is created                                                        "
echo "------------------------------------------------------------------------------------------"


echo "------------------------------------------------------------------------------------------"
echo "           Creating SVC ML model                                                          "
echo "------------------------------------------------------------------------------------------"


python3 damegender2json.py --ml=svc --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.svc.json

echo "------------------------------------------------------------------------------------------"
echo "           SVC ML model is created                                                        "
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           Creating NLTK ML model                                                         "
echo "------------------------------------------------------------------------------------------"

python3 damegender2json.py --ml=nltk --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.nltk.json

echo "------------------------------------------------------------------------------------------"
echo "           NLTK ML model is created                                                       "
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           GAUSSIAN NAIVE BAYES ML model is created                                       "
echo "------------------------------------------------------------------------------------------"


python3 damegender2json.py --ml=gaussianNB --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.gaussianNB.json

echo "------------------------------------------------------------------------------------------"
echo "           GAUSSIAN NAIVE BAYES ML model is created                                       "
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           Creating MULTINOMIAL NAIVE BAYES ML model                                      "
echo "------------------------------------------------------------------------------------------"

python3 damegender2json.py --ml=multinomialNB --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.multinomialNB.json

echo "------------------------------------------------------------------------------------------"
echo "           MULTINOMIAL NAIVE BAYES ML model is created                                    "
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           Creating BERNOULLI NAIVE BAYES ML model                                        "
echo "------------------------------------------------------------------------------------------"

python3 damegender2json.py --ml=bernoulliNB --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.bernoulliNB.json

echo "------------------------------------------------------------------------------------------"
echo "           BERNOULLI NAIVE BAYES ML model is created                                      "
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           Creating TREE ML model                                                         "
echo "------------------------------------------------------------------------------------------"

python3 damegender2json.py --ml=tree --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.tree.json

echo "------------------------------------------------------------------------------------------"
echo "           TREE ML model is created                                                       "
echo "------------------------------------------------------------------------------------------"

echo "------------------------------------------------------------------------------------------"
echo "           Creating MULTILAYER PERCEPTRON ML model                                        "
echo "------------------------------------------------------------------------------------------"

python3 damegender2json.py --ml=mlp --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.mlp.json

echo "------------------------------------------------------------------------------------------"
echo "           MULTILAYER PERCEPTRON ML model is created                                      "
echo "------------------------------------------------------------------------------------------"
