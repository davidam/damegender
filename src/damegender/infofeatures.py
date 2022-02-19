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

# DESCRIPTION: returns features with different datasets (corpus)

from app.dame_gender import Gender
import argparse

g = Gender()

parser = argparse.ArgumentParser()
parser.add_argument('corpus', default="es",
                    choices=['at', 'au', 'be', 'ca', 'ch',
                             'cn', 'de', 'dk', 'es', 'fi',
                             'fr', 'gb', 'ie', 'is', 'no', 'nz',
                             'mx', 'pt', 'ru', 'se', 'si',
                             'uy', 'us', 'namdict', 'inter'])
args = parser.parse_args()


# LETTER A
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)['count(a)'] >= 1):
        females = females + 1

nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with letter/s a: %s " % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)['count(a)'] >= 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with letter/s a: %s " % nmales)


# LAST LETTER A
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_a"] == 1):
        females = females + 1
nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with last letter a: %s " % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_a"] == 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with last letter a: %s " % nmales)

# LAST LETTER O
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_o"] == 1):
        females = females + 1
nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with last letter o: %s " % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_o"] == 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with last letter o: %s " % nmales)

# LAST LETTER CONSONANT
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_consonant"] == 1):
        females = females + 1
nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with last letter consonant: %s" % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_consonant"] == 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with last letter consonant: %s" % nmales)


# LAST LETTER VOCAL
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_vocal"] == 1):
        females = females + 1
nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with last letter vocal: %s" % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_vocal"] == 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with last letter vocal: %s" % nmales)
print("---------------------------------------------------------------")

# FIRST LETTER
# print("---------------------------------------------------------------")
# diccfemales = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g":0,
#                "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
#                "ñ": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
#                "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z":0 }

# for i in g.females_list(corpus=args.corpus):
#     if i[0].lower() in 'abcdefghijklmnñopqrstuvwxyz':
#         diccfemales[i[0].lower()] = diccfemales[i[0].lower()] + 1
# print("there are %s females" % len(g.females_list(corpus=args.corpus)))
# print("first letter females dictionary: ")
# listtuples = sorted(diccfemales.items(), reverse=True,  key=lambda x: x[1])
# for elem in listtuples :
#     n = (elem[1] / len(g.females_list(corpus=args.corpus)))
#     print(elem[0] , " ::" , n)

# print("---------------------------------------------------------------")
# diccmales = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g":0, "h": 0,
#              "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "ñ": 0,
#              "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0,
#              "v": 0, "w": 0, "x": 0, "y": 0, "z":0 }

# for i in g.males_list(corpus=args.corpus):
#     if i[0].lower() in 'abcdefghijklmnñopqrstuvwxyz':
#         diccmales[i[0].lower()] = diccmales[i[0].lower()] + 1
# print("there are %s males" % len(g.males_list(corpus=args.corpus)))
# print("first letter males dictionary: ")
# listtuples = sorted(diccmales.items(), reverse=True,  key=lambda x: x[1])
# for elem in listtuples :
#     n = (elem[1] / len(g.males_list(corpus=args.corpus)))
#     print(elem[0] , " ::" , n)

# FIRST LETTER CONSONANT
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_consonant"] == 1):
        females = females + 1
nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with first letter consonant: %s" % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_consonant"] == 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with first letter consonant: %s" % nmales)


# FIRST LETTER VOCAL
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_vocal"] == 1):
        females = females + 1
nfemales = (females / len(g.females_list(corpus=args.corpus)))
print("Females with first letter vocal: %s" % nfemales)

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_vocal"] == 1):
        males = males + 1
nmales = (males / len(g.males_list(corpus=args.corpus)))
print("Males with first letter vocal: %s" % nmales)
