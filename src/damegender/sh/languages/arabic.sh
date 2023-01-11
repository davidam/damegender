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

echo "Building arabicfemales.csv"
echo "Merging arabic countries, building females"
python3 mergeinterfiles.py --file1="files/names/names_ae/aefemales.csv" --file2="files/names/names_bh/bhfemales.csv" --output=files/tmp/aebhfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhfemales.csv" --file2="files/names/names_eg/egfemales.csv" --output=files/tmp/aebhegfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhegfemales.csv" --file2="files/names/names_sa/safemales.csv" --output=files/tmp/aebhegsafemales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhegsafemales.csv" --file2="files/names/names_sy/syfemales.csv" --output=files/tmp/aebhegsasyfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhegsasyfemales.csv" --file2="files/names/names_ye/yefemales.csv" --output=files/tmp/aebhegsasyyefemales.csv
cp files/tmp/aebhegsasyyefemales.csv files/names/languages/arabicfemales.csv

echo "Building arabicmales.csv"
echo "Merging arabic countries, building males"
python3 mergeinterfiles.py --file1="files/names/names_ae/aemales.csv" --file2="files/names/names_bh/bhmales.csv" --output=files/tmp/aebhmales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhmales.csv" --file2="files/names/names_eg/egmales.csv" --output=files/tmp/aebhegmales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhegmales.csv" --file2="files/names/names_sa/samales.csv" --output=files/tmp/aebhegsamales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhegsamales.csv" --file2="files/names/names_sy/symales.csv" --output=files/tmp/aebhegsasymales.csv
python3 mergeinterfiles.py --file1="files/tmp/aebhegsasymales.csv" --file2="files/names/names_ye/yemales.csv" --output=files/tmp/aebhegsasyyemales.csv
cp files/tmp/aebhegsasyyemales.csv files/names/languages/arabicmales.csv

#echo "Cleaning temporal files"
#rm files/tmp/*
