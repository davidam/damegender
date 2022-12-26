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

cd ../..

python3 csv2gender.py files/linux-maintainers.csv --first_name_position=0  --title="Linux maintaners grouped by gender" --dataset="inter"  --outcsv="files/logs/linux.gender.$(date "+%Y-%m-%d").csv"  --outimg="files/images/linux.gender.$(date "+%Y-%m-%d").png" --noshow --delete_duplicated

python3 csv2gender.py files/gnu-maintainers.csv --first_name_position=0 --title="GNU maintainers grouped by gender" --dataset="inter" --outcsv="files/logs/gnu.gender.$(date "+%Y-%m-%d").csv" --outimg="files/images/gnu.gender.$(date "+%Y-%m-%d").png" --noshow --delete_duplicated 

python3 csv2gender.py files/debian-maintainers-gpg-2020-04-01.csv --first_name_position=0 --title="Debian maintainers grouped by gender" --dataset="inter" --outcsv="files/logs/debian.gender.$(date "+%Y-%m-%d").csv" --outimg="files/images/debian.gender.$(date "+%Y-%m-%d").png" --noshow --delete_duplicated

python3 csv2gender.py files/names/names_tests/autores.csv --first_name_position=2 --dataset=inter --noshow --outcsv=files/names/names_tests/autores.firstnamestrict.interguessed.csv --skip_header --guess_with_first_name_strict

python3 csv2gender.py files/names/names_tests/autores.csv --first_name_position=2 --dataset=es --noshow --outcsv=files/names/names_tests/autores.esguessed.csv --skip_header --guess_with_first_name_strict

python3 csv2gender.py files/names/names_tests/autores.csv --first_name_position=2 --dataset=us --noshow --outcsv=files/names/names_tests/autores.usguessed.csv --skip_header --guess_with_first_name_strict

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=inter --noshow --outcsv=files/names/names_tests/liste_des_prenoms.interguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=us --noshow --outcsv=files/names/names_tests/liste_des_prenoms.usguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=fr --noshow --outcsv=files/names/names_tests/liste_des_prenoms.frguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=es --noshow --outcsv=files/names/names_tests/liste_des_prenoms.esguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/liste_des_prenoms.csv --first_name_position=3 --dataset=ca --noshow --outcsv=files/names/names_tests/liste_des_prenoms.caguessed.csv --skip_header --delimiter_csv=';'

python3 csv2gender.py files/names/names_tests/gender_JMLA.dta.csv --first_name_position=1 --dataset=inter --noshow --outcsv=files/names/names_tests/gender_JMLA.interguessed.dta.csv

python3 csv2gender.py files/names/names_tests/gender_JMLA.dta.csv --first_name_position=1 --dataset=us --noshow --outcsv=files/names/names_tests/gender_JMLA.usguessed.dta.csv

python3 csv2gender.py files/names/names_tests/conseil-departmental-haute-garonne.csv --first_name_position=1 --dataset=fr --noshow --outcsv=files/names/names_tests/conseil-departmental-haute-garonne.frguessed.csv --delimiter_csv=";" --skip_header

python3 csv2gender.py files/names/names_tests/conseil-departmental-haute-garonne.csv --first_name_position=1 --dataset=inter --noshow --outcsv=files/names/names_tests/conseil-departmental-haute-garonne.interguessed.csv --delimiter_csv=";" --skip_header

python3 csv2gender.py files/names/names_tests/female-scientists.csv --first_name_position=0 --dataset=inter --noshow --outcsv=files/names/names_tests/female-scientists.interguessed.csv --delimiter=',' --skip_header --guess_with_first_name_strict

python3 csv2gender.py files/names/names_tests/male-scientists.csv --first_name_position=0 --dataset=inter --noshow --outcsv=files/names/names_tests/male-scientists.interguessed.csv --delimiter=',' --skip_header --guess_with_first_name_strict

python3 csv2gender.py files/names/names_tests/female-scientists.csv --first_name_position=0 --dataset=us --noshow --outcsv=files/names/names_tests/female-scientists.usguessed.csv --delimiter=',' --skip_header --guess_with_first_name_strict

python3 csv2gender.py files/names/names_tests/fifa.csv --first_name_position=2 --dataset=inter --outcsv=files/names/names_tests/fifa.interguessed.csv --delimiter=';' --skip_header --guess_with_first_name_strict

