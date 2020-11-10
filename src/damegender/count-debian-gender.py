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



import csv
import unicodedata
import unidecode
from pprint import pprint
import re
from app.dame_gender import Gender
from app.dame_utils import DameUtils

du = DameUtils()
g = Gender()


result=""
dm = []

with open('files/debian-maintainers-gpg-2020-04-01.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    aux = ""
    cnt = 0
    for row in reader:
        cnt = cnt +1
        if (aux != row[0]):
            dm.append(row[0])
        aux = row[0]


print("Perhaps you need wait some minutes. You can take a tea or coffe now")

females = 0
males = 0
unknows = 0

list_males = []
list_females = []
list_unknows = []
for rowdm in dm:
    sex = g.guess(rowdm.upper(), binary=False)
    
    if (sex == 'female'):
        females = females + 1
        list_females.append(rowdm)
    elif (sex == 'male'):
        males = males + 1
        list_males.append(rowdm)        
    else:
        unknows = unknows + 1
        list_unknows.append(rowdm)

print("debian males: %s" % len(list_males))
print("debian females: %s" % len(list_females))
print("debian unknows: %s" % len(list_unknows))

csvfile.close()


import matplotlib.pyplot as plt

data = [len(list_males), len(list_females), len(list_unknows)]
gender = ["Males","Females", "Unknows"]
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.title("Debian people grouped by gender")
plt.savefig('files/images/debian_by_gender.png')
plt.axis("equal")
plt.show()
