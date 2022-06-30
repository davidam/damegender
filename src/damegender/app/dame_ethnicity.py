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

    def dicc_iso639_2(self):
        # giving 3 letters returns a list with the language
        # in english, french and german
        dicc = {"aar": ["Afar", "afar", "Danakil-Sprache"],
                "abk": ["Abkhazian", "abkhaze", "Abchasisch"],
                "ace": ["Achinese", "aceh", "Aceh-Sprache"],
                "ach": ["Acoli", "acoli", "Acholi-Sprache"],
                "ada": ["Adangme", "adangme", "Adangme-Sprache"],
                "ady": [["Adyghe", "Adygei"], "adyghé", "Adygisch"],
                "afa": ["Afro-Asiatic languages", "afro-asiatiques, langues",
                        "Hamitosemitische Sprachen (Andere)"],
                "afh": ["Afrihili", "afrihili",        "Afrihili"],
                "afr": ["Afrikaans", "afrikaans", "Afrikaans"],
                "ain": ["Ainu", "aïnou", "Ainu-Sprache"],
                "aka": ["Akan", "akan", "Akan-Sprache"],
                "akk": ["Akkadian", "akkadien", "Akkadisch"],
                "alb": ["Albanian", "albanais", "Albanisch"],
                "ale": ["Aleut", "aléoute", "Aleutisch"],
                "alg": ["Algonquian languages", "algonquines, langues",
                        "Algonkin-Sprachen (Andere)"],
                "alt": ["Southern Altai", "altai du Sud", "Altaisch"],
                "amh": ["Amharic", "amharique", "Amharisch"],
                "ang": ["English, Old (ca.450-1100)",
                        "anglo-saxon (ca.450-1100)",
                        "Altenglisch"],
                "anp": ["Angika", "angika", "Anga-Sprache"],
                "apa": ["Apache languages", "angika", "Anga-Sprache"],
                "ara": ["Arabic", "arabe", "Arabisch"],
                "arc": [["Official Aramaic (700-300 BCE)",
                         "Imperial Aramaic (700-300 BCE)"],
                        "araméen d'empire (700-300 BCE)", "Aramäisch"],
                "arg": ["Aragonese", "aragonais", "Aragonesisch"],
                "arm": ["Armenian", "arménien", "Armenisch"],
                "arn": [["Mapudungun", "Mapuche mapudungun"],
                        ["mapuche", "mapuce"],
                        "Arauka-Sprachen"],
                "arp": ["Arapaho", "arapaho", "Arapaho-Sprache"],
                "art": ["Artificial languages",
                        "artificielles, langues",
                        "Kunstsprachen (Andere)"],
                "arw": ["Arawak", "arawak", "Arawak-Sprachen"],
                "asm": ["Assamese", "assamais", "Assamesisch"],
                "ast": [["Asturian", "Bable", "Leonese", "Asturleonese"],
                        ["asturien", "bable", "léonais", "asturoléonais"],
                        "Asturisch"],
                "ath": ["Athapascan languages",
                        "athapascanes , langues",
                        "Athapaskische Sprachen (Andere)"],
                "aus": ["Australian languages",
                        "australiennes , langues",
                        "Australische Sprachen"],
                "ava": ["Avaric", "avar", "Awarisch"],
                "ave": ["Avestan", "avestique", "Avestisch"],
                "awa": ["Awadhi", "awadhi", "Awadhi"],
                "aym": ["Aymara", "aymara", "Aymará-Sprache"],
                "aze": ["Azerbaijani", "azéri", "Aserbeidschanisch"],
                "bad": ["Banda languages",
                        "banda, langues",
                        "Banda-Sprachen (Ubangi-Sprachen)"],
                "bai": ["Bamileke languages",
                        "bamiléké, langues",
                        "Bamileke-Sprachen"],
                "bak": ["Bashkir", "bachkir", "Baschkirisch"],
                "bal": ["Baluchi", "baloutchi", "Belutschisch"],
                "bam": ["Bambara", "bambara", "Bambara-Sprache"],
                "ban": ["Balinese", "balinais", "Balinesisch"],
                "baq": ["Basque", "basque", "Baskisch"],
                "bas": ["Basa", "basa", "Basaa-Sprache"],
                "bat": ["Baltic languages", "baltes",
                        "langues Baltische Sprachen (Andere)"],
                "bej": [["Beja", "Bedawiyet"], "bedja", "Bedauye"],
                "bel": ["Belarusian", "biélorusse", "Weißrussisch"],
                "bem": ["Bemba", "bemba", "Bemba-Sprache"],
                "ben": ["Bengali", "bengali", "Bengali"],
                "ber": ["Berber languages",
                        "berbères, langues",
                        "Berbersprachen (Andere)"],
                "bho": ["Bhojpuri", "bhojpuri", "Bhojpuri"],
                "bih": ["Bihari languages",
                        "langues biharis",
                        "Bihari (Andere)"],
                "bik": ["Bikol", "bikol", "Bikol-Sprache"],
                "bin": [["Bini", "Edo"], ["bini", "edo"], "Edo-Sprache"],
                "bis": ["Bislama", "bichlamar", "Beach-la-mar"],
                "bla": ["Siksika", "blackfoot", "Blackfoot-Sprache"],
                "bnt": ["Bantu languages",
                        "bantou, langues",
                        "Bantusprachen (Andere)"],
                "bod": ["Tibetan", "tibétain", "Tibetisch"],
                "bos": ["Bosnian", "bosniaque", "Bosnisch"],
                "bra": ["Braj", "braj", "Braj-Bhakha"],
                "bre": ["Breton", "breton", "Bretonisch"],
                "btk": ["Batak languages", "batak, langues", "Batak-Sprache"],
                "bua": ["Buriat", "bouriate", "Burjatisch"],
                "bug": ["Buginese", "bugi", "Bugi-Sprache"],
                "bul": ["Bulgarian", "bulgare", "Bulgarisch"],
                "bur": ["Burmese", "birman", "Birmanisch"],
                "byn": [["Blin", "Bilin"], ["blin", "bilen"], "Bilin-Sprache"],
                "cad": ["BurmCaddoese", "caddo", "Caddo-Sprachen"],
                "cai": ["Central American Indian languages",
                        "amérindiennes de l'Amérique centrale, langues",
                        "Indianersprachen, Zentralamerika (Andere)"],
                "car": ["Galibi Carib",
                        ["karib", "galibi", "carib"],
                        "Karibische Sprachen"],
                "cat": [["Catalan", "Valencian"],
                        ["catalan", "valencien"],
                        "Katalanisch"],
                "cau": ["Caucasian languages", "caucasiennes, langues",
                        "Kaukasische Sprachen (Andere)"],
                "ceb": ["Cebuano", "cebuano", "Cebuano"],
                "cel": ["Celtic languages",
                        ["celtiques, langues", "celtes, langues"],
                        "Keltische Sprachen"],
                "cze": ["Czech", "tchèque", "Tschechisch"],
                "ces": ["Czech", "tchèque", "Tschechisch"],
                "cha": ["Chamorro", "chamorro", "Chamorro-Sprache"],
                "chb": ["Chibcha", "chibcha", "Chibcha-Sprachen"],
                "che": ["Chechen", "tchétchène", "Tschetschenisch"],
                "chg": ["Chagatai", "djaghataï", "Tschagataisch"],
                "chi": ["Chinese", "chinois", "Chinesisch"],
                "chk": ["Chuukese", "chuuk", "Trukesisch"],
                "chm": ["Mari", "mari", "Tscheremissisch"],
                "chn": ["Chinook jargon", "chinook, jargon", "Chinook-Jargon"],
                "cho": ["Choctaw", "choctaw", "Choctaw-Sprache"],
                "chp": [["Chipewyan", "Dene Suline"],
                        "chipewyan",
                        "Chipewyan-Sprache"],
                "chr": ["Cherokee", "cherokee", "Cherokee-Sprache"],
                "chu": [["Church Slavic",
                         "Old Slavonic",
                         "Church Slavonic",
                         "Old Bulgarian",
                         "Old Church Slavonic"],
                        ["slavon d'église",
                         "vieux slave",
                         "slavon liturgique",
                         "vieux bulgare"],
                        "Kirchenslawisch"],
                "chv": ["Chuvash", "tchouvache", "Tschuwaschisch"],
                "chy": ["Cheyenne", "cheyenne", "Cheyenne-Sprache"],
                "ces": ["Czech", "tchèque", "Tschechisch"],
                "cmc": ["Chamic languages",
                        "chames, langues",
                        "Cham-Sprachen"],
                "cnr": ["CheMontenegrinyenne",
                        "monténégrin",
                        "Montenegrinisch"],
                "cop": ["Coptic", "copte", "Koptisch"],
                "cor": ["Cornish", "cornique", "Kornisch"],
                "cos": ["Corsican", "corse", "Korsisch"],
                "cpe": ["Creoles and pidgins, English based",
                        "créoles et pidgins basés sur l'anglais",
                        "Kreolisch-Englisch (Andere)"],
                "cpf": ["Creoles and pidgins, French-based",
                        "créoles et pidgins basés sur le français",
                        "Kreolisch-Französisch (Andere)"],
                "cpp": ["Creoles and pidgins, Portuguese-based",
                        "créoles et pidgins basés sur le portugais",
                        "Kreolisch-Portugiesisch (Andere)"],
                "cre": ["Cree", "cree", "Cree-Sprache"],
                "crh": [["Crimean Tatar", "Crimean Turkish"],
                        "tatar de Crimé",
                        "Krimtatarisch"],
                "crp": ["Creoles and pidgins",
                        "créoles et pidgins",
                        ["Kreolische Sprachen", "Pidginsprachen (Andere)"]],
                "csb": ["Kashubian", "kachoube", "Kaschubisch"],
                "cus": ["Cushitic languages",
                        "couchitiques, langues",
                        "Kuschitische Sprachen (Andere)"],
                "cym": ["Welsh", "gallois", "Kymrisch"],
                "cze": ["Czech", "tchèque", "Tschechisch"],
                "dak": ["Dakota", "dakota", "Dakota-Sprache"],
                "dan": ["Danish", "danois", "Dänisch"],
                "dar": ["Dargwa", "dargwa", "Darginisch"],
                "day": ["Land Dayak languages",
                        "dayak, langues",
                        "Dajakisch"],
                "del": ["Delaware", "delaware", "Delaware-Sprache"],
                "den": ["Slave (Athapascan)",
                        "esclave (athapascan)",
                        "Slave-Sprache"],
                "deu": ["German", "allemand", "Deutsch"],
                "dgr": ["Dogrib", "dogrib", "Dogrib-Sprache"],
                "din": ["Dinka", "dinka", "Dinka-Sprache"],
                "div": [["Divehi", "Dhivehi", "Maldivian"],
                        "maldivien", "Maledivisch"],
                "doi": ["Dogri", "dogri", "Dogri"],
                "dra": ["Dravidian languages",
                        "dravidiennes, langues",
                        "Drawidische Sprachen (Andere)"],
                "dsb": ["Lower Sorbian",
                        "bas-sorabe",
                        "Niedersorbisch"],
                "dua": ["Duala", "douala", "Duala-Sprachen"],
                "dum": ["Dutch, Middle (ca.1050-1350)",
                        "néerlandais moyen (ca. 1050-1350)",
                        "Mittelniederländisch"],
                "dut": [["Dutch", "Flemish"],
                        ["néerlandais", "flamand"],
                        "Niederländisch"],
                "dyu": ["Dyula", "dioula", "Dyula-Sprache"],
                "dzo": ["Dzongkha", "dzongkha", "Dzongkha"],
                "efi": ["Efik", "efik", "Efik"],
                "egy": ["Egyptian (Ancient)", "égyptien", "Ägyptisch"],
                "eka": ["Ekajuk", "ekajuk", "Ekajuk"],
                "ell": ["Greek, Modern (1453-)",
                        "grec moderne (après 1453)",
                        "Neugriechisch"],
                "elx": ["Elamite", "élamite", "Elamisch"],
                "eng": ["English", "anglais", "Englisch"],
                "enm": ["English, Middle (1100-1500)",
                        "anglais moyen (1100-1500)",
                        "Mittelenglisch"],
                "epo": ["Esperanto", "espéranto", "Esperanto"],
                "est": ["Estonian", "estonien", "Estnisch"],
                "eus": ["Basque", "basque", "Baskisch"],
                "ewe": ["Ewe", "éwé", "Ewe-Sprache"],
                "ewo": ["Ewondo", "éwondo", "Ewondo"],
                "fan": ["Fang", "fang", "Pangwe-Sprache"],
                "fao": ["Faroese", "féroïen", "Färöisch"],
                "fas": ["Persian", "persan", "Persisch"],
                "fat": ["Fanti", "fanti", "Fante-Sprache"],
                "fij": ["Fijian", "fidjien", "Fidschi-Sprache"],
                "fil": [["Filipino", "Pilipino"],
                        ["filipino", "pilipino"],
                        "Pilipino"],
                "fin": ["Finnish", "finnois", "Finnisch"],
                "fiu": ["Finno-Ugrian languages",
                        "finno-ougriennes, langues",
                        "Finnougrische Sprachen (Andere)"],
                "fon": ["Fon", "fon", "Fon-Sprache"],
                "fre": ["French", "français", "Französisch"],
                "fra": ["French", "français", "Französisch"],
                "frm": ["French, Middle (ca.1400-1600)",
                        "français moyen (1400-1600)",
                        "Mittelfranzösisch"],
                "fro": ["French, Old (842-ca.1400)",
                        "français ancien (842-ca.1400)",
                        "Altfranzösisch"],
                "frr": ["Northern Frisian",
                        "frison septentrional",
                        "Nordfriesisch"],
                "frs": ["Eastern Frisian", "frison oriental", "Ostfriesisch"],
                "fry": ["Western Frisian", "frison occidental", "Friesisch"],
                "ful": ["Fulah", "peul", "Ful"],
                "fur": ["Friulian", "frioulan", "Friulisch"],
                "gaa": ["Ga", "ga", "Ga-Sprache"],
                "gay": ["Gayo", "gayo", "Gayo-Sprache"],
                "gba": ["Gbaya", "gbaya", "Gbaya-Sprache"],
                "gem": ["Germanic languages",
                        "germaniques, langues",
                        "Germanische Sprachen (Andere)"],
                "geo": ["Georgian", "géorgien", "Georgisch"],
                "ger": ["German", "allemand", "Deutsch"],
                "gez": ["Geez", "guèze", "Altäthiopisch"],
                "gil": ["Gilbertese", "kiribati", "Gilbertesisch"],
                "gla": [["Gaelic", "Scottish Gaelic"],
                        ["gaélique", "gaélique écossais"],
                        "Gälisch-Schottisch"],
                "gle": ["Irish", "irlandais", "Irisch"],
                "glg": ["Galician", "galicien", "Galicisch"],
                "glv": ["Manx", ["manx", "mannois"], "Manx"],
                "gmh": ["German, Middle High (ca.1050-1500)",
                        "allemand, moyen haut (ca. 1050-1500)",
                        "Mittelhochdeutsch"],
                "goh": ["German, Old High (ca.750-1050)",
                        "allemand, vieux haut (ca. 750-1050)",
                        "Althochdeutsch"],
                "gon": ["Gondi", "gond", "Gondi-Sprache"],
                "gor": ["Gorontalo", "gorontalo", "Gorontalesisch"],
                "got": ["Gothic", "gothique", "Gotisch"],
                "grb": ["Grebo", "grebo", "Grebo-Sprache"],
                "grc": ["Greek, Ancient (to 1453)",
                        "grec ancien (jusqu'à 1453)",
                        "Griechisch"],
                "gre": ["Greek, Modern (1453-)",
                        "grec moderne (après 1453)",
                        "Neugriechisch"],
                "grn": ["Guarani", "guarani", "Guaraní-Sprache"],
                "gsw": [["Swiss German", "Alemannic", "Alsatian"],
                        ["suisse alémanique", "alémanique", "alsacien"],
                        "Schweizerdeutsch"],
                "guj": ["Gujarati", "goudjrati", "Gujarati-Sprache"],
                "gwi": ["Gwich'in", "gwich'in", "Kutchin-Sprache"],
                "hai": ["Haida", "haidan", "Haida-Sprache"],
                "hat": [["Haitian", "Haitian Creole"],
                        ["haïtien", "créole haïtien"],
                        "Haïtien (Haiti-Kreolisch)"],
                "hau": ["Hausa", "haoussa", "Haussa-Sprache"],
                "haw": ["Hawaiian", "hawaïen", "Hawaiisch"],
                "heb": ["Hebrew", "hébreu", "Hebräisch"],
                "her": ["Herero", "herero", "Herero-Sprache"],
                "hil": ["Hiligaynon", "hiligaynon", "Hiligaynon-Sprache"],
                "him": [["Himachali languages", "Western Pahari languages"],
                        ["langues himachalis", "langues paharis occidentale"],
                        "Himachali"],
                "hin": ["Hindi", "hindi", "Hindi"],
                "hit": ["Hittite", "hittite", "Hethitisch"],
                "hmn": [["Hmong", "Mong"], "hmong", "Miao-Sprachen"],
                "hmo": ["Hiri Motu", "hiri motu", "Hiri-Motu"],
                "hrv": ["Croatian", "croate", "Kroatisch"],
                "hsb": ["Upper Sorbian", "haut-sorabe", "Obersorbisch"],
                "hun": ["Hungarian", "hongroise", "Ungarisch"],
                "hup": ["Hupa", "hupa", "Hupa-Sprache"],
                "hye": ["Armenian", "arménien", "Armenisch"],
                "iba": ["Iban", "iban", "Iban-Sprache"],
                "ibo": ["Igbo", "igbo", "Ibo-Sprache"],
                "ice": ["Icelandic", "islandais", "Isländisch"],
                "isl": ["Icelandic", "islandais", "Isländisch"],
                "ido": ["Ido", "ido", "Ido"],
                "iii": [["Sichuan Yi", "Nuosu"],
                        "yi de Sichuan",
                        "Lalo-Sprache"],
                "ijo": ["Ijo languages", "ijo, langues", "Ijo-Sprache"],
                "iku": ["Inuktitut", "inuktitut", "Inuktitut"],
                "ile": [["Interlingue", "Occidental"],
                        "interlingue", "Interlingue"],
                "ilo": ["Iloko", "ilocano", "Ilokano-Sprache"],
                "ina": ["Interlingua International Auxiliary Language Assoc",
                        "interlingua (langue auxiliaire internationale)",
                        "Interlingua"],
                "inc": ["Indic languages",
                        "indo-aryennes, langues",
                        "Indoarische Sprachen (Andere)"],
                "ind": ["Indonesian", "indonésien", "Bahasa Indonesia"],
                "ine": ["Indo-European languages",
                        "indo-européennes, langues",
                        "Indogermanische Sprachen (Andere)"],
                "inh": ["Ingush", "ingouche", "Inguschisch"],
                "ipk": ["Inupiaq", "inupiaq", "Inupik"],
                "ira": ["Iranian languages", "iraniennes, langues",
                        "Iranische Sprachen (Andere)"],
                "iro": ["Iroquoian languages", "iroquoises, langues",
                        "Irokesische Sprachen"],
                "ice": ["Icelandic", "islandais", "Isländisch"],
                "isl": ["Icelandic", "islandais", "Isländisch"],
                "ita": ["Italian", "italien", "Italienisch"],
                "jav": ["Javanese", "javanais", "Javanisch"],
                "jbo": ["Lojban", "lojban", "Lojban"],
                "jpn": ["Japanese", "japonais", "Japanisch"],
                "jpr": ["Judeo-Persian", "judéo-persan", "Jüdisch-Persisch"],
                "jrb": ["Judeo-Arabic", "judéo-arabe", "Jüdisch-Arabisch"],
                "kaa": ["Kara-Kalpak", "karakalpak", "Karakalpakisch"],
                "kab": ["Kabyle", "kabyle", "Kabylisch"],
                "kac": [["Kachin", "Jingpho"],
                        ["kachin", "jingpho"],
                        "Kachin-Sprache"],
                "kal": [["Kalaallisut", "Greenlandic"],
                        "groenlandais",
                        "Grönländisch"],
                "kam": ["Kamba", "kamba", "Kamba-Sprache"],
                "kan": ["Kannada", "kannada", "Kannada"],
                "kar": ["Karen languages", "karen, langues", "Karenisch"],
                "kas": ["Kashmiri", "kashmiri", "Kaschmiri"],
                "kas": ["Georgian", "géorgien", "Georgisch"],
                "kau": ["Kanuri", "kanouri", "Kanuri-Sprache"],
                "kaw": ["Kawi", "kawi", "Kawi"],
                "kaz": ["Kazakh", "kazakh", "Kasachisch"],
                "kbd": ["Kabardian", "kabardien", "Kabardinisch"],
                "kha": ["Khasi", "khasi", "Khasi-Sprache"],
                "khi": ["Khoisan languages",
                        "khoïsan, langues",
                        "Khoisan-Sprachen (Andere)"],
                "khm": ["Central Khmer", "khmer central", "Kambodschanisch"],
                "kho": [["Khotanese", "Sakan"],
                        ["khotanais", "sakan"],
                        "Sakisch"],
                "kik": [["Kikuyu", "Gikuyu"], "kikuyu", "Kikuyu-Sprache"],
                "kin": ["Kinyarwanda", "rwanda", "Rwanda-Sprache"],
                "kir": [["Kirghiz", "Kyrgyz"], "kirghiz", "Kirgisisch"],
                "kmb": ["Kimbundu", "kimbundu", "Kimbundu-Sprache"],
                "kok": ["Konkani", "konkani", "Konkani"],
                "kon": ["Kongo", "kongo", "Kongo-Sprache"],
                "kor": ["Korean", "coréen", "Koreanisch"],
                "kos": ["Kosraean", "kosrae", "Kosraeanisch"],
                "kpe": ["Kpelle", "kpellé", "Kpelle-Sprache"],
                "krc": ["Karachay-Balkar",
                        "karatchai balkar",
                        "Karatschaiisch-Balkarisch"],
                "krl": ["Karelian", "carélien", "Karelisch"],
                "kro": ["Kru languages",
                        "krou, langues",
                        "Kru-Sprachen (Andere)"],
                "kru": ["Kurukh", "kurukh", "Oraon-Sprache"],
                "kua": [["Kuanyama", "Kwanyama"],
                        ["kuanyama", "kwanyama"],
                        "Kwanyama-Sprache"],
                "kum": ["Kumyk", "koumyk", "Kumükisch"],
                "kur": ["Kurdish", "kurde", "Kurdisch"],
                "kut": ["Kutenai", "kutenai", "Kutenai-Sprache"],
                "lad": ["Ladino", "judéo-espagnol", "Judenspanisch"],
                "lah": ["Lahnda", "lahnda", "Lahnda"],
                "lam": ["Lamba", "lamba", "Lamba-Sprache (Bantusprache)"],
                "lao": ["Lao", "lao", "Laotisch"],
                "lat": ["Latin", "latin", "Latein"],
                "lav": ["Latvian", "letton", "Lettisch"],
                "lez": ["Lezghian", "lezghien", "Lesgisch"],
                "lim": [["Limburgan", "Limburger", "Limburgish"],
                        "limbourgeois",
                        "Limburgisch"],
                "lin": ["Lingala", "lingala", "Lingala"],
                "lit": ["Lithuanian", "lituanien", "Litauisch"],
                "lol": ["Mongo", "mongo", "Mongo-Sprache"],
                "loz": ["Lozi", "lozi", "Rotse-Sprache"],
                "ltz": [["Luxembourgish", "Letzeburgesch"],
                        "luxembourgeois",
                        "Luxemburgisch"],
                "lua": ["Luba-Lulua", "luba-lulua", "Lulua-Sprache"],
                "lub": ["Luba-Katanga",
                        "luba-katanga",
                        "Luba-Katanga-Sprache"],
                "lug": ["Ganda", "ganda", "Ganda-Sprache"],
                "lui": ["Luiseno", "luiseno", "Luiseño-Sprache"],
                "lun": ["Lunda", "lunda", "Lunda-Sprache"],
                "luo": ["Luo (Kenya and Tanzania)",
                        "luo (Kenya et Tanzanie)",
                        "Luo-Sprache"],
                "lus": ["Lushai", "lushai", "Lushai-Sprache"],
                "mac": ["Macedonian", "macédonien", "Makedonisch"],
                "mad": ["Madurese", "madourais", "Maduresisch"],
                "mag": ["Magahi", "magahi", "Khotta"],
                "mah": ["Marshallese", "marshall", "Marschallesisch"],
                "mai": ["Maithili", "maithili", "Maithili"],
                "mak": ["Makasar", "makassar", "Makassarisch"],
                "mal": ["Malayalam", "malayalam", "Malayalam"],
                "man": ["Mandingo", "mandingue", "Malinke-Sprache"],
                "mao": ["Maori", "maori", "Maori-Sprache"],
                "map": ["Austronesian languages",
                        ["austronésiennes", "langues"],
                        "Austronesische Sprachen (Andere)"],
                "mar": ["Marathi", "marathe", "Marathi"],
                "mas": ["Masai", "massaï", "Massai-Sprache"],
                "may": ["Malay", "malais", "Malaiisch"],
                "mdf": ["Moksha", "moksa", "Mokscha-Sprache"],
                "mdr": ["Mandar", "mandar", "Mandaresisch"],
                "mic": [["Mi'kmaq", "Micmac"],
                        ["mi'kmaq", "micmac"],
                        "Micmac-Sprache"],
                "min": ["Minangkabau",
                        "minangkabau",
                        "Minangkabau-Sprache"],
                "mis": ["Uncoded languages",
                        "langues non codées",
                        "Einzelne andere Sprachen"],
                "men": ["Mende", "mendé", "Mende-Sprache"],
                "mga": ["Irish, Middle (900-1200)",
                        "irlandais moyen (900-1200)",
                        "Mittelirisch"],
                "mkd": ["Macedonian",
                        "macédonien",
                        "Makedonisch"],
                "mkh": ["Mon-Khmer languages",
                        "môn-khmer, langues",
                        "Mon-Khmer-Sprachen (Andere)"],
                "mlg": ["Malagasy", "malgache", "Malagassi-Sprache"],
                "mlt": ["Maltese", "maltais", "Maltesisch"],
                "mnc": ["Manchu",
                        "mandchou",
                        "Mandschurisch"],
                "mni": ["Manipuri",
                        "manipuri",
                        "Meithei-Sprache"],
                "mno": ["Manobo languages",
                        "manobo, langues",
                        "Manobo-Sprachen"],
                "mri": ["Maori", "maori", "Maori-Sprache"],
                "msa": ["Malay", "malais", "Malaiisch"],
                "moh": ["Mohawk", "mohawk", "Mohawk-Sprache"],
                "mon": ["Mongolian", "mongol", "Mongolisch"],
                "mos": ["Mossi", "moré", "Mossi-Sprache"],
                "mul": ["Multiple languages",
                        "multilingue",
                        "Mehrere Sprachen"],
                "mun": ["Munda languages",
                        "mounda, langues",
                        "Mundasprachen (Andere)"],
                "mus": ["Creek", "muskogee", "Muskogisch"],
                "mwl": ["Mirandese", "mirandais", "Mirandesisch"],
                "mwr": ["Marwari", "marvari", "Marwari"],
                "mya": ["Burmese", "birman", "Birmanisch"],
                "myn": ["Mayan languages", "maya, langues", "Maya-Sprachen"],
                "myv": ["Erzya", "erza", "Erza-Mordwinisch"],
                "nah": ["Nahuatl languages", "nahuatl, langues", "Nahuatl"],
                "nai": ["North American Indian languages",
                        "nord-amérindiennes, langues",
                        "Indianersprachen, Nordamerika (Andere)"],
                "nap": ["Neapolitan", "napolitain", "Neapel / Mundart"],
                "nau": ["Nauru", "nauruan", "Nauruanisch"],
                "nav": [["Navajo", "Navaho"], "navaho", "Navajo-Sprache"],
                "nbl": [["Ndebele, South", "South Ndebele"],
                        "ndébélé du Sud",
                        "Ndebele-Sprache (Transvaal)"],
                "nde": [["Ndebele, North", "North Ndebele"],
                        "ndébélé du Nord",
                        "Ndebele-Sprache (Simbabwe)"],
                "ndo": ["Ndonga", "ndonga", "Ndonga"],
                "nds": [["Low German",
                         "Low Saxon",
                         "German, Low",
                         "Saxon, Low"],
                        ["bas allemand",
                         "bas saxon",
                         "allemand, bas",
                         "saxon, bas"],
                        "Niederdeutsch"],
                "nep": ["Nepali", "népalais", "Nepali"],
                "new": [["Nepal Bhasa", "Newari"],
                        ["nepal bhasa", "newari"],
                        "Newari"],
                "nia": ["Nias", "nias", "Nias-Sprache"],
                "nic": ["Niger-Kordofanian languages",
                        ["nigéro-kordofaniennes", "langues"],
                        "Nigerkordofanische Sprachen (Andere)"],
                "niu": ["Niuean", "niué", "Niue-Sprache"],
                "nld": [["Dutch", "Flemish"],
                        ["néerlandais", "flamand"],
                        "Niederländisch"],
                "nno": [["Norwegian Nynorsk", "Nynorsk, Norwegian"],
                        ["norvégien nynorsk", "nynorsk, norvégien"],
                        "Nynorsk"],
                "nob": [["Bokmål, Norwegian", "Norwegian Bokmål"],
                        "norvégien bokmål",
                        "Bokmål"],
                "nog": ["Nogai",
                        ["nogaï", "nogay"],
                        "Nogaisch"],
                "non": [["Norse, Old"],
                        ["norrois, vieuxx"],
                        "Altnorwegisch"],
                "nor": ["Norwegian", "norvégien", "Norwegisch"],
                "nqo": ["N'Ko", "n'ko", "N'Ko"],
                "nso": [["Pedi", "Sepedi", "Northern Sotho"],
                        ["pedi", "sepedi", "sotho du Nord"],
                        "Pedi-Sprache"],
                "nub": ["Nubian languages",
                        "nubiennes, langues",
                        "Nubische Sprachen"],
                "nwc": [["Classical Newari",
                         "Old Newari",
                         "Classical Nepal Bhasa"],
                        "newari classique",
                        "Alt-Newari"],
                "nya": [["Chichewa", "Chewa", "Nyanja"],
                        ["chichewa", "chewa", "nyanja"],
                        "Nyanja-Sprache"],
                "nym": ["Nyamwezi", "nyamwezi", "Nyamwezi-Sprache"],
                "nyn": ["Nyankole", "nyankolé", "Nkole-Sprache"],
                "nyo": ["Nyoro", "nyoro", "Nyoro-Sprache"],
                "nzi": ["Nzima", "nzema", "Nzima-Sprache"],
                "oci": ["Occitan (post 1500)",
                        "occitan (après 1500)",
                        "Okzitanisch"],
                "oji": ["Ojibwa", "ojibwa", "Ojibwa-Sprache"],
                "ori": ["Oriya", "oriya", "Oriya-Sprache"],
                "orm": ["Oromo", "galla", "Galla-Sprache"],
                "osa": ["Osage", "osage", "Osage-Sprache"],
                "oss": [["Ossetian", "Ossetic"],
                        "ossète", "Ossetisch"],
                "ota": ["Turkish, Ottoman (1500-1928)",
                        "turc ottoman (1500-1928)",
                        "Osmanisch"],
                "oto": ["Otomian languages",
                        "otomi, langues",
                        "Otomangue-Sprachen"],
                "paa": ["Papuan languages",
                        "papoues, langues",
                        "Papuasprachen (Andere)"],
                "pag": ["Pangasinan", "pangasinan", "Pangasinan-Sprache"],
                "pal": ["Pahlavi", "pahlavi", "Mittelpersisch"],
                "pam": [["Pampanga", "Kapampangan"],
                        "pampangan",
                        "Pampanggan-Sprache"],
                "pan": [["Panjabi", "Punjabi"],
                        "pendjabi",
                        "Pandschabi-Sprache"],
                "pap": ["Papiamento", "papiamento", "Papiamento"],
                "pau": ["Palauan", "palau", "Palau-Sprache"],
                "peo": ["Persian, Old (ca.600-400 B.C.)",
                        "perse, vieux (ca. 600-400 av. J.-C.)",
                        "Altpersisch"],
                "per": ["Persian", "persan", "Persisch"],
                "phi": ["Philippine languages",
                        "philippines, langues",
                        "Philippinisch-Austronesisch (Andere)"],
                "phn": ["Phoenician", "phénicien", "Phönikisch"],
                "pli": ["Pali", "pali", "Pali"],
                "pol": ["Polish", "polonais", "Polnisch"],
                "pon": ["Pohnpeian", "pohnpei", "Ponapeanisch"],
                "por": ["Portuguese", "portugais", "Portugiesisch"],
                "pra": ["Prakrit languages",
                        "prâkrit, langues",
                        "Prakrit"],
                "pro": [["Provençal", "Old (to 1500)",
                         "Occitan, Old (to 1500)"],
                        ["provençal ancien (jusqu'à 1500)",
                         "occitan ancien (jusqu'à 1500)"],
                        "Altokzitanisch"],
                "pus": [["Pushto", "Pashto"],
                        "pachto",
                        "Paschtu"],
                "que": ["Quechua", "quechua", "Quechua-Sprache"],
                "raj": ["Rajasthani", "rajasthani", "Rajasthani"],
                "rap": ["Rapanui", "rapanui", "Osterinsel-Sprache"],
                "rar": [["Rarotongan", "Cook Islands Maori"],
                        ["rarotonga", "maori des îles Cook"],
                        "Rarotonganisch"],
                "roa": ["Romance languages", "romanes, langues",
                        "Romanische Sprachen (Andere)"],
                "roh": ["Romansh", "romanche", "Rätoromanisch"],
                "rom": ["Romany", "tsigane", "Romani (Sprache)"],
                "rum": [["Romanian", "Moldavian", "Moldovan"],
                        ["roumain", "moldave"],
                        "Rumänisch"],
                "ron": [["Romanian", "Moldavian", "Moldovan"],
                        ["roumain", "moldave"],
                        "Rumänisch"],
                "run": ["Rundi", "rundi", "Rundi-Sprache"],
                "rup": [["Aromanian", "Arumanian", "Macedo-Romanian"],
                        ["aroumain", "macédo-roumain"],
                        "Aromunisch"],
                "rus": ["Russian", "russe", "Russisch"],
                "sad": ["Sandawe", "sandawe", "Sandawe-Sprache"],
                "sag": ["Sango", "sango", "Sango-Sprache"],
                "sah": ["Yakut", "iakoute", "Jakutisch"],
                "sai": ["South American Indian languages",
                        "sud-amérindiennes, langues",
                        "Indianersprachen, Südamerika (Andere)"],
                "sal": ["Salishan languages",
                        "salishennes, langues",
                        "Salish-Sprache"],
                "sam": ["Samaritan Aramaic", "samaritain", "Samaritanisch"],
                "san": ["Sanskrit", "sanskrit", "Sanskrit"],
                "sas": ["Sasak", "sasak", "Sasak"],
                "sat": ["Santali", "santal", "Santali"],
                "scn": ["Sicilian", "sicilien", "Sizilianisch"],
                "sco": ["Scots", "écossais", "Schottisch"],
                "sel": ["Selkup", "selkoupe", "Selkupisch"],
                "sem": ["Semitic languages",
                        "sémitiques, langues",
                        "Semitische Sprachen (Andere)"],
                "sga": ["Irish, Old (to 900)",
                        "irlandais ancien (jusqu'à 900)",
                        "Altirisch"],
                "sgn": ["Sign Languages",
                        "langues des signes",
                        "Zeichensprachen"],
                "shn": ["Shan", "chan", "Schan-Sprache"],
                "sid": ["Sidamo", "sidamo", "Sidamo-Sprache"],
                "sin": [["Sinhala", "Sinhalese"],
                        "singhalais",
                        "Singhalesisch"],
                "sio": ["Siouan languages",
                        "sioux, langues",
                        "Sioux-Sprachen (Andere)"],
                "sit": ["Sino-Tibetan languages",
                        "sino-tibétaines, langues",
                        "Sinotibetische Sprachen (Andere)"],
                "sla": ["Slavic languages",
                        "slaves, langues",
                        "Slawische Sprachen (Andere)"],
                "slk": ["Slovak", "slovaque", "Slowakisch"],
                "slo": ["Slovak", "slovaque", "Slowakisch"],
                "slv": ["Slovenian", "slovène", "Slowenisch"],
                "sma": ["Southern Sami", "sami du Sud", "Südsaamisch"],
                "sme": ["Northern Sami", "sami du Nord", "Nordsaamisch"],
                "smi": ["Sami languages", "sames, langues", "Saamisch"],
                "smj": ["Lule Sami", "sami de Lule", "Lulesaamisch"],
                "smn": ["Inari Sami", "sami d'Inari", "Inarisaamisch"],
                "smo": ["Samoan", "samoan", "Samoanisch"],
                "sms": ["Skolt Sami", "sami skolt", "Skoltsaamisch"],
                "sna": ["Shona", "shona", "Schona-Sprache"],
                "snd": ["Sindhi", "sindhi", "Sindhi-Sprache"],
                "snk": ["Soninke", "soninké", "Soninke-Sprache"],
                "sog": ["Sogdian", "sogdien", "Sogdisch"],
                "som": ["Somali", "somali", "Somali"],
                "son": ["Songhai languages",
                        "songhai, langues",
                        "Songhai-Sprache"],
                "sot": ["Sotho, Southern",
                        "sotho du Sud",
                        "Süd-Sotho-Sprache"],
                "spa": [["Spanish", "Castilian"],
                        ["espagnol", "castillan"],
                        "Spanisch"],
                "sqi": ["Albanian", "albanais", "Albanisch"],
                "srd": ["Sardinian", "sarde", "Sardisch"],
                "srn": ["Sranan Tongo", "sranan tongo", "Sranantongo"],
                "srp": ["Serbian", "serbe", "Serbisch"],
                "srr": ["Serer", "sérère", "Serer-Sprache"],
                "ssa": ["Nilo-Saharan languages",
                        "nilo-sahariennes, langues",
                        "Nilosaharanische Sprachen (Andere)"],
                "ssw": ["Swati", "swati", "Swasi-Sprache"],
                "suk": ["Sukuma", "sukuma", "Sukuma-Sprache"],
                "sun": ["Sundanese", "soundanais", "Sundanesisch"],
                "sus": ["Susu", "soussou", "Susu"],
                "sux": ["Sumerian", "sumérien", "Sumerisch"],
                "swa": ["Swahili", "swahili", "Swahili"],
                "swe": ["Swedish", "suédois", "Schwedisch"],
                "syc": ["Classical Syriac", "syriaque classique", "Syrisch"],
                "syr": ["Syriac", "syriaque", "Neuostaramäisch"],
                "tah": ["Tahitian", "tahitien", "Tahitisch"],
                "tai": ["Tai languages",
                        "tai, langues",
                        "Thaisprachen (Andere)"],
                "tam": ["Tamil", "tamoul", "Tamil"],
                "tat": ["Tatar", "tatar", "Tatarisch"],
                "tel": ["Telugu", "télougou", "Telugu-Sprache"],
                "tem": ["Timne", "temne", "Temne-Sprache"],
                "ter": ["Tereno", "tereno", "Tereno-Sprache"],
                "tet": ["Tetum", "tetum", "Tetum-Sprache"],
                "tgk": ["Tajik", "tadjik", "Tadschikisch"],
                "tgl": ["Tagalog", "tagalog", "Tagalog"],
                "tha": ["Thai", "thaï", "Thailändisch"],
                "tib": ["Tibetan", "tibétain", "Tibetisch"],
                "tig": ["Tigre", "tigré", "Tigre-Sprache"],
                "tir": ["Tigrinya", "tigrigna", "Tigrinja-Sprache"],
                "tiv": ["Tiv", "tiv", "Tiv-Sprache"],
                "tkl": ["Tokelau", "tokelau", "Tokelauanisch"],
                "tlh": [["Klingon", "tlhIngan-Hol"], "klingon", "Klingonisch"],
                "tli": ["Tlingit", "tlingit", "Tlingit-Sprache"],
                "tmh": ["Tamashek", "tamacheq", "Tamašeq"],
                "tog": ["Tonga (Nyasa)",
                        "tonga (Nyasa)",
                        "Tonga (Bantusprache, Sambia)"],
                "ton": ["Tonga (Tonga Islands)",
                        "tongan (Îles Tonga)",
                        "Tongaisch"],
                "tpi": ["Tok Pisin", "tok pisin", "Neumelanesisch"],
                "tsi": ["Tsimshian", "tsimshian", "Tsimshian-Sprache"],
                "tsn": ["Tswana", "tswana", "Tswana-Sprache"],
                "tso": ["Tsonga", "tsonga", "Tsonga-Sprache"],
                "tuk": ["Turkmen", "turkmène", "Turkmenisch"],
                "tum": ["Tumbuka", "tumbuka", "Tumbuka-Sprache"],
                "tup": ["Tupi languages", "tupi, langues", "Tupi-Sprache"],
                "tur": ["Turkish", "turc", "Türkisch"],
                "tut": ["Altaic languages",
                        "altaïques, langues",
                        "Altaische Sprachen (Andere)"],
                "tvl": ["Tuvalu", "tuvalu", "Elliceanisch"],
                "twi": ["Twi", "twi", "Twi-Sprache"],
                "tyv": ["Tuvinian", "touva", "Tuwinisch"],
                "udm": ["Udmurt", "oudmourte", "Udmurtisch"],
                "uga": ["Ugaritic", "ougaritique", "Ugaritisch"],
                "uig": [["Uighur", "Uyghur"], "ouïgour", "Uigurisch"],
                "ukr": ["Ukrainian", "ukrainien", "Ukrainisch"],
                "umb": ["Umbundu", "umbundu", "Mbundu-Sprache"],
                "und": ["Undetermined",
                        "indéterminée",
                        "Nicht zu entscheiden"],
                "urd": ["Urdu", "ourdou", "Urdu"],
                "uzb": ["Uzbek", "ouszbek", "Usbekisch"],
                "vai": ["Vai", "vaï", "Vai-Sprache"],
                "ven": ["Venda", "venda", "Venda-Sprache"],
                "vie": ["Vietnamese", "vietnamien", "Vietnamesisch"],
                "vol": ["Volapük", "volapük", "Volapük"],
                "vot": ["Votic", "vote", "Wotisch"],
                "wak": ["Wakashan languages",
                        "wakashanes, langues",
                        "Wakash-Sprachen"],
                "wal": [["Wolaitta", "Wolaytta"],
                        ["wolaitta", "wolaytta"],
                        "Walamo-Sprache"],
                "war": ["Waray", "waray", "Waray"],
                "was": ["Washo", "washo", "Washo-Sprache"],
                "wel": ["Welsh", "gallois", "Kymrisch"],
                "wen": ["Sorbian languages",
                        "sorabes, langues",
                        "Sorbisch (Andere)"],
                "wln": ["Walloon", "wallon", "Wallonisch"],
                "wol": ["Wolof", "wolof", "Wolof-Sprache"],
                "xal": [["Kalmyk", "Oirat"],
                        ["kalmouk", "oïrat"],
                        "Kalmückisch"],
                "xho": ["Xhosa", "xhosa", "Xhosa-Sprache"],
                "yao": ["Yao", "yao", "Yao-Sprache (Bantusprache)"],
                "yap": ["Yapese", "yapois", "Yapesisch"],
                "yid": ["Yiddish", "yiddish", "Jiddisch"],
                "yor": ["Yoruba", "yoruba", "Yoruba-Sprache"],
                "ypk": ["Yupik language", "yupik, langues", "Ypik-Sprachen"],
                "zap": ["Zapotec", "zapotèque", "Zapotekisch"],
                "zbl": [["Blissymbols", "Blissymbolics", "Bliss"],
                        ["symboles Bliss", "Bliss"],
                        "Bliss-Symbol"],
                "zen": ["Zenaga", "zenaga", "Zenaga"],
                "zgh": ["Standard Moroccan Tamazight",
                        "amazighe standard marocain", ""],
                "zha": [["Zhuang", "Chuang"], ["zhuang", "chuang"], "Zhuang"],
                "zho": ["Chinese", "chinois", "Chinesisch"],
                "znd": ["Zande languages", "zandé, langues", "Zande-Sprachen"],
                "zul": ["Zulu", "zoulou", "Zulu-Sprache"],
                "zun": ["Zuni", "zuni", "Zuñi-Sprache"],
                "zxx": [["No linguistic content", " Not applicable"],
                        ["pas de contenu linguistique", "non applicable"],
                        "Kein linguistischer Inhalt"],
                "zza": [["Zaza", "Dimili", "Dimli",
                         "Kirdki", "Kirmanjki", "Zazaki"],
                        ["zaza", "dimili", "dimli",
                         "kirdki", "kirmanjki", "zazaki"], "Zazaki"]}
        return dicc

    def dicc_iso639_1(self):
        # giving 2 letters returns a list with the language
        # in english, french and german
        dicc = {"aa": ["Afar", "afar", "Danakil-Sprache"],
                "ab": ["Abkhazian", "abkhaze", "Abchasisch"],
                "af": ["Afrikaans", "afrikaans", "Afrikaans"],
                "ak": ["Akan", "akan",        "Akan-Sprache"],
                "sq": ["Albanian", "albanais", "Albanisch"],
                "am": ["Amharic", "amharique", "Amharisch"],
                "ar": ["Arabic", "arabe", "Arabisch"],
                "an": ["Aragonese", "aragonais", "Aragonesisch"],
                "hy": ["Armenian", "arménien", "Armenisch"],
                "as": ["Assamese", "assamais", "Assamesisch"],
                "av": ["Avaric", "avar", "Awarisch"],
                "ae": ["Avestan", "avestique", "Avestisch"],
                "ay": ["Aymara", "aymara", "Aymará-Sprache"],
                "az": ["Azerbaijani", "azéri", "Aserbeidschanisch"],
                "ba": ["Bashkir", "bachkir", "Baschkirisch"],
                "bm": ["Bambara", "bambara", "Bambara-Sprache"],
                "eu": ["Basque", "basque", "Baskisch"],
                "be": ["Belarusian", "biélorusse", "Weißrussisch"],
                "bn": ["Bengali", "bengali", "Bengali"],
                "bh": ["Bihari languages",
                       "langues biharis",
                       "Bihari (Andere)"],
                "bi": ["Bislama", "bichlamar", "Beach-la-mar"],
                "bo": ["Tibetan", "tibétain", "Tibetisch"],
                "bs": ["Bosnian", "bosniaque", "Bosnisch"],
                "br": ["Breton", "breton", "Bretonisch"],
                "bg": ["Bulgarian", "bulgare", "Bulgarisch"],
                "my": ["Burmese", "birman", "Birmanisch"],
                "ca": [["Catalan", "Valencian"],
                       ["catalan", "valencien"],
                       "Katalanisch"],
                "cs": ["Czech", "tchèque", "Tschechisch"],
                "ch": ["Chamorro", "chamorro", "Chamorro-Sprache"],
                "ce": ["Chechen", "tchétchène", "Tschetschenisch"],
                "zh": ["Chinese", "chinois", "Chinesisch"],
                "cu": [["Church Slavic",
                        "Old Slavonic",
                        "Church Slavonic",
                        "Old Bulgarian",
                        "Old Church Slavonic"],
                       ["slavon d'église",
                        "vieux slave",
                        "slavon liturgique",
                        "vieux bulgare"],
                       "Kirchenslawisch"],
                "cv": ["Chuvash", "tchouvache", "Tschuwaschisch"],
                "kw": ["Cornish", "cornique", "Kornisch"],
                "co": ["Corsican", "corse", "Korsisch"],
                "cr": ["Cree", "cree", "Cree-Sprache"],
                "cy": ["Welsh", "gallois", "Kymrisch"],
                "cs": ["Czech", "tchèque", "Tschechisch"],
                "da": ["Danish", "danois", "Dänisch"],
                "de": ["German", "allemand", "Deutsch"],
                "dv": [["Divehi", "Dhivehi", "Maldivian"],
                       "maldivien",
                       "Maledivisch"],
                "nl": [["Dutch", "Flemish"],
                       ["néerlandais", "flamand"],
                       "Niederländisch"],
                "dz": ["Dzongkha", "dzongkha", "Dzongkha"],
                "el": ["Greek, Modern (1453-)",
                       "grec moderne (après 1453)",
                       "Neugriechisch"],
                "en": ["English", "anglais", "Englisch"],
                "eo": ["Esperanto", "espéranto", "Esperanto"],
                "et": ["Estonian", "estonien", "Estnisch"],
                "eu": ["Basque", "basque", "Baskisch"],
                "ee": ["Ewe", "éwé", "Ewe-Sprache"],
                "fo": ["Faroese", "féroïen", "Färöisch"],
                "fa": ["Persian", "persan", "Persisch"],
                "fj": ["Fijian", "fidjien", "Fidschi-Sprache"],
                "fi": ["Finnish", "finnois", "Finnisch"],
                "fr": ["French", "français", "Französisch"],
                "fr": ["French", "français", "Französisch"],
                "fy": ["Western Frisian", "frison occidental", "Friesisch"],
                "ff": ["Fulah", "peul", "Ful"],
                "ka": ["Georgian", "géorgien", "Georgisch"],
                "de": ["German", "allemand", "Deutsch"],
                "gd": [["Gaelic", "Scottish Gaelic"],
                       ["gaélique", "gaélique écossais"],
                       "Gälisch-Schottisch"],
                "ga": ["Irish", "irlandais", "Irisch"],
                "gl": ["Galician", "galicien", "Galicisch"],
                "gv": ["Manx", ["manx", "mannois"], "Manx"],
                "el": ["Greek, Modern (1453-)",
                       "grec moderne (après 1453)",
                       "Neugriechisch"],
                "gn": ["Guarani", "guarani", "Guaraní-Sprache"],
                "gu": ["Gujarati", "goudjrati", "Gujarati-Sprache"],
                "ht": [["Haitian", "Haitian Creole"],
                       ["haïtien", "créole haïtien"],
                       "Haïtien (Haiti-Kreolisch)"],
                "ha": ["Hausa", "haoussa", "Haussa-Sprache"],
                "he": ["Hebrew", "hébreu", "Hebräisch"],
                "hz": ["Herero", "herero", "Herero-Sprache"],
                "hi": ["Hindi", "hindi", "Hindi"],
                "ho": ["Hiri Motu", "hiri motu", "Hiri-Motu"],
                "hr": ["Croatian", "croate", "Kroatisch"],
                "hu": ["Hungarian", "hongroise", "Ungarisch"],
                "hy": ["Armenian", "arménien", "Armenisch"],
                "ig": ["Igbo", "igbo", "Ibo-Sprache"],
                "is": ["Icelandic", "islandais", "Isländisch"],
                "io": ["Ido", "ido", "Ido"],
                "ii": [["Sichuan Yi", "Nuosu"],
                       "yi de Sichuan",
                       "Lalo-Sprache"],
                "iu": ["Inuktitut", "inuktitut", "Inuktitut"],
                "ie": [["Interlingue", "Occidental"],
                       "interlingue",
                       "Interlingue"],
                "ia": ["Interlingua International Auxiliary Language Assoc",
                       "interlingua (langue auxiliaire internationale)",
                       "Interlingua"],
                "id": ["Indonesian", "indonésien", "Bahasa Indonesia"],
                "ik": ["Inupiaq", "inupiaq", "Inupik"],
                "is": ["Icelandic", "islandais", "Isländisch"],
                "it": ["Italian", "italien", "Italienisch"],
                "jv": ["Javanese", "javanais", "Javanisch"],
                "ja": ["Japanese", "japonais", "Japanisch"],
                "kl": [["Kalaallisut", "Greenlandic"],
                       "groenlandais",
                       "Grönländisch"],
                "kn": ["Kannada", "kannada", "Kannada"],
                "ks": ["Kashmiri", "kashmiri", "Kaschmiri"],
                "ka": ["Georgian", "géorgien", "Georgisch"],
                "kr": ["Kanuri", "kanouri", "Kanuri-Sprache"],
                "kk": ["Kazakh", "kazakh", "Kasachisch"],
                "km": ["Central Khmer", "khmer central", "Kambodschanisch"],
                "ki": [["Kikuyu", "Gikuyu"], "kikuyu", "Kikuyu-Sprache"],
                "rw": ["Kinyarwanda", "rwanda", "Rwanda-Sprache"],
                "ky": [["Kirghiz", "Kyrgyz"], "kirghiz", "Kirgisisch"],
                "kv": ["Komi", "kom", "Komi-Sprache"],
                "kg": ["Kongo", "kongo", "Kongo-Sprache"],
                "ko": ["Korean", "coréen", "Koreanisch"],
                "kj": [["Kuanyama", "Kwanyama"],
                       ["kuanyama", "kwanyama"],
                       "Kwanyama-Sprache"],
                "ku": ["Kurdish", "kurde", "Kurdisch"],
                "lo": ["Lao", "lao", "Laotisch"],
                "la": ["Latin", "latin", "Latein"],
                "lv": ["Latvian", "letton", "Lettisch"],
                "li": [["Limburgan", "Limburger", "Limburgish"],
                       "limbourgeois",
                       "Limburgisch"],
                "ln": ["Lingala", "lingala", "Lingala"],
                "lt": ["Lithuanian", "lituanien", "Litauisch"],
                "lb": [["Luxembourgish", "Letzeburgesch"],
                       "luxembourgeois",
                       "Luxemburgisch"],
                "lu": ["Luba-Katanga",
                       "luba-katanga",
                       "Luba-Katanga-Sprache"],
                "lg": ["Ganda", "ganda", "Ganda-Sprache"],
                "mk": ["Macedonian", "macédonien", "Makedonisch"],
                "mh": ["Marshallese", "marshall", "Marschallesisch"],
                "ml": ["Malayalam", "malayalam", "Malayalam"],
                "mi": ["Maori", "maori", "Maori-Sprache"],
                "mr": ["Marathi", "marathe", "Marathi"],
                "ms": ["Malay", "malais", "Malaiisch"],
                "mk": ["Macedonian", "macédonien", "Makedonisch"],
                "mg": ["Malagasy", "malgache", "Malagassi-Sprache"],
                "mt": ["Maltese", "maltais", "Maltesisch"],
                "mn": ["Mongolian", "mongol", "Mongolisch"],
                "mi": ["Maori", "maori", "Maori-Sprache"],
                "ms": ["Malay", "malais", "Malaiisch"],
                "my": ["Burmese", "birman", "Birmanisch"],
                "na": ["Nauru", "nauruan", "Nauruanisch"],
                "nv": [["Navajo", "Navaho"],
                       "navaho",
                       "Navajo-Sprache"],
                "nr": [["Ndebele, South", "South Ndebele"],
                       "ndébélé du Sud",
                       "Ndebele-Sprache (Transvaal)"],
                "nd": [["Ndebele, North", "North Ndebele"],
                       "ndébélé du Nord",
                       "Ndebele-Sprache (Simbabwe)"],
                "ng": ["Ndonga", "ndonga", "Ndonga"],
                "ne": ["Nepali", "népalais", "Nepali"],
                "nl": [["Dutch", "Flemish"],
                       ["néerlandais", "flamand"],
                       "Niederländisch"],
                "nn": [["Norwegian Nynorsk", "Nynorsk, Norwegian"],
                       ["norvégien nynorsk", "nynorsk, norvégien"],
                       "Nynorsk"],
                "nb": [["Bokmål, Norwegian", "Norwegian Bokmål"],
                       "norvégien bokmål",
                       "Bokmål"],
                "no": ["Norwegian", "norvégien", "Norwegisch"],
                "ny": [["Chichewa", "Chewa", "Nyanja"],
                       ["chichewa", "chewa", "nyanja"], "Nyanja-Sprache"],
                "oc": ["Occitan (post 1500)",
                       "occitan (après 1500)",
                       "Okzitanisch"],
                "oj": ["Ojibwa", "ojibwa", "Ojibwa-Sprache"],
                "or": ["Oriya", "oriya", "Oriya-Sprache"],
                "om": ["Oromo", "galla", "Galla-Sprache"],
                "os": [["Ossetian", "Ossetic"], "ossète", "Ossetisch"],
                "pa": [["Panjabi", "Punjabi"],
                       "pendjabi",
                       "Pandschabi-Sprache"],
                "fa": ["Persian", "persan", "Persisch"],
                "pi": ["Pali", "pali", "Pali"],
                "pl": ["Polish", "polonais", "Polnisch"],
                "pt": ["Portuguese", "portugais", "Portugiesisch"],
                "ps": [["Pushto", "Pashto"], "pachto", "Paschtu"],
                "qu": ["Quechua", "quechua", "Quechua-Sprache"],
                "rm": ["Romansh", "romanche", "Rätoromanisch"],
                "ro": [["Romanian", "Moldavian", "Moldovan"],
                       ["roumain", "moldave"], "Rumänisch"],
                "rn": ["Rundi", "rundi", "Rundi-Sprache"],
                "ru": ["Russian", "russe", "Russisch"],
                "sg": ["Sango", "sango", "Sango-Sprache"],
                "sa": ["Sanskrit", "sanskrit", "Sanskrit"],
                "si": [["Sinhala", "Sinhalese"],
                       "singhalais", "Singhalesisch"],
                "sk": ["Slovak", "slovaque", "Slowakisch"],
                "sl": ["Slovenian", "slovène", "Slowenisch"],
                "se": ["Northern Sami", "sami du Nord", "Nordsaamisch"],
                "sm": ["Samoan", "samoan", "Samoanisch"],
                "sn": ["Shona", "shona", "Schona-Sprache"],
                "sd": ["Sindhi", "sindhi", "Sindhi-Sprache"],
                "so": ["Somali", "somali", "Somali"],
                "st": ["Sotho, Southern", "sotho du Sud", "Süd-Sotho-Sprache"],
                "es": [["Spanish", "Castilian"],
                       ["espagnol", "castillan"], "Spanisch"],
                "sq": ["Albanian", "albanais", "Albanisch"],
                "sc": ["Sardinian", "sarde", "Sardisch"],
                "sr": ["Serbian", "serbe", "Serbisch"],
                "ss": ["Swati", "swati", "Swasi-Sprache"],
                "su": ["Sundanese", "soundanais", "Sundanesisch"],
                "sw": ["Swahili", "swahili", "Swahili"],
                "sv": ["Swedish", "suédois", "Schwedisch"],
                "ty": ["Tahitian", "tahitien", "Tahitisch"],
                "ta": ["Tamil", "tamoul", "Tamil"],
                "tt": ["Tatar", "tatar", "Tatarisch"],
                "te": ["Telugu", "télougou", "Telugu-Sprache"],
                "tg": ["Tajik", "tadjik", "Tadschikisch"],
                "tl": ["Tagalog", "tagalog", "Tagalog"],
                "th": ["Thai", "thaï", "Thailändisch"],
                "bo": ["Tibetan", "tibétain", "Tibetisch"],
                "ti": ["Tigrinya", "tigrigna", "Tigrinja-Sprache"],
                "to": ["Tonga (Tonga Islands)",
                       "tongan (Îles Tonga)",
                       "Tongaisch"],
                "tn": ["Tswana", "tswana", "Tswana-Sprache"],
                "ts": ["Tsonga", "tsonga", "Tsonga-Sprache"],
                "tk": ["Turkmen", "turkmène", "Turkmenisch"],
                "tr": ["Turkish", "turc", "Türkisch"],
                "tw": ["Twi", "twi", "Twi-Sprache"],
                "ug": [["Uighur", "Uyghur"], "ouïgour",
                       "Uigurisch"],
                "uk": ["Ukrainian", "ukrainien", "Ukrainisch"],
                "ur": ["Urdu", "ourdou", "Urdu"],
                "uz": ["Uzbek", "ouszbek", "Usbekisch"],
                "ve": ["Venda", "venda", "Venda-Sprache"],
                "vi": ["Vietnamese", "vietnamien", "Vietnamesisch"],
                "vo": ["Volapük", "volapük", "Volapük"],
                "cy": ["Welsh", "gallois", "Kymrisch"],
                "wa": ["Walloon", "wallon", "Wallonisch"],
                "wo": ["Wolof", "wolof", "Wolof-Sprache"],
                "xh": ["Xhosa", "xhosa", "Xhosa-Sprache"],
                "yi": ["Yiddish", "yiddish", "Jiddisch"],
                "yo": ["Yoruba", "yoruba", "Yoruba-Sprache"],
                "za": [["Zhuang", "Chuang"], ["zhuang", "chuang"], "Zhuang"],
                "zh": ["Chinese", "chinois", "Chinesisch"],
                "zu": ["Zulu", "zoulou", "Zulu-Sprache"]}
        return dicc
