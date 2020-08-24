#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv
import requests
import json
#import gender_guesser.detector as gender
import os.path
import codecs
from app.dame_gender import Gender


class DameGenderGuesser(Gender):
    COUNTRIES = u"""great_britain ireland usa italy malta portugal spain france
                   belgium luxembourg the_netherlands east_frisia germany austria
                   swiss iceland denmark norway sweden finland estonia latvia
                   lithuania poland czech_republic slovakia hungary romania
                   bulgaria bosniaand croatia kosovo macedonia montenegro serbia
                   slovenia albania greece russia belarus moldova ukraine armenia
                   azerbaijan georgia the_stans turkey arabia israel china india
                   japan korea vietnam other_countries
                 """.split()

    def __init__(self,
                 case_sensitive=True):

        """Creates a detector parsing given data file"""
        self.case_sensitive = case_sensitive
        self._parse("files/names/nam_dict.txt")

    def _parse(self, filename):
        """Opens data file and for each line, calls _eat_name_line"""
        self.names = {}
        with codecs.open(filename, encoding="utf-8") as f:
            for line in f:
                self._eat_name_line(line.strip())

    def _eat_name_line(self, line):
        """Parses one line of data file"""
        if line[0] not in "#=":
            parts = line.split()
            country_values = line[30:-1]
            name = parts[1]
            if not self.case_sensitive:
                name = name.lower()

            if parts[0] == "M":
                self._set(name, u"male", country_values)
            elif parts[0] == "1M" or parts[0] == "?M":
                self._set(name, u"mostly_male", country_values)
            elif parts[0] == "F":
                self._set(name, u"female", country_values)
            elif parts[0] == "1F" or parts[0] == "?F":
                self._set(name, u"mostly_female", country_values)
            elif parts[0] == "?":
                self._set(name, u"andy", country_values)
            else:
                raise "Not sure what to do with a sex of %s" % parts[0]

    def _set(self, name, gender, country_values):
        """Sets gender and relevant country values for names dictionary of detector"""
        if '+' in name:
            for replacement in ['', ' ', '-']:
                self._set(name.replace('+', replacement), gender, country_values)
        else:
            if name not in self.names:
                self.names[name] = {}
            self.names[name][gender] = country_values

    def _most_popular_gender(self, name, counter):
        """Finds the most popular gender for the given name counting by given counter"""
        if name not in self.names:
            return u"unknown"

        max_count, max_tie = (0, 0)
        best = list(self.names[name].keys())[0]
        for gender, country_values in list(self.names[name].items()):
            count, tie = counter(country_values)
            if count > max_count or (count == max_count and tie > max_tie):
                max_count, max_tie, best = count, tie, gender

        return best if max_count > 0 else u"andy"

    def get_gender(self, name, country=None):
        """Returns best gender for the given name and country pair"""
        if not self.case_sensitive:
            name = name.lower()

        if name not in self.names:
            return u"unknown"
        elif not country:
            def counter(country_values):
                country_values = list(map(ord, country_values.replace(" ", "")))
                return (len(country_values),
                        sum([c > 64 and c-55 or c-48 for c in country_values]))
            return self._most_popular_gender(name, counter)
        elif country in self.__class__.COUNTRIES:
            index = self.__class__.COUNTRIES.index(country)
            counter = lambda e: (ord(e[index])-32, 0)
            return self._most_popular_gender(name, counter)
        else:
            raise NoCountryError("No such country: %s" % country)
    
    def guess(self, name, binary=False):
        # guess method to check names dictionary
        genderguesserlist = []
#        d = gender.Detector()
        get = self.get_gender(name)
        if (((get == 'female') or (get == 'mostly_female')) and binary):
            guess = 0
        elif (((get == 'male') or (get == 'mostly_male')) and binary):
            guess = 1
        elif (((get == 'unknown') or (get == 'andy')) and binary):
            guess = 2
        else:
            guess = get
        return guess


    def guess_list(self, path='files/names/partial.csv', binary=False, *args, **kwargs):
        # guess list method
        header = kwargs.get('header', True)
        slist = []
        with open(path) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            if (header == True):
                next(sexreader, None)
            for row in sexreader:
                name = row[0].title()
                name = name.replace('\"', '')
                slist.append(self.guess(name, binary))
        return slist

    
    # def print_confusion_matrix_gender(self, path='files/names/partial.csv', dimensions="2x3"):
    #     cmd = self.confusion_matrix_gender(path, dimensions)
    #     print("[[ %s, %s, %s]" % (cmd[0][0], cmd[0][1], cmd[0][2]))
    #     print(" [ %s, %s, %s]]\n" % (cmd[1][0], cmd[1][1], cmd[1][2]))
    #     return ""
