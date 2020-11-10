#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import unidecode
import unicodedata
import re
import os
import csv

class DameUtils():

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
        l = []
        with open(csvpath) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            if (header == True):
                next(sexreader, None)
            for row in sexreader:
                l.append(row[position])
        return l

    def csv2list(self, csvpath,  *args, **kwargs):
        # make a list from a csv file
        header = kwargs.get('header', False)        
        l = []
        with open(csvpath) as csvfile:
            sexreader = csv.reader(csvfile, delimiter=',', quotechar='|')
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

        
