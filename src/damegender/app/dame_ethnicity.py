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
        if ((locale == 'ci') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-costa-marfil.xls.csv', locale="ci"))
        if ((locale == 'cr') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-costa-rica.xls.csv', locale="ci"))
        if ((locale == 'hr') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-croacia.xls.csv', locale="hr"))
        if ((locale == 'cu') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-cuba.xls.csv', locale="cu"))
        if ((locale == 'dk') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-dinamarca.xls.csv', locale="dk"))
        if ((locale == 'ec') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-ecuador.xls.csv', locale="ec"))
        if ((locale == 'eg') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-egipto.xls.csv', locale="eg"))
        if ((locale == 'sv') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-el-salvador.xls.csv', locale="sv"))
        if ((locale == 'er') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-eritrea.xls.csv', locale="er"))
        if ((locale == 'si') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-eslovenia.xls.csv', locale="si"))
        if ((locale == 'ee') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-estonia.xls.csv', locale="ee"))
        if ((locale == 'et') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-etiopia.xls.csv', locale="et"))
        if ((locale == 'ph') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-filipinas.xls.csv', locale="ph"))
        if ((locale == 'fi') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-finlandia.xls.csv', locale="fi"))
        if ((locale == 'fr') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-francia.xls.csv', locale="fr"))
        if ((locale == 'gm') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-gambia.xls.csv', locale="gm"))
        if ((locale == 'ge') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-georgia.xls.csv', locale="ge"))
        if ((locale == 'gh') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-ghana.xls.csv', locale="gh"))
        if ((locale == 'gr') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-grecia.xls.csv', locale="gr"))
        if ((locale == 'gt') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-guatemala.xls.csv', locale="gt"))
        if ((locale == 'gw') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-guinea-bissau.xls.csv', locale="gw"))
        if ((locale == 'gq') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-guinea-ecuatorial.xls.csv', locale="gq"))
        if ((locale == 'gn') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-guinea.xls.csv', locale="gn"))
        if ((locale == 'ht') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-haiti.xls.csv', locale="ht"))            
        if ((locale == 'hn') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-honduras.xls.csv', locale="hn"))
        if ((locale == 'hu') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-hungria.xls.csv', locale="hu"))
        if ((locale == 'is') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-islandia.xls.csv', locale="is"))
        if ((locale == 'is') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-israel.xls.csv', locale="is"))
        if ((locale == 'it') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-italia.xls.csv', locale="it"))
        if ((locale == 'jp') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-japon.xls.csv', locale="jp"))
        if ((locale == 'jo') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-jordania.xls.csv', locale="jo"))
        if ((locale == 'kz') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-kazajstan.xls.csv', locale="kz"))
        if ((locale == 'ke') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-kenia.xls.csv', locale="ke"))
        if ((locale == 'kg') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-kirguistan.xls.csv', locale="kg"))
        if ((locale == 'kw') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-kuwait.xls.csv', locale="kw"))
        if ((locale == 'lv') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-letonia.xls.csv', locale="lv"))
            
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
        elif (locale == 'ci'):
            string = "Côte d'Ivoire"
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
            string = 'Democratic Republic of Korea'
        elif (locale == 'cu'):
            string = 'Cuba'                                                            
        elif (locale == 'dk'):
            string = 'Denmark'                                                
        elif (locale == 'dm'):
            string = 'Dominica'                                                
        elif (locale == 'ec'):
            string = 'Ecuador'                                                
        elif (locale == 'eg'):
            string = 'Egypt'                                                
        elif (locale == 'sv'):
            string = 'Republic of El Salvador'                                                
        elif (locale == 'er'):
            string = 'Eritrea'                                                
        elif (locale == 'si'):
            string = 'Slovenia'                                                
        elif (locale == 'sb'):
            string = 'Solomon Islands'                                                
        elif (locale == 'ee'):
            string = 'Republic of Estonia'                                                
        elif (locale == 'et'):
            string = 'Ethiopia'                                                
        elif (locale == 'et'):
            string = 'Ethiopia'                                                
        elif (locale == 'ph'):
            string = 'Philippines'                                                
        elif (locale == 'fi'):
            string = 'Finland'                                                
        elif (locale == 'fr'):
            string = 'France'                                                
        elif (locale == 'gm'):
            string = 'Gambia'                                                
        elif (locale == 'gh'):
            string = 'Ghana'
        elif (locale == 'ge'):
            string = 'Georgia'                                                            
        elif (locale == 'gr'):
            string = 'Greece'                                                
        elif (locale == 'gt'):
            string = 'Guatemala'                                                
        elif (locale == 'gw'):
            string = 'Guinea Bissau' 
        elif (locale == 'gn'):
            string = 'Guinea' 
        elif (locale == 'gq'):
            string = 'Guinea Ecuatorial' 
        elif (locale == 'ht'):
            string = 'Haití' 
        elif (locale == 'hn'):
            string = 'Honduras' 
        elif (locale == 'hu'):
            string = 'Hungary' 
        elif (locale == 'is'):
            string = 'Iceland' 
        elif (locale == 'il'):
            string = 'Israel' 
        elif (locale == 'it'):
            string = 'Italy' 
        elif (locale == 'jp'):
            string = 'Japan' 
        elif (locale == 'jo'):
            string = 'Jordan' 
        elif (locale == 'kz'):
            string = 'Kazakhstan'
        elif (locale == 'ke'):
            string = 'Kenya'
        elif (locale == 'kz'):
            string = 'Kyrgyzstan'
        elif (locale == 'kw'):
            string = 'Kuwait'
        elif (locale == 'lv'):
            string = 'Letonia'
            
        return string

