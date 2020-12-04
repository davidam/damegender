#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.




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

with open('files/forbes2020.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    aux = ""
    cnt = 0
    for row in reader:
        cnt = cnt +1
#        print(row[0])
        if (aux != row[0]):
            dm.append(row[0])
        aux = row[0]

    #print(dm)
    #print(len(dm))
    #print(cnt)

print("Perhaps you need wait some minutes. You can take a tea or coffe now")

females = 0
males = 0
unknows = 0
for rowdm in dm:
    sex = g.guess(rowdm.upper(), binary=False)
    
    if (sex == 'female'):
        females = females + 1
    elif (sex == 'male'):
        males = males + 1
    else:
        unknows = unknows + 1
        
print("this forbes list is about %s people" % len(dm))        
print("forbes males: %s" % males)
print("forbes females: %s" % females)
print("forbes not classified people: %s" % unknows)

csvfile.close()

import matplotlib.pyplot as plt

data = [males, females, unknows]
gender = ["Males","Females","Unknows"]
plt.title("Top 119 Forbes people grouped by gender")
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.axis("equal")
plt.savefig('files/images/forbes119_by_gender.png')
plt.show()
