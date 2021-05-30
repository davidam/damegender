#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import unidecode
import unicodedata
import re
import os
import csv

class DameUtils():

    def locales(self):
        locales = [["at"], ["au"], ["be"], ["ca"], ["cn"], ["de"], ["dk"], ["es", "ine"], ["fi"], ["fr"], ["gb"], ["ie"], ["is"], ["mx"], ["nz"], ["pt"], ["si"], ["us", "usa"], ["uy"]]
        return locales

    def dicc_dataset(self, sex):
        if ((sex == "male") or (sex == "males") or (sex == 1)):
            path_dataset = { "at": "files/names/names_at/atmales.csv",
                             "au": "files/names/names_au/baby-names-1944-2013/aumales.csv",
                             "be": "files/names/names_be/bemales.csv",
                             "ca": "files/names/names_ca/camales.csv",
                             "cn": "files/names/names_cn/cnmales.csv",
                             "de": "files/names/names_de/demales.csv",
                             "dk": "files/names/names_dk/males.csv",
                             "es": "files/names/names_es/esmasculinos.csv",
                             "fi": "files/names/names_fi/fimales.csv",
                             "fr": "files/names/names_fr/frmales.csv",
                             "gb": "files/names/names_gb/ukmales.csv",
                             "ie": "files/names/names_ie/iemales.csv",
                             "ine": "files/names/names_es/esmasculinos.csv",
                             "inter": "files/names/names_inter/intermales.csv",
                             "is": "files/names/names_is/ismales.csv",
                             "mx": "files/names/names_mx/hombres.csv",
                             "nz": "files/names/names_nz/nzmales.csv",
                             "pt": "files/names/names_pt/ptmales.csv",
                             "tr": "files/names/names_tr/male_name_tally",
                             "si": "files/names/names_si/simales.csv",
                             "us": "files/names/names_us/usmales.csv",
                             "usa": "files/names/names_us/usmales.csv",
                             "uy": "files/names/names_uy/uymasculinos.csv"}
        elif ((sex == "female") or (sex == "females") or (sex == 0)):
            path_dataset = { "at": "files/names/names_at/atfemales.csv",
                             "au": "files/names/names_au/baby-names-1944-2013/aufemales.csv",
                             "be": "files/names/names_be/befemales.csv",
                             "ca": "files/names/names_ca/cafemales.csv",
                             "cn": "files/names/names_cn/cnfemales.csv",
                             "de": "files/names/names_de/defemales.csv",
                             "dk": "files/names/names_dk/females.csv",
                             "es": "files/names/names_es/esfemeninos.csv",
                             "fi": "files/names/names_fi/fifemales.csv",
                             "fr": "files/names/names_fr/frfemales.csv",
                             "gb": "files/names/names_gb/ukfemales.csv",
                             "ie": "files/names/names_ie/iefemales.csv",
                             "ine": "files/names/names_es/esfemeninos.csv",
                             "inter": "files/names/names_inter/interfemales.csv",
                             "is": "files/names/names_is/isfemales.csv",
                             "mx": "files/names/names_mx/mujeres.csv",
                             "nz": "files/names/names_nz/nzfemales.csv",
                             "pt": "files/names/names_pt/ptfemales.csv",
                             "tr": "files/names/names_tr/female_name_tally",
                             "si": "files/names/names_si/sifemales.csv",
                             "us": "files/names/names_us/usfemales.csv",
                             "usa": "files/names/names_us/usfemales.csv",
                             "uy": "files/names/names_uy/uyfemeninos.csv"}
        return path_dataset

    def string2array(self, string):
        res = ""
        string = unidecode.unidecode(string)
        if re.search(r' ', string):
            res = re.sub(r' +', ' ', string)
        array = res.split(' ')
        return array

    def is_not_blank(self, s):
        return bool(s and s.strip())

    def various_words_p(self, s):
        match = re.search(r"( ?(\w+)( \w)+)|( ?(\w+)(\+\w)+)", s)
        if match:
            return 1
        else:
            return 0

    def represents_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def split(self, arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs

    def path2file(self, s):
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if ((c == ' ') | (c == '/')):
                aux = aux + "_"
            else:
                aux = aux + c
        return aux

    def drop_dots(self, s):
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if (c != '.'):
                aux = aux + c
        return aux

    def drop_quotes(self, s):
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if ((c != '"') and (c != "'")):
                aux = aux + c
        return aux

    def drop_white_space(self, s):
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if (c != ' '):
                aux = aux + c
        return aux

    def single_hyphen_p(self, s):
        cnt = 0
        for c in unicodedata.normalize('NFD', str(s)):
            if (c == '-'):
                cnt = cnt +1
        if (cnt == 1):
            boolean = True
        else:
            boolean = False
        return boolean

    def replace_single_hyphen(self, s):
        if (self.single_hyphen_p(s)):
            aux = ""
            for c in unicodedata.normalize('NFD', str(s)):
                if (c != '-'):
                    aux = aux + c
                else:
                    aux = aux + " "
        return aux

    def white_space_inside_by(self, s, by):
        inside = 0
        aux = ""
        string = self.drop_white_space_around(s)
        for c in unicodedata.normalize('NFD', str(string)):
            if (c == ' '):
                aux = aux + by
            else:
                aux = aux + c
        return aux

    def drop_white_space_around(self, s):
        aux = ""
        arr = unicodedata.normalize('NFD', str(s))
        i = 0
        j = -1
        while (i != j):
            if (arr[i] == " "):
                aux = ""
            else:
                aux = aux + arr[i]
                j = i + 1
            i = i + 1
        j = -1
        while (len(arr) > i) and (i != j):
            if (arr[i].isalpha()):
                aux = aux + arr[i]
            elif ((arr[i] == " ") and (len(arr) == (i+1))):
                j = i+1
            elif ((arr[i] == " ") and (arr[i+1].isalpha())):
                aux = aux + arr[i]
            else:
                j = i+1
            i = i+1
        return aux

    def drop_accents(self, s):
        return ''.join((c for c in unicodedata.normalize('NFD', s)
                        if unicodedata.category(c) != 'Mn'))

    def drop_pwd(self, s):
        cwd = os.getcwd()
        result = ""
        if re.search(cwd, s):
            result = re.sub(cwd+'/', '', s)
        return result

    def identity2name_email(self, s):
        string1 = self.drop_accents(s)
        string2 = self.drop_quotes(string1)
        r0 = re.match(r"([\w+ ]*)<([\w\.\+\-]+\@[\w\.\+\-]+\.[a-z]{2,3})>", string2)
        if r0:
            fullname = r0.group(1)
            email = r0.group(2)
        else:
            fullname = s
            email = ""
        fullname = self.drop_white_space_around(fullname)
        return [fullname, email]

    def same_identity(self, string1, string2):
        same_identity = False
        string1 = self.drop_accents(string1)
        string2 = self.drop_accents(string2)
        identity1 = self.identity2name_email(string1)
        fullname1 = identity1[0]
        email1 = identity1[1]
        identity2 = self.identity2name_email(string2)
        fullname2 = identity2[0]
        email2 = identity2[1]
        if (string1 == string2):
            same_identity = True
        elif (fullname1 == fullname2):
            same_identity = True
        elif ((email1 == email2) and (fullname1 in fullname2) or (fullname2 in fullname1)):
            same_identity = True
        else:
            same_identity = False
        return same_identity

    def list2lower(self, l):
        ll = [element.lower() for element in l] ; l
        return ll

    def num_columns_in_csv(self, csvpath):
        with open(csvpath, 'r') as csvfile:
            first_line = csvfile.readline()
            ncol = first_line.count(',') + 1
        return ncol

    def csvcolumn2list(self, csvpath,  *args, **kwargs):
        # make a list from a column in a csv file
        position = kwargs.get('position', 0)
        header = kwargs.get('header', True)
        delimiter = kwargs.get('delimiter', ',')
        l = []
        with open(csvpath) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            if (header == True):
                next(sexreader, None)
            for row in sexreader:
                l.append(row[position])
        return l

    def csv2list(self, csvpath,  *args, **kwargs):
        # make a list from a csv file
        header = kwargs.get('header', False)
        delimiter = kwargs.get('delimiter', ',')
        l = []
        with open(csvpath) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            if (header == True):
                next(sexreader, None)
            for row in sexreader:
                l.append(row)
        return l


    # def delete_duplicated(self, l):
    #     if (len(l) == 0):
    #         return l
    #     else:
    #         rest = []
    #         for i in l:
    #             if (i != l[0]):
    #                 rest = rest + [i]
    #     return [l[0]] + self.delete_duplicated(rest)

    def delete_duplicated(self, l):
        if (len(l) == 0):
            return []
        else:
            nodup = []
            for i in l:
                if (not( i in nodup)):
                    nodup.append(i)
        return nodup

    def delete_duplicated_identities(self, l):
        s = []
        for i in l:
            if not(i in s):
                identity_duplicated = False
                for j in s:
                    identity_duplicated = (identity_duplicated or self.same_identity(i, j))
                if (not(identity_duplicated)):
                    s.append(i)
        return s

    def clean_list(self, l):
        if (len(l) == 0):
            print([])
        else:
            aux = []
            for i in l:
                if ((i != "") and (not(re.search(r' ?.*@.*\..*', i)))):
                    aux =  aux + [i]
        return aux

    def files_one_level(self, directory):
        f = os.popen('find ' + directory)
        l = []
        for line in f:
            fields = line.strip().split()
            l.append(fields[0])
        return l

    def files_one_level_drop_pwd(self, directory):
        f = os.popen('find ' + directory)
        l = []
        for line in f:
            fields = line.strip().split()
            if not(os.path.isdir(fields[0])):
                l.append(self.drop_pwd(fields[0]))
        return l

    def yes_or_not(self, question):

        reply = str(input(question+' (y/n): ')).lower().strip()
        ret = None
        if ((reply[0] == 'y') or (reply[0] == 'yes')):
            ret = True
        elif ((reply[0] == 'n') or (reply[0] == 'no') or (reply[0] == 'not')):
            ret = False
        else:
            ret = self.yes_or_not("Uhhhh... please enter ")
        return ret

    def int2gender(self, int):
        if (int == 0):
            gender = "female"
        elif (int == 1):
            gender = "male"
        else:
            gender = "unknown"
        return gender

    def number_or_zero(self, x):
        try:
            num = int(x)
        except ValueError:
            num = 0
        return num


    def round_and_not_zero_division(self, x, y):
        if ((x == 0) and (y == 0)):
            return 0
        elif (y == 0):
            return 0
        else:
            division = x / y
            return (round(division, 3))

    def initial_letters(self, s):
        match = re.search(r'(([A-Z][\.| ]){1,2})|([A-Z]{2})', s)
        if match:
            return True
        else:
            return False
