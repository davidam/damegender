#!/usr/bin/python
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
        dicc = {"white": w,
                "black": b,
                "api": api,
                "aian": aian,
                "doublerace": doublerace,
                "hispanic": h}
        empty_dicc = {"white": "",
                      "black": "",
                      "api": "",
                      "aian": "",
                      "doublerace": "",
                      "hispanic": ""}
        if (dicc == empty_dicc):
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
        l1 = []
        # ISO 3166
        if ((locale == 'af') or (locale == 'all')):
            pathaf = 'files/inesurnames/apellidos-afganistan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathaf,
                                        locale="af"))
        if ((locale == 'al') or (locale == 'all')):
            pathal = 'files/inesurnames/apellidos-albania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathal,
                                        locale="al"))
        if ((locale == 'de') or (locale == 'all')):
            pathde = 'files/inesurnames/apellidos-alemania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathde,
                                        locale="de"))
        if ((locale == 'ad') or (locale == 'all')):
            pathad = 'files/inesurnames/apellidos-andorra.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathad,
                                        locale="ad"))
        if ((locale == 'dz') or (locale == 'all')):
            pathdz = 'files/inesurnames/apellidos-argelia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathdz,
                                        locale="dz"))
        if ((locale == 'ar') or (locale == 'all')):
            pathar = 'files/inesurnames/apellidos-argentina.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathar,
                                        locale="ar"))
        if ((locale == 'am') or (locale == 'all')):
            patham = 'files/inesurnames/apellidos-armenia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=patham,
                                        locale="am"))
        if ((locale == 'au') or (locale == 'all')):
            pathau = 'files/inesurnames/apellidos-austria.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathau,
                                        locale="au"))
        if ((locale == 'az') or (locale == 'all')):
            pathaz = 'files/inesurnames/apellidos-azerbaiyan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathaz,
                                        locale="az"))
        if ((locale == 'bd') or (locale == 'all')):
            pathbd = 'files/inesurnames/apellidos-bangladesh.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbd,
                                        locale="bd"))
        if ((locale == 'by') or (locale == 'all')):
            pathby = 'files/inesurnames/apellidos-belarus.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathby,
                                        locale="by"))
        if ((locale == 'be') or (locale == 'all')):
            pathbe = 'files/inesurnames/apellidos-belgica.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbe,
                                        locale="be"))
        if ((locale == 'bz') or (locale == 'all')):
            pathbz = 'files/inesurnames/apellidos-belice.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbz,
                                        locale="bz"))
        if ((locale == 'bj') or (locale == 'all')):
            pathbj = 'files/inesurnames/apellidos-benin.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbj,
                                        locale="bj"))
        if ((locale == 'bo') or (locale == 'all')):
            pathbo = 'files/inesurnames/apellidos-bolivia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbo,
                                        locale="bo"))
        if ((locale == 'br') or (locale == 'all')):
            pathbr = 'files/inesurnames/apellidos-brasil.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbr,
                                        locale="br"))
        if ((locale == 'bg') or (locale == 'all')):
            pathbg = 'files/inesurnames/apellidos-bulgaria.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbg,
                                        locale="bg"))
        if ((locale == 'bf') or (locale == 'all')):
            pathbf = 'files/inesurnames/apellidos-burkina.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathbf,
                                        locale="bf"))
        if ((locale == 'cv') or (locale == 'all')):
            pathcv = 'files/inesurnames/apellidos-cabo-verde.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcv,
                                        locale="cv"))
        if ((locale == 'cm') or (locale == 'all')):
            pathcm = 'files/inesurnames/apellidos-camerun.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcm,
                                        locale="cm"))
        if ((locale == 'ca') or (locale == 'all')):
            pathca = 'files/inesurnames/apellidos-canada.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathca,
                                        locale="ca"))
        if ((locale == 'cl') or (locale == 'all')):
            pathcl = 'files/inesurnames/apellidos-chile.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcl,
                                        locale="cl"))
        if ((locale == 'cn') or (locale == 'all')):
            pathcn = 'files/inesurnames/apellidos-china.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcn,
                                        locale="cn"))
        if ((locale == 'cy') or (locale == 'all')):
            pathcy = 'files/inesurnames/apellidos-chipre.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcy,
                                        locale="cy"))
        if ((locale == 'co') or (locale == 'all')):
            pathco = 'files/inesurnames/apellidos-colombia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathco,
                                        locale="co"))
        if ((locale == 'cg') or (locale == 'all')):
            pathcg = 'files/inesurnames/apellidos-congo.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcg,
                                        locale="cg"))
        if ((locale == 'kr') or (locale == 'all')):
            pathkr = 'files/inesurnames/apellidos-corea-norte.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathkr,
                                        locale="kr"))
        if ((locale == 'ci') or (locale == 'all')):
            pathci = 'files/inesurnames/apellidos-costa-marfil.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathci,
                                        locale="ci"))
        if ((locale == 'cr') or (locale == 'all')):
            pathcr = 'files/inesurnames/apellidos-costa-rica.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcr,
                                        locale="ci"))
        if ((locale == 'hr') or (locale == 'all')):
            pathhr = 'files/inesurnames/apellidos-croacia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathhr,
                                        locale="hr"))
        if ((locale == 'cu') or (locale == 'all')):
            pathcu = 'files/inesurnames/apellidos-cuba.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcu,
                                        locale="cu"))
        if ((locale == 'dk') or (locale == 'all')):
            pathdk = 'files/inesurnames/apellidos-dinamarca.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathdk,
                                        locale="dk"))
        if ((locale == 'ec') or (locale == 'all')):
            pathec = 'files/inesurnames/apellidos-ecuador.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathec,
                                        locale="ec"))
        if ((locale == 'eg') or (locale == 'all')):
            patheg = 'files/inesurnames/apellidos-egipto.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=patheg,
                                        locale="eg"))
        if ((locale == 'sv') or (locale == 'all')):
            pathsv = 'files/inesurnames/apellidos-el-salvador.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathsv,
                                        locale="sv"))
        if ((locale == 'er') or (locale == 'all')):
            pather = 'files/inesurnames/apellidos-eritrea.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pather,
                                        locale="er"))
        if ((locale == 'si') or (locale == 'all')):
            pathsi = 'files/inesurnames/apellidos-eslovenia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathsi,
                                        locale="si"))
        if ((locale == 'ee') or (locale == 'all')):
            pathee = 'files/inesurnames/apellidos-estonia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathee,
                                        locale="ee"))
        if ((locale == 'et') or (locale == 'all')):
            pathet = 'files/inesurnames/apellidos-etiopia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathet,
                                        locale="et"))
        if ((locale == 'ph') or (locale == 'all')):
            pathph = 'files/inesurnames/apellidos-filipinas.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathph,
                                        locale="ph"))
        if ((locale == 'fi') or (locale == 'all')):
            pathfi = 'files/inesurnames/apellidos-finlandia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathfi,
                                        locale="fi"))
        if ((locale == 'fr') or (locale == 'all')):
            pathfr = 'files/inesurnames/apellidos-francia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathfr,
                                        locale="fr"))
        if ((locale == 'gm') or (locale == 'all')):
            pathgm = 'files/inesurnames/apellidos-gambia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgm,
                                        locale="gm"))
        if ((locale == 'ge') or (locale == 'all')):
            pathge = 'files/inesurnames/apellidos-georgia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathge,
                                        locale="ge"))
        if ((locale == 'gh') or (locale == 'all')):
            pathgh = 'files/inesurnames/apellidos-ghana.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgh,
                                        locale="gh"))
        if ((locale == 'gr') or (locale == 'all')):
            pathgr = 'files/inesurnames/apellidos-grecia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgr,
                                        locale="gr"))
        if ((locale == 'gt') or (locale == 'all')):
            pathgt = 'files/inesurnames/apellidos-guatemala.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgt,
                                        locale="gt"))
        if ((locale == 'gw') or (locale == 'all')):
            pathgw = 'files/inesurnames/apellidos-guinea-bissau.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgw,
                                        locale="gw"))
        if ((locale == 'gq') or (locale == 'all')):
            pathgq = 'files/inesurnames/apellidos-guinea-ecuatorial.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgq,
                                        locale="gq"))
        if ((locale == 'gn') or (locale == 'all')):
            pathgn = 'files/inesurnames/apellidos-guinea.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgn,
                                        locale="gn"))
        if ((locale == 'ht') or (locale == 'all')):
            pathht = 'files/inesurnames/apellidos-haiti.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathht,
                                        locale="ht"))
        if ((locale == 'hn') or (locale == 'all')):
            pathhn = 'files/inesurnames/apellidos-honduras.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathhn,
                                        locale="hn"))
        if ((locale == 'hu') or (locale == 'all')):
            pathhu = 'files/inesurnames/apellidos-hungria.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathhu,
                                        locale="hu"))
        if ((locale == 'is') or (locale == 'all')):
            pathis = 'files/inesurnames/apellidos-islandia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathis,
                                        locale="is"))
        if ((locale == 'il') or (locale == 'all')):
            pathil = 'files/inesurnames/apellidos-israel.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathil,
                                        locale="il"))
        if ((locale == 'it') or (locale == 'all')):
            pathit = 'files/inesurnames/apellidos-italia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathit,
                                        locale="it"))
        if ((locale == 'jp') or (locale == 'all')):
            pathjp = 'files/inesurnames/apellidos-japon.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathjp,
                                        locale="jp"))
        if ((locale == 'jo') or (locale == 'all')):
            pathjo = 'files/inesurnames/apellidos-jordania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathjo,
                                        locale="jo"))
        if ((locale == 'kz') or (locale == 'all')):
            pathkz = 'files/inesurnames/apellidos-kazajstan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathkz,
                                        locale="kz"))
        if ((locale == 'ke') or (locale == 'all')):
            pathke = 'files/inesurnames/apellidos-kenia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathke,
                                        locale="ke"))
        if ((locale == 'kg') or (locale == 'all')):
            pathkg = 'files/inesurnames/apellidos-kirguistan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathkg,
                                        locale="kg"))
        if ((locale == 'kw') or (locale == 'all')):
            pathkw = 'files/inesurnames/apellidos-kuwait.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathkw,
                                        locale="kw"))
        if ((locale == 'lv') or (locale == 'all')):
            pathlv = 'files/inesurnames/apellidos-letonia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathlv,
                                        locale="lv"))
        if ((locale == 'lb') or (locale == 'all')):
            pathlb = 'files/inesurnames/apellidos-libano.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathlb,
                                        locale="lb"))
        if ((locale == 'lr') or (locale == 'all')):
            pathlr = 'files/inesurnames/apellidos-liberia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathlr,
                                        locale="lr"))
        if ((locale == 'ly') or (locale == 'all')):
            pathly = 'files/inesurnames/apellidos-libia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathly,
                                        locale="ly"))
        if ((locale == 'lt') or (locale == 'all')):
            pathlt = 'files/inesurnames/apellidos-lituania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathlt,
                                        locale="lt"))
        if ((locale == 'lu') or (locale == 'all')):
            pathlu = 'files/inesurnames/apellidos-luxemburgo.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathlu,
                                        locale="lu"))
        if ((locale == 'my') or (locale == 'all')):
            pathmy = 'files/inesurnames/apellidos-malasia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmy,
                                        locale="my"))
        if ((locale == 'ml') or (locale == 'all')):
            pathml = 'files/inesurnames/apellidos-mali.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathml,
                                        locale="ml"))
        if ((locale == 'mt') or (locale == 'all')):
            pathmt = 'files/inesurnames/apellidos-malta.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmt,
                                        locale="mt"))
        if ((locale == 'ma') or (locale == 'all')):
            pathma = 'files/inesurnames/apellidos-marruecos.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathma,
                                        locale="ma"))
        if ((locale == 'mr') or (locale == 'all')):
            pathmr = 'files/inesurnames/apellidos-mauritania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmr,
                                        locale="mr"))
        if ((locale == 'mx') or (locale == 'all')):
            pathmx = 'files/inesurnames/apellidos-mexico.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmx,
                                        locale="mx"))
        if ((locale == 'md') or (locale == 'all')):
            pathmd = 'files/inesurnames/apellidos-moldavia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmd,
                                        locale="md"))
        if ((locale == 'mn') or (locale == 'all')):
            pathmn = 'files/inesurnames/apellidos-mongolia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmn,
                                        locale="mn"))
        if ((locale == 'me') or (locale == 'all')):
            pathme = 'files/inesurnames/apellidos-montenegro.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathme,
                                        locale="me"))
        if ((locale == 'mz') or (locale == 'all')):
            pathmz = 'files/inesurnames/apellidos-mozambique.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathmz,
                                        locale="mz"))
        if ((locale == 'np') or (locale == 'all')):
            pathnp = 'files/inesurnames/apellidos-nepal.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathnp,
                                        locale="np"))
        if ((locale == 'ni') or (locale == 'all')):
            pathni = 'files/inesurnames/apellidos-nicaragua.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathni,
                                        locale="ni"))
        if ((locale == 'ne') or (locale == 'all')):
            pathne = 'files/inesurnames/apellidos-niger.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathne,
                                        locale="ne"))
        if ((locale == 'ng') or (locale == 'all')):
            pathng = 'files/inesurnames/apellidos-nigeria.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathng,
                                        locale="ng"))
        if ((locale == 'no') or (locale == 'all')):
            pathno = 'files/inesurnames/apellidos-noruega.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathno,
                                        locale="no"))
        if ((locale == 'nz') or (locale == 'all')):
            pathnz = 'files/inesurnames/apellidos-nueva-zelanda.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathnz,
                                        locale="nz"))
        if ((locale == 'nl') or (locale == 'all')):
            pathnl = 'files/inesurnames/apellidos-paises-bajos.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathnl,
                                        locale="nl"))
        if ((locale == 'pk') or (locale == 'all')):
            pathpk = 'files/inesurnames/apellidos-pakistan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpk,
                                        locale="pk"))
        if ((locale == 'pw') or (locale == 'all')):
            pathpw = 'files/inesurnames/apellidos-palaos.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpw,
                                        locale="pw"))
        if ((locale == 'ps') or (locale == 'all')):
            pathps = 'files/inesurnames/apellidos-palestina.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathps,
                                        locale="ps"))
        if ((locale == 'pa') or (locale == 'all')):
            pathpa = 'files/inesurnames/apellidos-panama.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpa,
                                        locale="pa"))
        if ((locale == 'py') or (locale == 'all')):
            pathpy = 'files/inesurnames/apellidos-paraguay.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpy,
                                        locale="py"))
        if ((locale == 'pe') or (locale == 'all')):
            pathpe = 'files/inesurnames/apellidos-peru.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpe,
                                        locale="pe"))
        if ((locale == 'pl') or (locale == 'all')):
            pathpl = 'files/inesurnames/apellidos-polonia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpl,
                                        locale="pl"))
        if ((locale == 'pt') or (locale == 'all')):
            pathpt = 'files/inesurnames/apellidos-portugal.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathpt,
                                        locale="pt"))
        if ((locale == 'gb') or (locale == 'all')):
            pathgb = 'files/inesurnames/apellidos-reino-unido.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathgb,
                                        locale="gb"))
        if ((locale == 'cz') or (locale == 'all')):
            pathcz = 'files/inesurnames/apellidos-republica-checa.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathcz,
                                        locale="cz"))
        if ((locale == 'do') or (locale == 'all')):
            pathdo = 'files/inesurnames/apellidos-republica-dominicana.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathdo,
                                        locale="do"))
        if ((locale == 'rw') or (locale == 'all')):
            pathrw = 'files/inesurnames/apellidos-ruanda.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathrw,
                                        locale="rw"))
        if ((locale == 'ro') or (locale == 'all')):
            pathro = 'files/inesurnames/apellidos-rumania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathro,
                                        locale="ro"))
        if ((locale == 'ru') or (locale == 'all')):
            pathru = 'files/inesurnames/apellidos-rusia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathru,
                                        locale="ru"))
        if ((locale == 'sn') or (locale == 'all')):
            pathsn = 'files/inesurnames/apellidos-senegal.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathsn,
                                        locale="sn"))
        if ((locale == 'rs') or (locale == 'all')):
            pathrs = 'files/inesurnames/apellidos-serbia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathrs,
                                        locale="rs"))
        if ((locale == 'sl') or (locale == 'all')):
            pathsl = 'files/inesurnames/apellidos-sierra-leona.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=pathsl,
                                        locale="sl"))
        if ((locale == 'sg') or (locale == 'all')):
            sgpath = 'files/inesurnames/apellidos-singapur.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=sgpath,
                                        locale="sg"))
        if ((locale == 'sy') or (locale == 'all')):
            sypath = 'files/inesurnames/apellidos-siria.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=sypath,
                                        locale="sy"))
        if ((locale == 'so') or (locale == 'all')):
            sopath = 'files/inesurnames/apellidos-somalia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=sopath,
                                        locale="so"))
        if ((locale == 'lk') or (locale == 'all')):
            lkpath = 'files/inesurnames/apellidos-sri-lanka.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=lkpath,
                                        locale="lk"))
        if ((locale == 'za') or (locale == 'all')):
            zapath = 'files/inesurnames/apellidos-sudafrica.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=zapath,
                                        locale="za"))
        if ((locale == 'sd') or (locale == 'all')):
            sdpath = 'files/inesurnames/apellidos-sudan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=sdpath,
                                        locale="sd"))
        if ((locale == 'se') or (locale == 'all')):
            sepath = 'files/inesurnames/apellidos-suecia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=sepath,
                                        locale="se"))
        if ((locale == 'ch') or (locale == 'all')):
            chpath = 'files/inesurnames/apellidos-suiza.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=chpath,
                                        locale="ch"))
        if ((locale == 'th') or (locale == 'all')):
            thpath = 'files/inesurnames/apellidos-tailandia.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=thpath,
                                        locale="th"))
        if ((locale == 'ua') or (locale == 'all')):
            uapath = 'files/inesurnames/apellidos-ucrania.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=uapath,
                                        locale="ua"))
        if ((locale == 'us') or (locale == 'usa') or (locale == 'all')):
            usapath = 'files/inesurnames/apellidos-usa.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=usapath,
                                        locale="us"))
        if ((locale == 'uz') or (locale == 'all')):
            uzpath = 'files/inesurnames/apellidos-uzbekistan.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=uzpath,
                                        locale="uz"))
        if ((locale == 'uy') or (locale == 'all')):
            uypath = 'files/inesurnames/apellidos-uruguay.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=uypath,
                                        locale="uy"))
        if ((locale == 'ye') or (locale == 'all')):
            yepath = 'files/inesurnames/apellidos-yemen.xls.csv'
            l1.append(self.locale_match(surname=surname,
                                        path=yepath,
                                        locale="ye"))
        return l1

    def dicc_iso3166_to_eng(self):
        dicc = {"ad": "Andorra",
                "ae": "United Arab Emirates",
                "af": "Afghanistan",
                "ag": "Antigua and Barbuda",
                "al": "Albania",
                "ao": "Angola",
                "am": "Armenia",
                "ar": "Argentina",
                "at": "Austria",
                "au": "Australia",
                "az": "Azerbaiyan",
                "ba": "Bosnia and Herzegovina",
                "bb": "Barbados",
                "bd": "Bangladesh",
                "be": "Belgium",
                "bf": "Burkina Faso",
                "bg": "Bulgaria",
                "bh": "Bahrain",
                "bi": "Burundi",
                "bj": "Republic of Benin",
                "bn": "Brunei Darussalam",
                "bo": "Bolivia",
                "br": "Brazil",
                "bs": "Bahamas",
                "bt": "Bhutan",
                "bw": "Bostwana",
                "by": "Belarus",
                "bz": "Belize",
                "ca": "Canada",
                "cd": "Democratic Republic of the Congo",
                "cf": "Central African Republic",
                "cg": "Congo",
                "ch": "Switzerland",
                "ci": "Côte d'Ivoire",
                "cl": "Chile",
                "cm": "Cameroon",
                "cn": "China",
                "co": "Colombia",
                "cr": "Costa Rica",
                "cu": "Cuba",
                "cv": "Cabo Verde",
                "cy": "Cyprus",
                "cz": "Czech Republic",
                "de": "Germany",
                "dj": "Dijbouti",
                "dk": "Denmark",
                "dm": "Dominica",
                "do": "Dominican Republic",
                "dz": "Algeria",
                "ec": "Ecuador",
                "ee": "Estonia",
                "eg": "Egypt",
                "er": "Eritrea",
                "es": "Spain",
                "et": "Ethiopia",
                "fi": "Finland",
                "fj": "Fiji",
                "fm": "Federated States of Micronesia",
                "fr": "France",
                "ga": "Gabon",
                "gb": "United Kingdom of Great Britain",
                "ge": "Georgia",
                "gh": "Ghana",
                "gm": "Gambia",
                "gn": "Guinea",
                "gq": "Republic of Equatorial Guinea",
                "gr": "Greece",
                "gt": "Guatemala",
                "gw": "Guinea Bissau",
                "gy": "Guyana",
                "hn": "Honduras",
                "hr": "Croatia",
                "ht": "Haiti",
                "hu": "Hungary",
                "id": "Indonesia",
                "ie": "Ireland",
                "il": "Israel",
                "in": "India",
                "iq": "Iraq",
                "ir": "Islamic Republic of Iran",
                "is": "Iceland",
                "it": "Italy",
                "jm": "Jamaica",
                "jo": "Jordan",
                "jp": "Japan",
                "ke": "Kenya",
                "kg": "Kyrgyzstan",
                "kh": "Cambodia",
                "ki": "Kiribati",
                "km": "Union of the Comoros",
                "kn": "Saint Kitts and Nevis",
                "kp": "Democratic Republic of Korea",
                "kw": "Kuwait",
                "kz": "Kazakhstan",
                "la": "Lao People's Democratic Republic",
                "lb": "Lebanon",
                "lc": "Saint Lucia",
                "li": "Liechtenstein",
                "lk": "Sri Lanka",
                "lr": "Liberia",
                "ls": "Lesotho",
                "lt": "Lithuania",
                "lu": "Luxembourg",
                "lv": "Letonia",
                "ly": "Libia",
                "ma": "Morocco",
                "mc": "Monaco",
                "md": "Moldova",
                "me": "Montenegro",
                "mg": "Madagascar",
                "mh": "Marshall Islands",
                "mk": "North Macedonia",
                "ml": "Mali",
                "mm": "Myanmar",
                "mn": "Mongolia",
                "mr": "Mauritania",
                "mt": "Malta",
                "mu": "Mauritius",
                "mv": "Maldives",
                "mw": "Malawi",
                "mx": "Mexico",
                "my": "Malasya",
                "mz": "Mozambique",
                "na": "Namibia",
                "ne": "Republic of Niger",
                "ng": "Nigeria",
                "ni": "Nicaragua",
                "nl": "Netherlands",
                "no": "Norway",
                "np": "Nepal",
                "nr": "Republic of Nauru",
                "nz": "New Zealand",
                "om": "Oman",
                "pa": "Panama",
                "pe": "Peru",
                "pg": "Papua New Guinea",
                "ph": "Philippines",
                "pk": "Pakistan",
                "pl": "Polonia",
                "pt": "Portugal",
                "pw": "Palaos",
                "py": "Paraguay",
                "qa": "Qatar",
                "ro": "Romania",
                "rs": "Republic of Serbia",
                "ru": "Russia",
                "rw": "Rwanda",
                "sa": "Saudi Arabia",
                "sb": "Solomon Islands",
                "sc": "Seychelles",
                "sd": "Sudan",
                "se": "Sweden",
                "sg": "Singapore",
                "si": "Slovenia",
                "sk": "Slovakia",
                "sl": "Sierra Leona",
                "sm": "San Marino",
                "sn": "Senegal",
                "so": "Somalia",
                "sr": "Suriname",
                "ss": "South Sudan",
                "st": "Sao Tome and Principe",
                "sv": "Republic of El Salvador",
                "sy": "The Syrian Arab Republic",
                "sz": "Eswatini",
                "td": "The Republic of Chad",
                "tg": "Togo",
                "th": "Thailand",
                "tj": "Tajikistan",
                "tl": "The Democratic Republic of Timor-Leste",
                "tm": "Turkemistan",
                "tn": "The Republic of Tunisia",
                "to": "Tonga",
                "tr": "Turkey",
                "tt": "Trinidad and Tobago",
                "tv": "Tuvalu",
                "tw": "Taiwan",
                "tz": "Tanzania",
                "ua": "Ukraine",
                "ug": "Uganda",
                "us": "United States of America",
                "uy": "Uruguay",
                "uz": "Republic of Uzbekistan",
                "va": "Holy See",
                "vc": "Saint Vicent and the Grenadines",
                "ve": "Venezuela",
                "vn": "Vietnam",
                "vu": "Vanuatu",
                "ws": "Samoa",
                "ye": "Yemen",
                "za": "South Africa",
                "zm": "Zambia",
                "zw": "Zimbabwe"
                }
        return dicc

    def iso3166_to_eng(self, locale):
        dicc = self.dicc_iso3166_to_eng()
        return dicc[locale]
