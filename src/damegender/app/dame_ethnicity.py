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
        # ISO 3166
        if ((locale == 'af') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-afganistan.xls.csv', locale="af"))
        if ((locale == 'al') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-albania.xls.csv', locale="al"))
        if ((locale == 'de') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-alemania.xls.csv', locale="de"))
        if ((locale == 'ad') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-andorra.xls.csv', locale="ad"))
        if ((locale == 'dz') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-argelia.xls.csv', locale="dz"))
        if ((locale == 'ar') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-argentina.xls.csv', locale="ar"))
        if ((locale == 'am') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-armenia.xls.csv', locale="am"))
        if ((locale == 'au') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-austria.xls.csv', locale="au"))
        if ((locale == 'az') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-azerbaiyan.xls.csv', locale="az"))
        if ((locale == 'bd') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-bangladesh.xls.csv', locale="bd"))
        if ((locale == 'by') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-belarus.xls.csv', locale="by"))
        if ((locale == 'be') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-belgica.xls.csv', locale="be"))
        if ((locale == 'be') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-belice.xls.csv', locale="be"))
        if ((locale == 'bj') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-benin.xls.csv', locale="bj"))
        if ((locale == 'bo') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-bolivia.xls.csv', locale="bo"))
        if ((locale == 'br') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-brasil.xls.csv', locale="br"))
        if ((locale == 'bg') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-bulgaria.xls.csv', locale="bg"))
        if ((locale == 'bf') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-burkina.xls.csv', locale="bf"))
        if ((locale == 'bf') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-cabo-verde.xls.csv', locale="bf"))
        if ((locale == 'cm') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-camerun.xls.csv', locale="cm"))
        if ((locale == 'ca') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-canada.xls.csv', locale="ca"))
        if ((locale == 'cl') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-chile.xls.csv', locale="cl"))
        if ((locale == 'cn') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-china.xls.csv', locale="cn"))
        if ((locale == 'cy') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-chipre.xls.csv', locale="cy"))
        if ((locale == 'co') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-colombia.xls.csv', locale="co"))
        if ((locale == 'cd') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-congo.xls.csv', locale="cd"))
        if ((locale == 'kp') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-corea-norte.xls.csv', locale="kp"))
            
        return l

    def locale2eng(self, locale):
        # ISO 3166        
        if (locale == 'af'):
            string = 'Afghanistan'
        elif (locale == 'al'):
            string = 'Albania'
        elif (locale == 'de'):
            string = 'Germany'
        elif (locale == 'ad'):
            string = 'Andorra'
        elif (locale == 'dz'):
            string = 'Argelia'                                                
        elif (locale == 'ar'):
            string = 'Argentina'                                                
        elif (locale == 'am'):
            string = 'Armenia'                                                
        elif (locale == 'au'):
            string = 'Austria'                                                
        elif (locale == 'az'):
            string = 'Azerbaiyan'                                                
        elif (locale == 'bd'):
            string = 'Bangladesh'                                                
        elif (locale == 'by'):
            string = 'Belarus'                                                
        elif (locale == 'be'):
            string = 'Belgica'                                                
        elif (locale == 'be'):
            string = 'Belice'                                                
        elif (locale == 'bj'):
            string = 'Benin'                                                
        elif (locale == 'bo'):
            string = 'Bolivia'                                                
        elif (locale == 'br'):
            string = 'Brasil'                                                
        elif (locale == 'bg'):
            string = 'Bulgaria'                                                
        elif (locale == 'cm'):
            string = 'Cameroon'                                                
        elif (locale == 'cm'):
            string = 'Cameroon'                                                
        elif (locale == 'ca'):
            string = 'Canada'
        elif (locale == 'cl'):
            string = 'Chile'                                                
        elif (locale == 'cn'):
            string = 'China'                                                
        elif (locale == 'cy'):
            string = 'Chipre'                                                
        elif (locale == 'co'):
            string = 'Colombia'                                                
        elif (locale == 'cd'):
            string = 'Congo'                                                
        elif (locale == 'kp'):
            string = 'Republic of Korea'                                                
            
        return string

