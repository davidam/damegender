#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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
from app.dame_gender import Gender

g = Gender()

# LETTER A
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["a"] >= 1):
        females = females + 1
#print("Females with last letter a: " + str(females))
print("Females with letter/s a: %s " % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["a"] >= 1):
        males = males + 1
print("Males with letter/s a: %s " % (males/ len(g.males_list())))


# LAST LETTER A
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["last_letter_a"] == 1):
        females = females + 1
#print("Females with last letter a: " + str(females))
print("Females with last letter a: %s " % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["last_letter_a"] == 1):
        males = males + 1
print("Males with last letter a: %s " % (males/ len(g.males_list())))

# LAST LETTER O
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["last_letter_o"] == 1):
        females = females + 1
#print("Females with last letter a: " + str(females))
print("Females with last letter o: %s " % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["last_letter_o"] == 1):
        males = males + 1
print("Males with last letter o: %s " % (males/ len(g.males_list())))

# LAST LETTER CONSONANT
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["last_letter_consonant"] == 1):
        females = females + 1
print("Females with last letter consonant: %s" % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["last_letter_consonant"] == 1):
        males = males + 1
print("Males with last letter consonant: %s" % (males/ len(g.males_list())))


# LAST LETTER VOCAL
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["last_letter_vocal"] == 1):
        females = females + 1
print("Females with last letter vocal: %s" % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["last_letter_vocal"] == 1):
        males = males + 1
print("Males with last letter vocal: %s" % (males/ len(g.males_list())))
print("---------------------------------------------------------------")

# FIRST LETTER CONSONANT
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["first_letter_consonant"] == 1):
        females = females + 1
print("Females with first letter consonant: %s" % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["first_letter_consonant"] == 1):
        males = males + 1
print("Males with first letter consonant: %s" % (males/ len(g.males_list())))

# FIRST LETTER VOCAL
print("---------------------------------------------------------------")
females = 0
for i in g.females_list():
    if (g.features_int(i)["first_letter_vocal"] == 1):
        females = females + 1
print("Females with first letter vocal: %s" % (females/ len(g.females_list())))

males = 0
for i in g.males_list():
    if (g.features_int(i)["first_letter_vocal"] == 1):
        males = males + 1
print("Males with first letter vocal: %s" % (males/ len(g.males_list())))


# # FIRST LETTER VOCAL
# print("---------------------------------------------------------------")
# females = 0
# for i in g.females_list():
#     if (g.features_int(i)["first_letter_vocal"] == 1):
#         females = females + 1
# print("Females with first letter vocal: %s" % (females/ len(g.females_list())))

# males = 0
# for i in g.males_list():
#     if (g.features_int(i)["first_letter_vocal"] == 1):
#         males = males + 1
# print("Males with first letter vocal: %s" % (males/ len(g.males_list())))
# print("---------------------------------------------------------------")


# # LETTER A
# print("---------------------------------------------------------------")
# females = 0
# for i in g.females_list():
#     if (g.features_int(i)["a"] >= 1):
#         females = females + 1
# #print("Females with last letter a: " + str(females))
# print("Females with letter a: %s " % (females/ len(g.females_list())))

# males = 0
# for i in g.males_list():
#     if (g.features_int(i)["a"] >= 1):
#         males = males + 1
# print("Males with letter a: %s " % (males/ len(g.males_list())))


# females = 0
# for i in g.females_list():
#     if (g.features_int(i)["first_letter_vocal"] == 1):
#         females = females + 1
# print("Females with first letter vocal: %s" % (females/ len(g.females_list())))

# males = 0
# for i in g.males_list():
#     if (g.features_int(i)["first_letter_vocal"] == 1):
#         males = males + 1
# print("Males with first letter vocal: %s" % (males/ len(g.males_list())))

# females = 0
# for i in g.females_list():
#     if (g.features_int(i)["first_letter_consonant"] == 1):
#         females = females + 1
# print("Females with first letter vocal: %s" % (females/ len(g.females_list())))

# males = 0
# for i in g.males_list():
#     if (g.features_int(i)["first_letter_consonant"] == 1):
#         males = males + 1
# print("Males with first letter consonant: %s" % (males/ len(g.males_list())))
