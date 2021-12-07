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
import json
from pprint import pprint

# jsontext = '{"fruits": ["apple", "banana", "orange"]}'
# j = json.loads(jsontext);
# print(j)
# print(j['fruits'])

# # Open a file
# fo = open("db.json", "r+")
# print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line


jsondata = open('names_table.jsonl').read()
print(jsondata)

d = json.loads(jsondata)
print("----------------------------------------------------------------")
print(d[0]["text"])
print(d[0]["gender"])
print(d[0]["gender_p"])
print(d[0]["num"])

fof = open("rufemales.csv", "w")
fom = open("rumales.csv", "w")
for i in d:
    if (i["gender"] == "f"):
        fof.write(i["text"] + "," + str(i["num"]) + "\n")
    elif (i["gender"] == "m"):
        fom.write(i["text"] + "," + str(i["num"]) + "\n")
fof.close()
fom.close()           
    
    

# json_object = json.loads(jsondata)
# print("JSON_OBJECT")
# print(json_object)

# with open('db.json') as json_data:
#     d = json.load(json_data)
#     print(d)
#     list1 = d['clients']
#     print("################################## list1: ", list1)
#     print("################################## element 1: ", list1[0])
#     print("################################## element 1 keys: ", list(list1[0].keys()))
#     print("################################## element 1 values: ", list(list1[0].values()))
#     # list2 = d['clients'].values()
#     # print("list2: ", list2)


# jsondata2 = open('genderapifiles_names_min.csv.json').read()
# print("JSONDATA")
# print(jsondata2)
# json_object2 = json.loads(jsondata2)
# print("JSON_OBJECT")
# print(json_object2)

# print(json_object2["names"][0])
# genderlist = []
# for i in json_object2["names"][0]:
#     print(i)
#     print(i['name'])
#     print(i['gender'])
#     genderlist.append(i['gender'])
#     # if (i['gender'] == 'female'):
#     #     genderlistbin.append
# # Close opend file
# #fo.close()
# print(genderlist)
