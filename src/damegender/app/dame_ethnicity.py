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
        if ((locale == 'lb') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-libano.xls.csv', locale="lb"))
        if ((locale == 'lr') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-liberia.xls.csv', locale="lr"))
        if ((locale == 'ly') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-libia.xls.csv', locale="ly"))
        if ((locale == 'lt') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-lituania.xls.csv', locale="lt"))
        if ((locale == 'lu') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-luxemburgo.xls.csv', locale="lu"))
        # if ((locale == 'lu') or (locale == 'all')):
        #     l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-macedonia.xls.csv', locale="lu"))
        if ((locale == 'my') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-malasia.xls.csv', locale="my"))
        if ((locale == 'ml') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-mali.xls.csv', locale="ml"))
        if ((locale == 'mt') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-malta.xls.csv', locale="mt"))
        if ((locale == 'ma') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-marruecos.xls.csv', locale="ma"))
        if ((locale == 'mr') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-mauritania.xls.csv', locale="mr"))
        if ((locale == 'mx') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-mexico.xls.csv', locale="mx"))
        if ((locale == 'md') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-moldavia.xls.csv', locale="md"))
        if ((locale == 'mn') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-mongolia.xls.csv', locale="mn"))
        if ((locale == 'me') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-montenegro.xls.csv', locale="me"))
        if ((locale == 'mz') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-mozambique.xls.csv', locale="mz"))
        if ((locale == 'np') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-nepal.xls.csv', locale="np"))
        if ((locale == 'ni') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-nicaragua.xls.csv', locale="ni"))
        if ((locale == 'ne') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-niger.xls.csv', locale="ne"))
        if ((locale == 'ng') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-nigeria.xls.csv', locale="ng"))
        if ((locale == 'no') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-noruega.xls.csv', locale="no"))
        if ((locale == 'nz') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-nueva-zelanda.xls.csv', locale="nz"))
        if ((locale == 'nl') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-paises-bajos.xls.csv', locale="nl"))
        if ((locale == 'pk') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-pakistan.xls.csv', locale="pk"))
        if ((locale == 'pw') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-palaos.xls.csv', locale="pw"))
        if ((locale == 'ps') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-palestina.xls.csv', locale="ps"))
        if ((locale == 'pa') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-panama.xls.csv', locale="pa"))
        if ((locale == 'py') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-paraguay.xls.csv', locale="py"))
        if ((locale == 'pe') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-peru.xls.csv', locale="pe"))
        if ((locale == 'pl') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-polonia.xls.csv', locale="pl"))
        if ((locale == 'pt') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-portugal.xls.csv', locale="pt"))
        if ((locale == 'gb') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-reino-unido.xls.csv', locale="gb"))
        if ((locale == 'cz') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-republica-checa.xls.csv', locale="cz"))
        if ((locale == 'do') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-republica-dominicana.xls.csv', locale="do"))
        if ((locale == 'rw') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-ruanda.xls.csv', locale="rw"))
        if ((locale == 'ro') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-rumania.xls.csv', locale="ro"))
        if ((locale == 'ru') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-rusia.xls.csv', locale="ru"))
        if ((locale == 'sn') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-senegal.xls.csv', locale="sn"))
        if ((locale == 'rs') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-serbia.xls.csv', locale="rs"))
        if ((locale == 'sl') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-sierra-leona.xls.csv', locale="sl"))
        if ((locale == 'sg') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-singapur.xls.csv', locale="sg"))
        if ((locale == 'sy') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-siria.xls.csv', locale="sy"))
        if ((locale == 'so') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-somalia.xls.csv', locale="so"))
        if ((locale == 'lk') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-sri-lanka.xls.csv', locale="lk"))
        if ((locale == 'za') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-sudafrica.xls.csv', locale="za"))
        if ((locale == 'sd') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-sudan.xls.csv', locale="sd"))
        if ((locale == 'se') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-suecia.xls.csv', locale="se"))
        if ((locale == 'ch') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-suiza.xls.csv', locale="ch"))
        if ((locale == 'th') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-tailandia.xls.csv', locale="th"))
        if ((locale == 'ua') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-ucrania.xls.csv', locale="ua"))
        if ((locale == 'us') or (locale == 'usa') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-usa.xls.csv', locale="us"))
        if ((locale == 'uz') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-uzbekistan.xls.csv', locale="uz"))
        if ((locale == 'uy') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-uruguay.xls.csv', locale="uy"))
        if ((locale == 'ye') or (locale == 'all')):
            l.append(self.locale_match(surname=surname, path='files/inesurnames/apellidos-yemen.xls.csv', locale="ye"))

            
        return l

    def locale2eng(self, locale):
        # ISO 3166        
        if (locale == 'af'):
            string = 'Afghanistan'
        elif (locale == 'al'):
            string = 'Albania'
        elif (locale == 'ad'):
            string = 'Andorra'
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
        elif (locale == 'be'):
            string = 'Belgica'                                                
        elif (locale == 'be'):
            string = 'Belice'
        elif (locale == 'bf'):
            string = 'Burkina Faso'                                                            
        elif (locale == 'bg'):
            string = 'Bulgaria'            
        elif (locale == 'bj'):
            string = 'Benin'
        elif (locale == 'bo'):
            string = 'Bolivia'                                                
        elif (locale == 'br'):
            string = 'Brasil'                                                            
        elif (locale == 'by'):
            string = 'Belarus'
        elif (locale == 'ca'):
            string = 'Canada'            
        elif (locale == 'ci'):
            string = "Côte d'Ivoire"
        elif (locale == 'ch'):
            string = "Switzerland"
        elif (locale == 'cl'):
            string = 'Chile'                                                
        elif (locale == 'cm'):
            string = 'Cameroon'                                                
        elif (locale == 'cn'):
            string = 'China'
        elif (locale == 'co'):
            string = 'Colombia'
        elif (locale == 'cu'):
            string = 'Cuba'            
        elif (locale == 'cy'):
            string = 'Chipre'                                                
        elif (locale == 'cd'):
            string = 'Congo'
        elif (locale == 'cz'):
            string = 'Czech Republic'            
        elif (locale == 'de'):
            string = 'Germany'
        elif (locale == 'dk'):
            string = 'Denmark'
        elif (locale == 'dm'):
            string = 'Dominica'                                                            
        elif (locale == 'do'):
            string = 'Dominican Republic'                                                            
        elif (locale == 'dz'):
            string = 'Argelia'
        elif (locale == 'ec'):
            string = 'Ecuador'
        elif (locale == 'ee'):
            string = 'Republic of Estonia'                                                            
        elif (locale == 'eg'):
            string = 'Egypt'
        elif (locale == 'er'):
            string = 'Eritrea'
        elif (locale == 'et'):
            string = 'Ethiopia'
        elif (locale == 'fi'):
            string = 'Finland'                                                
        elif (locale == 'fr'):
            string = 'France'
        elif (locale == 'gb'):
            string = 'United Kingdom of Great Britain'                                                            
        elif (locale == 'ge'):
            string = 'Georgia'                                                            
        elif (locale == 'gh'):
            string = 'Ghana'
        elif (locale == 'gm'):
            string = 'Gambia'                                                
        elif (locale == 'gn'):
            string = 'Guinea'
        elif (locale == 'gq'):
            string = 'Guinea Ecuatorial'             
        elif (locale == 'gr'):
            string = 'Greece'                                                
        elif (locale == 'gt'):
            string = 'Guatemala'                                                
        elif (locale == 'gw'):
            string = 'Guinea Bissau'
        elif (locale == 'hn'):
            string = 'Honduras'             
        elif (locale == 'ht'):
            string = 'Haití' 
        elif (locale == 'hu'):
            string = 'Hungary'
        elif (locale == 'il'):
            string = 'Israel'
        elif (locale == 'is'):
            string = 'Iceland' 
        elif (locale == 'it'):
            string = 'Italy'
        elif (locale == 'jp'):
            string = 'Japan' 
        elif (locale == 'jo'):
            string = 'Jordan'
        elif (locale == 'ke'):
            string = 'Kenya'
        elif (locale == 'kg'):
            string = 'Kyrgyzstan'
        elif (locale == 'kp'):
            string = 'Democratic Republic of Korea'            
        elif (locale == 'kz'):
            string = 'Kazakhstan'            
        elif (locale == 'kw'):
            string = 'Kuwait'
        elif (locale == 'lb'):
            string = 'Lebanon'            
        elif (locale == 'lr'):
            string = 'Liberia'
        elif (locale == 'lt'):
            string = 'Lithuania'
        elif (locale == 'lu'):
            string = 'Luxembourg'
        elif (locale == 'lv'):
            string = 'Letonia'            
        elif (locale == 'ly'):
            string = 'Libia'
        elif (locale == 'my'):
            string = 'Malaysia'
        elif (locale == 'ml'):
            string = 'Mali'
        elif (locale == 'mt'):
            string = 'Malta'
        elif (locale == 'ma'):
            string = 'Marruecos'
        elif (locale == 'mr'):
            string = 'Mauritania'
        elif (locale == 'mx'):
            string = 'Mexico'
        elif (locale == 'md'):
            string = 'Moldova'
        elif (locale == 'mn'):
            string = 'Mongolia'
        elif (locale == 'me'):
            string = 'Montenegro'
        elif (locale == 'mz'):
            string = 'Mozambique'
        elif (locale == 'nl'):
            string = 'Netherlands'            
        elif (locale == 'np'):
            string = 'Nepal'
        elif (locale == 'ni'):
            string = 'Nicaragua'
        elif (locale == 'ne'):
            string = 'Niger'
        elif (locale == 'ng'):
            string = 'Nigeria'
        elif (locale == 'no'):
            string = 'Noruega'
        elif (locale == 'nz'):
            string = 'Nueva Zelanda'
        elif (locale == 'ph'):
            string = 'Philippines'
        elif (locale == 'pk'):
            string = 'Pakistan'
        elif (locale == 'pw'):
            string = 'Palaos'
        elif (locale == 'ps'):
            string = 'Palestina'
        elif (locale == 'pa'):
            string = 'Panama'
        elif (locale == 'py'):
            string = 'Paraguay'
        elif (locale == 'pe'):
            string = 'Peru'
        elif (locale == 'pl'):
            string = 'Polonia'
        elif (locale == 'pt'):
            string = 'Portugal'            
        elif (locale == 'sb'):
            string = 'Solomon Islands'
        elif (locale == 'se'):
            string = 'Sweden'
        elif (locale == 'sv'):
            string = 'Republic of El Salvador'                                                
        elif (locale == 'si'):
            string = 'Slovenia'
        elif (locale == 'ro'):
            string = 'Romania'                                                
        elif (locale == 'ru'):
            string = 'Russia'                                                
        elif (locale == 'rw'):
            string = 'Rwanda'                                                
        elif (locale == 'ua'):
            string = 'Ukraine'                                                
        elif (locale == 'us'):
            string = 'United States of America'                                                
        elif (locale == 'uy'):
            string = 'Uruguay'                                                
        elif (locale == 'uz'):
            string = 'Republic of Uzbekistan'                                                
        elif (locale == 'ye'):
            string = 'Yemen'                                                
            
        return string

