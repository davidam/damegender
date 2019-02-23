#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,


from pprint import pprint
import pandas as pd
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
from app.dame_sexmachine import DameSexmachine
from app.dame_gender import Gender

## LOAD DATASET
g = Gender()
g.features_list2csv(categorical="both", path="files/names/all.csv")
features = "files/features_list.csv"

#print("STEP1: N COMPONENTS + 1 TARGET")

x = pd.read_csv(features)
print(x.columns)

y = g.dataset2genderlist(dataset="files/names/all.csv")
print(y)

# load dataset

# adding target
target = pd.DataFrame(data = y, columns = ['target component'])
finalDf = x.join(target)


# normalize data
from sklearn import preprocessing
data_scaled = pd.DataFrame(preprocessing.scale(finalDf), columns = finalDf.columns)


# PCA
pca = PCA(n_components=6)
pca.fit_transform(data_scaled)

# Dump components relations with features:
print(pd.DataFrame(pca.components_,columns=data_scaled.columns,index = ['PC-1','PC-2','PC-3','PC-4','PC-5','PC-6']))



# print("STEP2: STANDARIZE THE DATA")
# from sklearn.preprocessing import StandardScaler
# # Standardizing the features
# x = StandardScaler().fit_transform(x)

# # ## PCA PROJECTION TO N DIMENSIONS

# from sklearn.decomposition import PCA
# pca = PCA(n_components=6)
# principalComponents = pca.fit_transform(x)
# print("STEP3: PCA PROJECTION")
# pprint(principalComponents)
# principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4', 'principal component 5', 'principal component 6'])

# target = pd.DataFrame(data = y, columns = ['target component'])

# finalDf = data_scaled.join(target)


# # # ## Visualize N Projection

# finalDf.plot()
# plt.show()
