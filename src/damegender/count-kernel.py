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
import argparse

from app.dame_gender import Gender
from app.dame_utils import DameUtils

parser = argparse.ArgumentParser()
parser.add_argument('--show', choices=['males', 'females', 'unknows', 'all'])
parser.add_argument('--version', action='version', version='0.3')
args = parser.parse_args()

du = DameUtils()
g = Gender()


result=""
dm = []

with open('files/linux-maintainers.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    aux = ""
    cnt = 0
    for row in reader:
        cnt = cnt +1
#        print(row[0])
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
    listfullname = rowdm.split()
    name = listfullname[0]
    sex = g.guess(name.upper(), binary=False)
    
    if (sex == 'female'):
        females = females + 1
        list_females.append(name)
    elif (sex == 'male'):
        males = males + 1
        list_males.append(name)        
    else:
        unknows = unknows + 1
        list_unknows.append(name)
        
print("this kernel maintainers list is about %s people" % len(dm))        
print("kernel maintainers males: %s" % males)
print("kernel maintainers females: %s" % females)
print("kernel maintainers not classified: %s" % unknows)

if ((args.show=='males') or (args.show=='all')):
    print("The list of kernel maintainers males:" % list_males)
    print(list_males)
    
if ((args.show=='females') or (args.show=='all')):
    print("The list of kernel maintainers females:" % list_females)
    print(list_females)
    
if ((args.show=='unknows') or (args.show=='all')):
    print("The list of people with unknown gender as kernel maintainers:" % list_unknows)
    print(list_unknows)

csvfile.close()



import matplotlib.pyplot as plt

data = [len(list_males), len(list_females), len(list_unknows)]
gender = ["Males","Females", "Unknows"]
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.title("Kernel people grouped by gender")
plt.savefig('files/images/kernel_by_gender.png')
plt.savefig('files/images/kernel_by_gender.svg', format="svg")
plt.axis("equal")
plt.show()
