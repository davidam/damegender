#  Copyright (C) 2020 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com> 
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
#  You can share, copy and modify this software if you are a woman or you
#  are David Arroyo Menéndez and you include this note.

import csv

#from app.dame_utils import DameUtils

def number_or_zero(x):
    try:
        num = int(x)
    except ValueError:
        num = 0
    return num

print(number_or_zero("-"))

l = []
dicc = {}
with open('males-by-year.csv', newline='', encoding='utf-8') as csvfile:
    next(csvfile) # skipping the header row, first row
    next(csvfile) # skipping the header row, first row
    next(csvfile) # skipping the header row, first row
    sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sexreader:
        dicc[row[0]] = number_or_zero(row[1]) + number_or_zero(row[2]) + number_or_zero(row[3]) + number_or_zero(row[4]) + number_or_zero(row[5]) + number_or_zero(row[6]) + number_or_zero(row[7]) + number_or_zero(row[8]) + number_or_zero(row[9]) + number_or_zero(row[10]) + number_or_zero(row[11]) + number_or_zero(row[12]) + number_or_zero(row[13])  

fo = open("simales.csv", "w")
for i in dicc.keys():
    fo.write(str(i) + "," + str(dicc[i]) + "\n")

fo.close()    
        
