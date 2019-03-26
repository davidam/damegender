#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

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
from app.dame_sexmachine import DameSexmachine
from app.dame_utils import DameUtils
import csv
from pprint import pprint
import re

du = DameUtils()

with open('files/names/all.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    filenou = open('files/names/allnoundefined.csv','w+')

    for row in reader:
        g = du.drop_quotes(row[4])
        if ((g == "m") | (g == "f")):
            filenou.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+'\n')

    filenou.close()

#        print(sorted(l, key=str.lower))
#        print(row[1])
        # if re.search(r"'", row[1]):
        #     result = re.sub(r"'", "", row[1])
        # pprint(result)
