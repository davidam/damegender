#!/bin/sh

# Copyright (C) 2021 David Arroyo Menéndez

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

cd ../../
mkdir -p files/tmp

# https://en.wikipedia.org/wiki/Portuguese_language
echo "Countries where portuguese is the majoritary language: Portugal, Sao Tome, Angola and Brazil"

echo "Building portuguesefemales.csv"
echo "Merging Portuguese (official statistics) and Angola (Wikipedia)"
python3 mergeinterfiles.py --file1="files/names/names_pt/ptfemales.csv" --file2="files/names/names_ao/aofemales.csv" --output=files/tmp/ptaofemales.csv
echo "Adding Sao Tome e Principe (Wikipedia)"
python3 mergeinterfiles.py --file1="files/tmp/ptaofemales.csv" --file2="files/names/names_st/stfemales.csv" --output=files/tmp/ptaostfemales.csv
echo "Adding Brazil (Official Statistics + Wikipedia)"
python3 mergeinterfiles.py --file1="files/tmp/ptaostfemales.csv" --file2="files/names/names_br/brfemales.csv" --output=files/tmp/ptaostbrfemales.csv
cp files/tmp/ptaostbrfemales.csv files/names/languages/portuguesefemales.csv

echo "Building portuguesemales.csv"
echo "Merging Portuguese (Official Statistics) and Angola (Wikipedia)"
python3 mergeinterfiles.py --file1="files/names/names_pt/ptmales.csv" --file2="files/names/names_ao/aomales.csv" --output=files/tmp/ptaomales.csv
echo "Adding Sao Tome e Principe (Wikipedia)"
python3 mergeinterfiles.py --file1="files/tmp/ptaomales.csv" --file2="files/names/names_st/stmales.csv" --output=files/tmp/ptaostmales.csv
echo "Adding Brazil (Official Statistics + Wikipedia)"
python3 mergeinterfiles.py --file1="files/tmp/ptaostmales.csv" --file2="files/names/names_br/brmales.csv" --output=files/tmp/ptaostbrmales.csv
cp files/tmp/ptaostbrmales.csv files/names/languages/portuguesemales.csv


echo "Cleaning temporal files"
rm files/tmp/*
