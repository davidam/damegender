#!/usr/bin/python3
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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_utils import DameUtils
import csv
import nltk
from pprint import pprint
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ml', choices=['nltk', 'svc', 'sgd', 'gaussianNB', 'multinomialNB', 'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--dataset', choices=['uk', 'us', 'uy'])
args = parser.parse_args()

nltk.download('names')

g = Gender()

if (args.dataset):
    uspathmales = "files/names/names_us/usmales.csv"
    uspathfemales = "files/names/names_us/usfemales.csv"
    ukpathmales = "files/names/names_uk/ukmales.csv"
    ukpathfemales = "files/names/names_uk/ukfemales.csv"
    uypathmales = "files/names/names_uy/uymales.csv"
    uypathfemales = "files/names/names_uy/uyfemales.csv"
    if (args.dataset == 'uk'):
        with open('files/names/names_uk/ukmales.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader, None)
            males = []
            females = []
            unknowns = []
            for row in reader:
                print(row[0])
                print(g.name_frec(row[0], dataset=args.dataset))
                dicc = g.name_frec(row[0], dataset=args.dataset)
                if (int(dicc['females']) > int(dicc['males'])):
                    females.append(row[0])
                elif (int(dicc['females']) < int(dicc['males'])):
                    males.append(row[0])
                else:
                    unknowns.append(row[0])
            # print(males)
            # print(females)
            # print(unknowns)
        fo = open("files/names/names_uk/ukmales.txt", "w")
        for m in males:
            fo.write(m+"\n")
        fo.close()
#        fo.writelines(males)
        fo2 = open("files/names/names_uk/ukfemales.txt", "w")
        for f in females:
            fo2.write(f+"\n")
        fo2.close()
#        fo2.writelines(females)
        fo3 = open("files/names/names_uk/ukunknown.txt", "w")
        for u in unknowns:
            fo3.write(u+"\n")
        fo3.close()
    if (args.dataset == 'us'):
        with open('files/names/names_us/usmales.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader, None)
            males = []
            females = []
            unknowns = []
            for row in reader:
                print(row[0])
                print(g.name_frec(row[0], dataset=args.dataset))
                dicc = g.name_frec(row[0], dataset=args.dataset)
                if (int(dicc['females']) > int(dicc['males'])):
                    females.append(row[0])
                elif (int(dicc['females']) < int(dicc['males'])):
                    males.append(row[0])
                else:
                    unknowns.append(row[0])
            # print(males)
            # print(females)
            # print(unknowns)
        fo = open("files/names/names_us/usmales.txt", "w")
        for m in males:
            fo.write(m+"\n")
        fo.close()
#        fo.writelines(males)
        fo2 = open("files/names/names_us/usfemales.txt", "w")
        for f in females:
            fo2.write(f+"\n")
        fo2.close()
#        fo2.writelines(females)
        fo3 = open("files/names/names_us/usunknown.txt", "w")
        for u in unknowns:
            fo3.write(u+"\n")
        fo3.close()


if (args.ml):
    s = DameSexmachine()
    if (args.ml == "nltk"):
        guess = s.guess(args.name, binary=True, ml="nltk")
    if (args.ml == "sgd"):
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
    elif (args.ml == "tree"):
        s.tree()
    elif (args.ml == "mlp"):
        s.mlp()

else:

    print("You don't need execute this script in normal conditions. We are going to create some data files, in normal conditions you've downloaded these files cloning the repository. But perhaps you need regenerate these files.")

    yesornot = input("Do you want continue? (Yes/Not) ")

    #print(yesornot)

    if ((yesornot == "Yes") | (yesornot == "yes") | (yesornot == "Y") | (yesornot == "y")):
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
        print("This process has finished. You have the models in files/datamodels/*.sav")

        du = DameUtils()

        print("Creating the file files/names/allnoundefined.csv from files/names/all.csv")
        with open('files/names/all.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            filenou = open('files/names/allnoundefined.csv','w+')
            for row in reader:
                g = du.drop_quotes(row[4])
                if ((g == "m") | (g == "f")):
                    filenou.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+'\n')
            filenou.close()
