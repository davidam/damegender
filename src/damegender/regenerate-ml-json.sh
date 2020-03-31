#!/bin/bash

# Copyright (C) 2020  David Arroyo Menéndez

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

python3 damegender2json.py --ml=sgd --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.sgd.json
python3 damegender2json.py --ml=svc --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.svc.json
python3 damegender2json.py --ml=nltk --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.nltk.json
python3 damegender2json.py --ml=gaussianNB --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.gaussianNB.json
python3 damegender2json.py --ml=multinomialNB --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.multinomialNB.json
python3 damegender2json.py --ml=bernoulliNB --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.bernoulliNB.json
python3 damegender2json.py --ml=tree --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.tree.json
python3 damegender2json.py --ml=mlp --csv=files/names/allnoundefined.csv --jsonoutput=files/names/allnoundefined.csv.mlp.json
