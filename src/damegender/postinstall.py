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

# DESCRIPTION: This script is oriented about reproducibility in
# Damegender. If you are not interested on it you don't need execute
# it.

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_utils import DameUtils
import csv
import nltk
from pprint import pprint
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ml', choices=['nltk', 'svc', 'sgd', 'gaussianNB',
                                     'multinomialNB', 'bernoulliNB',
                                     'forest', 'tree', 'mlp', 'adaboost'])
parser.add_argument('--dataset', choices=['uk', 'us', 'uy'])
parser.add_argument('--nltk', default=False, action="store_true")
parser.add_argument('--allstuff', default=False, action="store_true")
args = parser.parse_args()

if (args.nltk):
    nltk.download('names')
    nltk.download('punkt')

g = Gender()


def create_file(dataset):
    uspathmales = "files/names/names_us/usmales.csv"
    uspathfemales = "files/names/names_us/usfemales.csv"
    ukpathmales = "files/names/names_gb/ukmales.csv"
    ukpathfemales = "files/names/names_gb/ukfemales.csv"
    uypathmales = "files/names/names_uy/uymasculinos.csv"
    uypathfemales = "files/names/names_uy/uyfemeninos.csv"
    if (dataset == "us"):
        pathmales = uspathmales
        pathfemales = uspathfemales
    elif (dataset == "uk"):
        pathmales = ukpathmales
        pathfemales = ukpathfemales
    elif (dataset == "uy"):
        print("inside")
        pathmales = uypathmales
        pathfemales = uypathfemales

    with open(pathmales) as csvfile:
        print("males")
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader, None)
        males = []
        females = []
        unknowns = []
        for row in reader:
            print(row)
            print(row[0])
            dicc = g.name_frec(row[0], dataset=dataset)
            print(dicc)
            if (int(dicc['females']) > int(dicc['males'])):
                females.append(row[0])
            elif (int(dicc['females']) < int(dicc['males'])):
                males.append(row[0])
            else:
                unknowns.append(row[0])
        print(males)
        print(females)
        fo = open(pathmales, "w")
        for m in males:
            fo.write(m+"\n")
        fo.close()
        fo2 = open(pathfemales, "w")
        for f in females:
            fo2.write(f+"\n")
        fo2.close()


if (args.dataset):
    print(args.dataset)
    create_file(args.dataset)

if (args.ml):
    s = DameSexmachine()
    if (args.ml == "nltk"):
        s.classifier()
    elif (args.ml == "sgd"):
        s.sgd()
    elif (args.ml == "svc"):
        s.svc()
    elif (args.ml == "gaussianNB"):
        s.gaussianNB()
    elif (args.ml == "multinomialNB"):
        s.multinomialNB()
    elif (args.ml == "bernoulliNB"):
        s.bernoulliNB()
    elif (args.ml == "forest"):
        s.forest()
    elif (args.ml == "adaboost"):
        s.adaboost()
    elif (args.ml == "tree"):
        s.tree()
    elif (args.ml == "mlp"):
        s.mlp()

if (args.allstuff):

    print("You don't need execute this script in normal conditions.")
    print("We are going to create some data files")
    print("previously, you've downloaded these files cloning the repository.")
    print("But perhaps you need regenerate these files.")

    yesornot = input("Do you want continue? (Yes/Not) ")

    boolean1 = (yesornot == "Yes") or (yesornot == "yes")
    boolean1 = boolean1 or (yesornot == "Y") or (yesornot == "y")
    if (boolean1):
        print("We are creating files/names/nam_dict_list.txt")
        g.namdict2file()
        print("We are creating .sav files data models in files/datamodels")
        print("This process take a long time, you can rest.")
        s = DameSexmachine()
        s.classifier()
        s.gaussianNB()
        s.svc()
        s.sgd()
        s.multinomialNB()
        s.bernoulliNB()
        s.tree()
        s.mlp()
        print("This process has finished.")
        print("You have the models in files/datamodels/*.sav")

        du = DameUtils()

        print("Creating the file files/names/allnoundefined.csv")
        with open('files/names/all.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            filenou = open('files/names/allnoundefined.csv', 'w+')
            for row in reader:
                g = du.drop_quotes(row[4])
                if ((g == "m") | (g == "f")):
                    string1 = row[0] + ',' + row[1] + ',' + row[2] + ','
                    string1 = string1 + row[3] + ',' + row[4]
                    string1 = string1 + ',' + row[5] + '\n'
                    filenou.write(string1)
            filenou.close()
