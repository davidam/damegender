#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com> 
# Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv

dicc = {}

def int_with_null(x):
    ret = 0
    if (x == 'null'):
        ret = 0
    else:
        ret =  int(x)
    return ret

with open('walesmales.orig.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = -1
    for row in reader:
        i = i + 1
        if (i == 0):
            v = row[0].split(';')
            dicc = {}
            for index in v:
                dicc[index] = 0
        else:
            j = 1
            w = row[0].split(';')

            while (j < len(w)):
                dicc[v[j]] = int(dicc[v[j]]) + int_with_null(w[j])
                j = j + 1

fo = open("walesmales.csv", "w")                
for i in dicc.keys():
    if (i != "Date"):
        fo.write(str(i)+","+str(dicc[i])+"\n");

fo.close()


# with open('walesfemales.orig.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     i = -1
#     for row in reader:
#         i = i + 1
#         if (i == 0):
#             v = row[0].split(';')
#             dicc = {}
#             for index in v:
#                 dicc[index] = 0
#         else:
#             j = 1
#             w = row[0].split(';')

#             while (j < len(w)):
#                 dicc[v[j]] = int(dicc[v[j]]) + int_with_null(w[j])
#                 j = j + 1

# fo2 = open("walesfemales.csv", "w")                
# for i in dicc.keys():
#     if (i != "Date"):
#         fo2.write(str(i)+","+str(dicc[i])+"\n");

# fo2.close()


# print(dicc.keys())
# print(dicc.values())
    # for row in reader:
    #     dicc[row[2]] = dicc[row[2]] + int(row[3])
