#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

import re
import argparse
from newspaper import Article
from app.dame_gender import Gender

parser = argparse.ArgumentParser()
parser.add_argument("url", help="display the gender")
parser.add_argument('--total', default="us",
                    choices=['at', 'au', 'be', 'ca', 'ch',
                             'cn', 'de', 'dk', 'es', 'fi',
                             'fr', 'gb', 'ie', 'is', 'no', 'nz',
                             'mx', 'pt', 'se', 'si', 'tr', 'uy',
                             'us', 'namdict', 'inter'])
# More about iso codes on https://www.iso.org/obp/ui/
parser.add_argument('--version', action='version', version='0.1')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()

article = Article(args.url)
article.download()
article.parse()

g = Gender()
for i in article.authors:
    print("--------------------------------")    
    print(i)
    l = re.split(r'\W+', i)
#    print(l)
    print(g.guess(l[0], dataset=args.total))
    print("--------------------------------")
