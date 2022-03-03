#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2022  David Arroyo Menéndez

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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import requests
import argparse
from app.dame_wikidata import DameWikidata

parser = argparse.ArgumentParser()
parser.add_argument('gender', default="female",
                    choices=['female', 'male'])
parser.add_argument('--total', default="inter",
                    choices=['af', 'al', 'dz', 'as', 'ad',
                             'at', 'au', 'be', 'ca', 'ch',
                             'cn', 'de', 'dk', 'es', 'fi',
                             'fr', 'gb', 'ie', 'is', 'no', 'nz',
                             'mx', 'pt', 'ru', 'se', 'si',
                             'uy', 'us'])
args = parser.parse_args()

url = 'https://query.wikidata.org/sparql'

male = False
female = False
if (args.gender == "female"):
    female = True
elif (args.gender == "male"):
    male = True

if female:
    gender = "    ?person wdt:P21 wd:Q6581072 . "
elif male:
    gender = "    ?person wdt:P21 wd:Q6581097 . "

dw = DameWikidata()
dicc = dw.dicc_countries()
    
query2 = """
SELECT ?name ?nameLabel ?count
WITH {
  SELECT ?name (count(?person) AS ?count) WHERE {
    ?person wdt:P735 ?name . 
""" + gender + """
    ?person wdt:P27 wd:""" + dicc[args.total] + """ .
  }
  GROUP BY ?name
  ORDER BY DESC(?count)
  LIMIT 100
} AS %results
WHERE {
  INCLUDE %results
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?count)
"""
r = requests.get(url, params = {'format': 'json', 'query': query2})
data = r.json()

# print(data["results"]["bindings"])

print("Dumping to names.csv")
fo = open("names.csv", "w")
for d in data["results"]["bindings"]:
    # print(d)
    # print(d["count"]["value"])
    # print(d["nameLabel"]["value"])
    fo.write(d['nameLabel']['value'] + "," + d['count']['value'] +  "\n")





# Cerramos el archivo fichero.txt
fo.close()
