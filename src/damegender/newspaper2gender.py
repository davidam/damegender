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

# DESCRIPTION: Given an article url from a newspaper returns the
# number of males and females

import re
import argparse
try:
    from newspaper import Article
except ModuleNotFoundError:
    print("module 'newspaper' is not installed")
    print("try:")
    print("$ pip3 install 'newspaper3k'")
    exit()
#    os.kill(os.getpid(), signal.SIGUSR1)
    # or
#    install("newspaper3k") # the install function from the question


from app.dame_gender import Gender

parser = argparse.ArgumentParser()
parser.add_argument("url", help="display the gender")
parser.add_argument('--total', default="us",
                    choices=['ar', 'at', 'au', 'be', 'ca', 'ch',
                             'cl', 'cn', 'de', 'dk', 'es', 'fi',
                             'fr', 'gb', 'ie', 'is', 'it', 'no', 'nz',
                             'mx', 'pt', 'ru', 'ru_ru',
                             'ru_en', 'se', 'si',
                             'uy', 'us', 'inter'])
# More about iso codes on https://www.iso.org/obp/ui/
parser.add_argument('--gender_standard', default=False,
                    choices=['damegender', 'isoiec5218', 'rfc6350'])
parser.add_argument('--version', action='version', version='0.1')
parser.add_argument('--verbose', default=False, action="store_true")

args = parser.parse_args()

article = Article(args.url)
try:
    article.download()
    article.parse()
    g = Gender()
    for i in article.authors:
        print("--------------------------------")
        print(i)
        l1 = re.split(r'\W+', i)
        print(g.guess(l1[0], dataset=args.total, standard=args.gender_standard))
        print("--------------------------------")
except ValueError:
    print("Please, check the Internet connection")
