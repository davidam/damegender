#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unicodedata
import re

class DameUtils():
    def split(self, arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs

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

    def drop_accents(self, s):
        return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

    def delete_duplicated(self, l):
        if (len(l) == 0):
            return l
        else:
            rest = []
            for i in l:
                if (i != l[0]):
                    rest = rest + [i]
        return [l[0]] + self.delete_duplicated(rest)

    def clean_list(self, l):
        if (len(l) == 0):
            print([])
        else:
            aux = []
            for i in l:
                if ((i != "") and (not(re.search(r' ?.*@.*\..*', i)))):
                    aux = aux + [i]
        return aux
