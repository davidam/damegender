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
# along with Damegender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import requests
import argparse
from app.dame_wikidata import DameWikidata

dw = DameWikidata()
dicc = dw.dicc_countries()

parser = argparse.ArgumentParser()
parser.add_argument('--total', default="us",
                    choices=dicc.keys())
args = parser.parse_args()

url = 'https://query.wikidata.org/sparql'
query2 = """
SELECT ?surname ?surnameLabel ?count
WITH {
  SELECT ?surname (count(?person) AS ?count) WHERE {
    ?person wdt:P734 ?surname .
    ?person wdt:P27 wd:""" + dicc[args.total] + """ .
  }
  GROUP BY ?surname
  ORDER BY DESC(?count)
} AS %results
WHERE {
  INCLUDE %results
  SERVICE wikibase:label
  { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?count)
"""

r = requests.get(url, params={'format': 'json', 'query': query2})
data = r.json()

print("Dumping to surnames.csv")
fo = open("surnames.csv", "w")
for d in data["results"]["bindings"]:
    fo.write(d['surnameLabel']['value'] + "," + d['count']['value'] + "\n")

fo.close()
