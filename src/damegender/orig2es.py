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

country = "es"

results = []

du = DameUtils()
outpath = "files/names/names_" + country + "/"
outmales = outpath + country  + "masculinos.csv"
outfemales = outpath + country  + "femeninos.csv"

origpath = outpath + "orig/"
origfile = origpath + "esmasculinos.csv"
origfile2 = origpath + "esfemeninos.csv"

du.reduce_csv_columns_to_name_and_freq(origfile, respath=outmales, name=1, freq=2)
du.reduce_csv_columns_to_name_and_freq(origfile2, respath=outfemales, name=1, freq=2)

