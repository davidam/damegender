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

import unidecode
import unicodedata
import re
import os
import csv


class DameUtils():

    def dicc_dataset(self, sex):
        # given the gender (sex) returns a dictionary where the key is
        # the country and the value is the path with names and sex
        if ((sex == "male") or (sex == "males") or (sex == 1)):
            path = {"ar": "files/names/names_ar/armales.csv",
                    "at": "files/names/names_at/atmales.csv",
                    "au": "files/names/names_au/aumales.csv",
                    "be": "files/names/names_be/bemales.csv",
                    "ca": "files/names/names_ca/camales.csv",
                    "ch": "files/names/names_ch/chmales.csv",
                    "cn": "files/names/names_cn/cnmales.csv",
                    "de": "files/names/names_de/demales.csv",
                    "dk": "files/names/names_dk/males.csv",
                    "es": "files/names/names_es/esmasculinos.csv",
                    "fi": "files/names/names_fi/fimales.csv",
                    "fr": "files/names/names_fr/frmales.csv",
                    "gb": "files/names/names_gb/gbmales.csv",
                    "ie": "files/names/names_ie/iemales.csv",
                    "ine": "files/names/names_es/esmasculinos.csv",
                    "inter": "files/names/names_inter/intermales.csv",
                    "is": "files/names/names_is/ismales.csv",
                    "it": "files/names/names_it/itmales.csv",
                    "mx": "files/names/names_mx/hombres.csv",
                    "no": "files/names/names_no/nomales.csv",
                    "nz": "files/names/names_nz/nzmales.csv",
                    "pt": "files/names/names_pt/ptmales.csv",
                    "ru": "files/names/names_ru/rumales.csv",
                    "ru_ru": "files/names/names_ru/rumales.csv",
                    "ru_en": "files/names/names_ru/rumales.en.csv",
                    "se": "files/names/names_se/semales.csv",
                    "si": "files/names/names_si/simales.csv",
                    # "tr": "files/names/names_tr/trmales.csv",
                    "us": "files/names/names_us/usmales.csv",
                    "usa": "files/names/names_us/usmales.csv",
                    "uy": "files/names/names_uy/uymasculinos.csv"}
        elif ((sex == "female") or (sex == "females") or (sex == 0)):
            path = {"ar": "files/names/names_ar/arfemales.csv",
                    "at": "files/names/names_at/atfemales.csv",
                    "au": "files/names/names_au/aufemales.csv",
                    "be": "files/names/names_be/befemales.csv",
                    "ca": "files/names/names_ca/cafemales.csv",
                    "ch": "files/names/names_ch/chfemales.csv",
                    "cn": "files/names/names_cn/cnfemales.csv",
                    "de": "files/names/names_de/defemales.csv",
                    "dk": "files/names/names_dk/females.csv",
                    "es": "files/names/names_es/esfemeninos.csv",
                    "fi": "files/names/names_fi/fifemales.csv",
                    "fr": "files/names/names_fr/frfemales.csv",
                    "gb": "files/names/names_gb/gbfemales.csv",
                    "ie": "files/names/names_ie/iefemales.csv",
                    "ine": "files/names/names_es/esfemeninos.csv",
                    "inter": "files/names/names_inter/interfemales.csv",
                    "is": "files/names/names_is/isfemales.csv",
                    "it": "files/names/names_it/itfemales.csv",
                    "mx": "files/names/names_mx/mujeres.csv",
                    "no": "files/names/names_no/nofemales.csv",
                    "nz": "files/names/names_nz/nzfemales.csv",
                    "pt": "files/names/names_pt/ptfemales.csv",
                    "ru": "files/names/names_ru/rufemales.csv",
                    "ru_ru": "files/names/names_ru/rufemales.csv",
                    "ru_en": "files/names/names_ru/rufemales.en.csv",
                    "se": "files/names/names_se/sefemales.csv",
                    "si": "files/names/names_si/sifemales.csv",
                    # "tr": "files/names/names_tr/trfemales.csv",
                    "us": "files/names/names_us/usfemales.csv",
                    "usa": "files/names/names_us/usfemales.csv",
                    "uy": "files/names/names_uy/uyfemeninos.csv"}
        elif ((sex == "all") or (sex == 2)):
            path = {"ar": "files/names/names_ar/arall.csv",
                    "at": "files/names/names_at/atall.csv",
                    "au": "files/names/names_au/auall.csv",
                    "be": "files/names/names_be/beall.csv",
                    "ca": "files/names/names_ca/caall.csv",
                    "cn": "files/names/names_cn/cnall.csv",
                    "de": "files/names/names_de/deall.csv",
                    "dk": "files/names/names_dk/dkall.csv",
                    "es": "files/names/names_es/esall.csv",
                    "fi": "files/names/names_fi/fiall.csv",
                    "fr": "files/names/names_fr/frall.csv",
                    "gb": "files/names/names_gb/gball.csv",
                    "ie": "files/names/names_ie/ieall.csv",
                    "ine": "files/names/names_es/esall.csv",
                    "inter": "files/names/names_inter/interall.csv",
                    "is": "files/names/names_is/isall.csv",
                    "it": "files/names/names_it/itall.csv",                    
                    "mx": "files/names/names_mx/mxall.csv",
                    "no": "files/names/names_no/noall.csv",
                    "nz": "files/names/names_nz/nzall.csv",
                    "pt": "files/names/names_pt/ptall.csv",
                    "ru": "files/names/names_ru/ruall.csv",
                    "ru_ru": "files/names/names_ru/ruall.csv",
                    "ru_en": "files/names/names_ru/ruall.en.csv",
                    "se": "files/names/names_si/seall.csv",
                    "si": "files/names/names_si/siall.csv",
                    # "tr": "files/names/names_tr/trall.csv",
                    "us": "files/names/names_us/usall.csv",
                    "usa": "files/names/names_us/usall.csv",
                    "uy": "files/names/names_uy/uyall.csv"}
        return path

    def string2array(self, string):
        # given a string returns an array splitted by white spaces
        res = ""
        string = unidecode.unidecode(string)
        if re.search(r' ', string):
            res = re.sub(r' +', ' ', string)
        array = res.split(' ')
        return array

    def is_not_blank(self, s):
        # given a string returns True if it is not white spaces
        return bool(s and s.strip())

    def various_words_p(self, s):
        # given a string returns True if the are several words
        match = re.search(r"( ?(\w+)( \w)+)|( ?(\w+)(\+\w)+)", s)
        if match:
            return 1
        else:
            return 0

    def represents_int(self, s):
        # returns true if the string s is an integer
        try:
            int(s)
            return True
        except ValueError:
            return False

    def split(self, arr, size):
        # TODO: to replace split name by divide_in_fragments
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs

    def path2file(self, s):
        # given s replaces white spaces or slash symbols in
        # the string by underscore
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if ((c == ' ') | (c == '/')):
                aux = aux + "_"
            else:
                aux = aux + c
        return aux

    def drop_dots(self, s):
        # given s removes dots symbols in the string        
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if (c != '.'):
                aux = aux + c
        return aux

    def drop_quotes(self, s):
        # given s removes quotes symbols in the string        
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if ((c != '"') and (c != "'")):
                aux = aux + c
        return aux

    def drop_external_quotes(self, s):
        # given s removes quotes symbols
        # in element zero and in the last element        
        aux = ""
        c = unicodedata.normalize('NFD', str(s))
        i = 0
        n = len(c)-1
        while (i <= n):
            if (i == 0):
                if ((c[0] != '"') and (c[0] != "'")):
                    aux = aux + c[i]
            elif (i == n): 
                if ((c[n] != '"') and (c[n] != "'")):
                    aux = aux + c[i]
            else:
                aux = aux + c[i]
            i = i + 1
        return aux

    def drop_external_symbols(self, s, l):
        # given s removes symbols contained in l
        # in element zero and in the last element
        aux = ""
        c = unicodedata.normalize('NFD', str(s))
        i = 0
        n = len(c)-1
        while (i <= n):
            if (i == 0):
                if not(c[i] in l):
                    aux = aux + c[i]
            elif (i == n):
                if not(c[i] in l):                
                    aux = aux + c[i]
            else:
                aux = aux + c[i]
            i = i + 1
        return aux
    
    def drop_white_space(self, s):
        # given s removes white space symbols 
        aux = ""
        for c in unicodedata.normalize('NFD', str(s)):
            if (c != ' '):
                aux = aux + c
        return aux

    def single_hyphen_p(self, s):
        # given s returns true if exists only one -
        cnt = 0
        for c in unicodedata.normalize('NFD', str(s)):
            if (c == '-'):
                cnt = cnt + 1
        if (cnt == 1):
            boolean = True
        else:
            boolean = False
        return boolean

    def replace_single_hyphen(self, s):
        # given the string s replace hyphen by a white spaca
        if (self.single_hyphen_p(s)):
            aux = ""
            for c in unicodedata.normalize('NFD', str(s)):
                if (c != '-'):
                    aux = aux + c
                else:
                    aux = aux + " "
        return aux

    def white_space_inside_by(self, s, by):
        # given the string s and the character by replaces white
        # spaces by the s character
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
        # deleting white spaces around a string 
        aux = ""
        arr = unicodedata.normalize('NFD', str(s))
        i = 0
        j = len(arr)
        while (i != j):
            if (arr[i] == " "):
                aux = ""
            else:
                aux = aux + arr[i]
                j = i + 1
            i = i + 1
        j = -1
        while (len(arr) > i) and (i != j):
            if (arr[i] != " "):                
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
        # given a string s delete accents
        return ''.join((c for c in unicodedata.normalize('NFD', s)
                        if unicodedata.category(c) != 'Mn'))

    def drop_pwd(self, s):
        # given a path drop the part of the that is pwd command
        cwd = os.getcwd()
        result = ""
        if re.search(cwd, s):
            result = re.sub(cwd+'/', '', s)
        return result

    def identity2name_email(self, s):
        # given a string identify name and email in the string
        string1 = self.drop_accents(s)
        string2 = self.drop_quotes(string1)
        r1 = r"([\w+ ]*)<([\w\.\+\-]+\@[\w\.\+\-]+\.[a-z]{2,3})>"
        r0 = re.match(r1, string2)
        if r0:
            fullname = r0.group(1)
            email = r0.group(2)
        else:
            fullname = s
            email = ""
        fullname = self.drop_white_space_around(fullname)
        return [fullname, email]

    def same_identity(self, string1, string2):
        # given two strings with fullnames returns True
        # when is the same person or identity
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
        elif ((email1 == email2) and
              ((fullname1 in fullname2) or (fullname2 in fullname1))):
            same_identity = True
        else:
            same_identity = False
        return same_identity

    def list2lower(self, l1):
        # returns a list with lower elements
        l2 = [element.lower() for element in l1]
        return l2

    def num_columns_in_csv(self, csvpath):
        # returns the number of columns in a csv file
        with open(csvpath, 'r') as csvfile:
            first_line = csvfile.readline()
            ncol = first_line.count(',') + 1
        return ncol

    def csvcolumn2list(self, csvpath,  *args, **kwargs):
        # make a list from a column in a csv file
        position = kwargs.get('position', 0)
        header = kwargs.get('header', True)
        delimiter = kwargs.get('delimiter', ',')
        l1 = []
        with open(csvpath) as csvfile:
            rowreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            if header:
                next(rowreader, None)
            for row in rowreader:
                l1.append(row[position])
        return l1

    def csv2list(self, csvpath,  *args, **kwargs):
        # make a list from a csv file
        header = kwargs.get('header', True)
        delimiter = kwargs.get('delimiter', ',')
        noemptyfield = kwargs.get('noemptyfield', False)
        deletewhitespaces = kwargs.get('deletewhitespaces', False)
        deletequotes = kwargs.get('deletequotes', False)
        l1 = []
        with open(csvpath) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            if header:
                next(sexreader, None)
            for row in sexreader:
                if (row != []):
                    if ((noemptyfield is False) or (row[noemptyfield] != "")):
                        i = 0
                        while i < len(row):
                            if deletewhitespaces:
                                row[i] = drop_white_spaces(row[i])
                            if deletequotes:
                                row[i] = drop_quotes(row[i])
                            i = i + 1
                        l1.append(row)
        return l1

    def reduce_csv_columns_to_name_and_freq(self, csvpath, *args, **kwargs):
        name = kwargs.get('name', 0)
        freq = kwargs.get('freq', 1)
        respath = kwargs.get('respath', 'files/tmp/respath.csv')        
        l = self.csv2list(csvpath, header=False)
        fo = open(respath, "w")
        for i in l:
            strname = self.drop_quotes(str(i[name]))
            strname = self.drop_white_space_around(strname)
            strfreq = self.drop_white_space_around(str(i[freq]))
            fo.write(strname + "," + strfreq + "\n")
        fo.close()
        return 1
    
    def lists2csvfile(self, listoflists, csvpath, *args, **kwargs):
        # given a list make a csv file
        samelen = True
        length0 = listoflists[0]
        name_position = kwargs.get('name_position', 0)
        frequency_position = kwargs.get('frequency_position', 1)
        for l1 in listoflists:
            if (length0 == len(l1)):
                samelen = samelen and True
            else:
                samelen = samelen and False
        fo = open(csvpath, "w")
        for l2 in listoflists:
            fo.write(l2[name_position], l2[frequency_position])
        fo.close()
        return 1

    def diccnames2csvfile(self, dicc, csvpath):
        # given a dictionary where the names are keys make a csv file
        # where the first column are names and the second column is
        # the value of the name in the dictionary
        fo = open(csvpath, "w")
        for l1 in dicc.keys():
            fo.write(str(l1) + "," + str(dicc[l1]) + "\n")
        fo.close()
        return 1

    def delete_duplicated(self, l1):
        # given a list l1 returns a new list without duplicated elements
        if (len(l1) == 0):
            return []
        else:
            nodup = []
            for i in l1:
                if (not(i in nodup)):
                    nodup.append(i)
        return nodup

    def delete_duplicated_identities(self, l1):
        # given a list delete duplicated identities
        s = []
        for i in l1:
            if not(i in s):
                identity_dup = False
                for j in s:
                    identity_dup = (identity_dup or self.same_identity(i, j))
                if (not(identity_dup)):
                    s.append(i)
        return s

    def clean_list(self, l1):
        # given a list drop elements with a pattern
        if (len(l1) == 0):
            print([])
        else:
            aux = []
            for i in l1:
                if ((i != "") and (not(re.search(r' ?.*@.*\..*', i)))):
                    aux = aux + [i]
        return aux

    def files_one_level(self, directory):
        # given a folder returns a list with the files
        f = os.popen('find ' + directory)
        l1 = []
        for line in f:
            fields = line.strip().split()
            l1.append(fields[0])
        return l1

    def files_one_level_drop_pwd(self, directory):
        # given a folder returns a list with the path of files
        # without the part given by the pwd command
        f = os.popen('find ' + directory)
        l2 = []
        for line in f:
            fields = line.strip().split()
            if not(os.path.isdir(fields[0])):
                l2.append(self.drop_pwd(fields[0]))
        return l2

    def int2gender(self, int):
        # given an integer returns the gender coded
        # TODO: ISO/IEC 5218 proposes a norm about coding gender:
        #``0 as not know'',``1 as male'', ``2 as female'' and ``9 as not applicable''
        if (int == 0):
            gender = "female"
        elif (int == 1):
            gender = "male"
        else:
            gender = "unknown"
        return gender

    def number_or_zero(self, x):
        # given the variable x returns a number or zero
        # if x is not a number
        try:
            num = int(x)
        except ValueError:
            num = 0
        return num

    def round_and_not_zero_division(self, x, y):
        # given x and y returns the division rounded
        # or zero if x or y is zero
        if ((x == 0) and (y == 0)):
            return 0
        elif (y == 0):
            return 0
        else:
            division = x / y
            return (round(division, 2))

    def initial_letters(self, s):
        # returns true if the string seems initial from a full name
