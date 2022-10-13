#!/bin/sh

# Copyright (C) 2022 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

python3 csv2gender.py files/names/names_tests/autores.csv --first_name_position=2 --dataset=inter --noshow --outcsv=files/names/names_tests/autores.interguessed.csv --skip_header

python3 csv2gender.py files/names/names_tests/autores.csv --first_name_position=2 --dataset=es --noshow --outcsv=files/names/names_tests/autores.esguessed.csv --skip_header

python3 csv2gender.py files/names/names_tests/autores.csv --first_name_position=2 --dataset=us --noshow --outcsv=files/names/names_tests/autores.usguessed.csv --skip_header

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=inter --noshow --outcsv=files/names/names_tests/liste_des_prenoms.interguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=us --noshow --outcsv=files/names/names_tests/liste_des_prenoms.usguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=fr --noshow --outcsv=files/names/names_tests/liste_des_prenoms.frguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=es --noshow --outcsv=files/names/names_tests/liste_des_prenoms.esguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=ca --noshow --outcsv=files/names/names_tests/liste_des_prenoms.caguessed.csv --skip_header --delimiter_csv=';'
