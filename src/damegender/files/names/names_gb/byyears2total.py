#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv


l = []
with open('nat2019females.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    name = ""
    cnt = 0
    for row in reader:
        if (row[0] != name):
            print(name)
            print(cnt)
            l.append([name, cnt])
            name = str(row[0])
            cnt = int(row[2])
        else:
            cnt = cnt + int(row[2])
    l.append([name, cnt])
    print(name)
    print(cnt)

print(l)
fo = open("frfemales.csv", "w")
ll = l[1:len(l)]
print(ll)
for i in ll:
    fo.write(str(i[0]) + "," + str(i[1]) + "\n");

# Cerramos el archivo fichero.txt
fo.close()


l = []
with open('nat2019males.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    name = ""
    cnt = 0
    for row in reader:
        if (row[0] != name):
            print(name)
            print(cnt)
            l.append([name, cnt])
            name = str(row[0])
            cnt = int(row[2])
        else:
            cnt = cnt + int(row[2])
    l.append([name, cnt])
    print(name)
    print(cnt)

print(l)
fo = open("frmales.csv", "w")
ll = l[1:len(l)]
print(ll)
for i in ll:
    fo.write(str(i[0]) + "," + str(i[1]) + "\n");

# Cerramos el archivo fichero.txt
fo.close()
