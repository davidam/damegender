#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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
#  along with damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,


import requests
from lxml import html
from pprint import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="display the gender")
parser.add_argument('--total', default="us", choices=['en', 'es'])
parser.add_argument('--version', action='version', version='0.3')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()



#r = requests.get('http://localhost/maria.html')
if (args.total == "es"):
    r = requests.get('https://es.wikipedia.org/wiki/'+ args.name +'_(nombre)')
elif (args.total == "en"):
    r = requests.get('https://en.wikipedia.org/wiki/'+ args.name +'_(given_name)')
#print(r.url)
#print(r.text)


tree = html.fromstring(r.content)

if (args.total == "es"):
    gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
    arraygender = tree.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
    footer = tree.xpath('//div[@class="action-list"]//p/text()')
elif (args.total == "en"):
    arraygender = tree.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
    footer = tree.xpath('//div[@class="action-list"]//p/text()')

#print(gender)
#print(arraygender[3])

if (args.total == "es"):
    for i in arraygender:
        if (i.strip() == "Masculino"):
            print("Masculino")
        elif (i.strip() == "Femenino"):
            print("Femenino")
elif (args.total == "en"):
    for i in arraygender:
        if (i.strip() == "Male"):
            print("Male")
        elif (i.strip() == "Female"):
            print("Female")