#        s = s.capitalize()
        match = re.search(r'(([A-Z][\.| ]){1,2})|([A-Z]{2})', s)
        if match:
            return True
        else:
            return False

    def initialize_dictionary_names_from_file(self, path, row_name_position):
        # first step processing orig files given a csv file
        # returns a dictionary with the names set in the file
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            l = []
            dicc = {}
            for row1 in reader:
                # this for is only to set the dicc about names
                name = row1[row_name_position]
                name = self.drop_external_symbols(name, ['+', '"', "'"])
                name = name.capitalize()
                name = self.drop_white_space_around(name)
                if (not(name in dicc.keys()) and (name != "")):
                    dicc[name] = {}
        csvfile.close()
        return dicc

    # def initialize_dictionary_names_and_year_from_file(self, path, row_name_position, row_year_position):
    #     dicc = {}
    #     dicc = self.initialize_dictionary_names_from_file(path, row_name_position)
    #     with open(path) as csvfile2:
    #         reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
    #         next(reader2, None)
    #         for row2 in reader2:
    #             # this for is only to set the dicc about years and gender
    #             name = row2[row_name_position]
    #             name = self.drop_external_quotes(name)
    #             name = name.capitalize()
    #             name = self.drop_white_space_around(name)                
    #             if (name != ""):
    #                 dicc[name][row2[row_year_position]] = {}
    #                 dicc[name][row2[row_year_position]]["males"] = 0
    #                 dicc[name][row2[row_year_position]]["females"] = 0
    #     csvfile2.close()
    #     return dicc
