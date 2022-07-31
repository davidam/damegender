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
# along with python-examples; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """#added before 2016-10
SELECT DISTINCT ?men ?menLabel
WHERE
{
       ?men wdt:P31 wd:Q5 .
       ?men wdt:P21 wd:Q6581097 .
       ?men wdt:P106/wdt:P279* wd:Q901 . # scientists
       SERVICE wikibase:label {bd:serviceParam wikibase:language "en" }
}
limit 10000"""

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

print("showing some results")

fo = open("male-scientists.csv", "w")
for result in results["results"]["bindings"]:
    print(result)
    fo.write(result['menLabel']['value'] + "," + result['men']['value'] +  "\n");

# Cerramos el archivo fichero.txt
fo.close()

    
# l1 = []
# with open('results.csv') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
#     for row in results:
#         l1.append([row[1], )
#     l1sorted = sorted(l1, key=str.lower)
#     for item in l1sorted:
#         filefem.write(item+"\n")
    
# filefem.close()
    
