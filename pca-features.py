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
import matplotlib.pyplot as plt
from app.dame_sexmachine import DameSexmachine
from app.dame_gender import Gender

## LOAD DATASET
g = Gender()
g.features_list2csv(categorical="both", path="files/all.csv")
features = "files/features_list.csv"

print("STEP1: N COMPONENTS + 1 TARGET")

x = pd.read_csv(features)
print(x.columns)

y = g.dataset2genderlist(dataset="files/all.csv")
print(y)

print("STEP2: STANDARIZE THE DATA")
from sklearn.preprocessing import StandardScaler
# Standardizing the features
x = StandardScaler().fit_transform(x)

# ## PCA PROJECTION TO N DIMENSIONS

from sklearn.decomposition import PCA
pca = PCA(n_components=6)
principalComponents = pca.fit_transform(x)
print("STEP3: PCA PROJECTION")
pprint(principalComponents)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4', 'principal component 5', 'principal component 6'])

target = pd.DataFrame(data = y, columns = ['target component'])

print(principalDf.join(target))

# print(list(principalDf.columns.values))
# finalDf = pd.concat([principalDf, y])

# ## Visualize N Projection

# fig = plt.figure(figsize = (8,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_alabel('Principal Component 1', fontsize = 15)
# ax.set_blabel('Principal Component 2', fontsize = 15)
# ax.set_clabel('Principal Component 3', fontsize = 15)
# ax.set_dlabel('Principal Component 4', fontsize = 15)
# ax.set_elabel('Principal Component 5', fontsize = 15)
# ax.set_flabel('Principal Component 6', fontsize = 15)
# ax.set_title('6 component PCA', fontsize = 20)
# targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# colors = ['r', 'g', 'b']
# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf['target'] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)
# ax.legend(targets)
# ax.grid()

# plt.show()
