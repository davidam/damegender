#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

from app.dame_gender import Gender
import argparse

g = Gender()

parser = argparse.ArgumentParser()
parser.add_argument('corpus', default="ine", choices=['au', 'ca', 'es', 'ine', 'uy', 'uk', 'us', 'luciahelena', 'genderguesser', 'all'])
args = parser.parse_args()


# LETTER A
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)['count(a)'] >= 1):
        females = females + 1
#print("Females with last letter a: " + str(females))
print("Females with letter/s a: %s " % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)['count(a)'] >= 1):
        males = males + 1
print("Males with letter/s a: %s " % (males/ len(g.males_list(corpus=args.corpus))))


# LAST LETTER A
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_a"] == 1):
        females = females + 1
#print("Females with last letter a: " + str(females))
print("Females with last letter a: %s " % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_a"] == 1):
        males = males + 1
print("Males with last letter a: %s " % (males/ len(g.males_list(corpus=args.corpus))))

# LAST LETTER O
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_o"] == 1):
        females = females + 1
#print("Females with last letter a: " + str(females))
print("Females with last letter o: %s " % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_o"] == 1):
        males = males + 1
print("Males with last letter o: %s " % (males/ len(g.males_list(corpus=args.corpus))))

# LAST LETTER CONSONANT
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_consonant"] == 1):
        females = females + 1
print("Females with last letter consonant: %s" % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_consonant"] == 1):
        males = males + 1
print("Males with last letter consonant: %s" % (males/ len(g.males_list(corpus=args.corpus))))


# LAST LETTER VOCAL
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_vocal"] == 1):
        females = females + 1
print("Females with last letter vocal: %s" % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["last_letter_vocal"] == 1):
        males = males + 1
print("Males with last letter vocal: %s" % (males/ len(g.males_list(corpus=args.corpus))))
print("---------------------------------------------------------------")

# FIRST LETTER
# print("---------------------------------------------------------------")
# diccfemales = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g":0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "ñ": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z":0 }

# for i in g.females_list(corpus=args.corpus):
#     if i[0].lower() in 'abcdefghijklmnñopqrstuvwxyz':
#         diccfemales[i[0].lower()] = diccfemales[i[0].lower()] + 1
# print("there are %s females" % len(g.females_list(corpus=args.corpus)))
# print("first letter females dictionary: ")
# listtuples = sorted(diccfemales.items(), reverse=True,  key=lambda x: x[1])
# for elem in listtuples :
#     print(elem[0] , " ::" , (elem[1] / len(g.females_list(corpus=args.corpus))))

# print("---------------------------------------------------------------")
# diccmales = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g":0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "ñ": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z":0 }

# for i in g.males_list(corpus=args.corpus):
#     if i[0].lower() in 'abcdefghijklmnñopqrstuvwxyz':
#         diccmales[i[0].lower()] = diccmales[i[0].lower()] + 1
# print("there are %s males" % len(g.males_list(corpus=args.corpus)))
# print("first letter males dictionary: ")
# listtuples = sorted(diccmales.items(), reverse=True,  key=lambda x: x[1])
# for elem in listtuples :
#     print(elem[0] , " ::" , (elem[1] / len(g.males_list(corpus=args.corpus))))

# FIRST LETTER CONSONANT
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_consonant"] == 1):
        females = females + 1
print("Females with first letter consonant: %s" % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_consonant"] == 1):
        males = males + 1
print("Males with first letter consonant: %s" % (males/ len(g.males_list(corpus=args.corpus))))

# FIRST LETTER VOCAL
print("---------------------------------------------------------------")
females = 0
for i in g.females_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_vocal"] == 1):
        females = females + 1
print("Females with first letter vocal: %s" % (females/ len(g.females_list(corpus=args.corpus))))

males = 0
for i in g.males_list(corpus=args.corpus):
    if (g.features_int(i)["first_letter_vocal"] == 1):
        males = males + 1
print("Males with first letter vocal: %s" % (males/ len(g.males_list(corpus=args.corpus))))
