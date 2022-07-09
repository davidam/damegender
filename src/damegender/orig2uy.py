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

# This script allows transform the orig files retrieved and processed
# with download.sh in files/names/names_country to damegender csv files,
# such as, countrymales.csv, countryfemales.csv, countrysurnames.csv


import csv
import json
import re
from app.dame_utils import DameUtils

country = "uy"

results = []

du = DameUtils()
outpath = "files/names/names_" + country + "/"
outmales = outpath + country  + "males.csv"
outfemales = outpath + country  + "females.csv"

origpath = outpath + "orig/"
origfile = origpath + "nombre_nacim_x_anio_sexo.csv"

# row_name_position = 2
# row_year_position = 0

posname = 2
posquant = 3
dicc0 = {}
diccmales = du.dump_name_and_quantity_in_dicc(origfile, posname, posquant, dicc=dicc0, delimiter=",")
dicc1 = {}
diccfemales = du.dump_name_and_quantity_in_dicc(origfile, posname, posquant, dicc=dicc1, delimiter=",")

fo = open(outpath + "uymales.csv", "w")
for i in diccmales.keys():
    fo.write(str(i) + "," + str(diccmales[i]) + "\n")
fo.close()

fo = open(outpath + "uyfemales.csv", "w")
for i in diccfemales.keys():
    fo.write(str(i) + "," + str(diccfemales[i]) + "\n")
fo.close()

# d0 = du.find_max_and_min_in_column(origfile, 0)

# dicc = du.init_dicc_names_and_years(origfile, 2, d0["min"], d0["max"])
# dicc2 = du.fill_dicc_names_and_years(origfile, 0, 2)
# print(dicc2)

