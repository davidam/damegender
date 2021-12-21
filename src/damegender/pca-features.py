#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

# DESCRIPTION: Returns Principal Component Analysis (features) from damegender
# csv files given a number of components and a category

import json
import pandas as pd
import matplotlib.pyplot as plt
import argparse

from json2html import *
from pprint import pprint
from sklearn.decomposition import PCA
from app.dame_sexmachine import DameSexmachine
from app.dame_gender import Gender

# PARAMETERS
parser = argparse.ArgumentParser()
parser.add_argument("--categorical", default="both",
                    choices=['both', 'noletters', 'nocategorical', 'all'])
parser.add_argument("--components", default=0, type=int)
args = parser.parse_args()

if (args.components > 0):
    # LOAD DATASET
    g = Gender()
    if (args.categorical == "both"):
        g.features_list2csv(categorical="both",
                            path="files/names/allnoundefined.csv")
        features = "files/features_list_no_undefined.csv"
    elif (args.categorical == "noletters"):
        g.features_list2csv(categorical="noletters",
                            path="files/names/allnoundefined.csv")
        features = "files/features_list_cat.csv"
    elif (args.categorical == "nocategorical"):
        g.features_list2csv(categorical="nocategorical",
                            path="files/names/allnoundefined.csv")
        features = "files/features_list_no_cat.csv"
    else:
        g.features_list2csv(categorical="both",
                            path="files/names/all.csv")
        features = "files/features_list.csv"
    # STEP1: N COMPONENTS + 1 TARGET
    x = pd.read_csv(features)

    y = g.dataset2genderlist(dataset="files/names/allnoundefined.csv")

    # STEP2: ADDING TARGET
    target = pd.DataFrame(data=y, columns=['target component'])
    finalDf = x.join(target)

    # STEP3: NORMALIZE DATA
    from sklearn import preprocessing
    data1 = pd.DataFrame(preprocessing.scale(finalDf), columns=finalDf.columns)

    # STEP4: PCA
    pca = PCA(n_components=int(args.components))
    pca.fit_transform(data1)

    # STEP5: Dump components relations with features:

    finalIndex = []
    for i in range(1, int(args.components)+1):
        finalIndex.append('PC-'+str(i))

    df = pd.DataFrame(pca.components_, columns=data1.columns, index=finalIndex)

    jsondata = df.to_json(orient='records')

    fo = open("files/pca.json", "w")
    fo.write(jsondata)
    # Close json file
    fo.close()

    print("The json file is created in files/pca.json")

    # STEP6: Dump to html file

    jh = json2html.convert(json=jsondata)
    jh = "<html><body>" + jh + "</body></html>"
    fo = open("files/pca.html", "w")
    fo.write(jh)

    print("The html file is created in files/pca.html")
else:
    print("Components must be >0, try with: ")
    print("$ python3 pca-features.py --categorical='noletters' --components=3")
    print("You can use")
    print("$ python3 pca-components.py to determine the number of components")
