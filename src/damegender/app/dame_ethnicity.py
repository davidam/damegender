#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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

import csv
from app.dame_utils import DameUtils

class DameEthnicity(object):

    def surname2ethnicity(self, surname):
        du = DameUtils()
        surname = du.drop_accents(surname).upper()
        path = 'files/names/names_us/surnames.csv'
        boolean = False
        with open(path) as csvfile:
            surnamereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(surnamereader, None)
            w, b, api, aian, doublerace, h = ("",)*6
            for row in surnamereader:
#                print(row)
                if (row[0] == surname):
                    # white
                    w = row[5]
                    # black
                    b = row[6]
                    # api = Asian Pacific American
                    api = row[7]
                    # aian = American Indian and Alaska Native
                    aian = row[8]
                    # 2prace
                    doublerace = row[9]
                    # hispanic
                    h = row[10]
        dicc = {"white": w, "black": b, "api": api, "aian": aian, "doublerace": doublerace, "hispanic": h}
        if (dicc == {"white": "", "black": "", "api": "", "aian": "", "doublerace": "", "hispanic": ""}):
            res = False
        else:
            res = dicc
        return res

    def locale_match(self, surname, path, locale):
        du = DameUtils()
        surname = du.drop_accents(surname).upper()
        string = ""
        with open(path) as csvfile:
            freader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(freader, None)
            for row in freader:
                if ((len(row)) == 11):
                    if (surname in row[1]):
                        string = locale
        return string

    def inesurname2ethnicity(self, surname, locale):
        du = DameUtils()
        surname = du.drop_accents(surname).upper()
        l = []
        if (locale == 'af'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-afganistan.xls.csv', locale="af")
            l.append('af')
        elif (locale == 'al'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-albania.xls.csv', locale="al")
            l.append('al')
        elif (locale == 'de'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-alemania.xls.csv', locale="de")
            l.append('de')
        elif (locale == 'ad'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-andorra.xls.csv', locale="ad")
            l.append('ad')
        elif (locale == 'dz'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-argelia.xls.csv', locale="dz")
            l.append('dz')
        elif (locale == 'ar'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-argentina.xls.csv', locale="ar")
            l.append('ar')
        elif (locale == 'am'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-armenia.xls.csv', locale="am")
            l.append('am')
        elif (locale == 'au'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-austria.xls.csv', locale="au")
            l.append('au')
        elif (locale == 'az'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-azerbaiyan.xls.csv', locale="az")
            l.append('az')
        elif (locale == 'bd'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-bangladesh.xls.csv', locale="bd")
            l.append('bd')
        elif (locale == 'by'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-belarus.xls.csv', locale="by")
            l.append('by')
        elif (locale == 'be'):
            self.locale_match(surname=surname, path='files/inesurnames/apellidos-belgica.xls.csv', locale="be")
            l.append('be')


        return l
