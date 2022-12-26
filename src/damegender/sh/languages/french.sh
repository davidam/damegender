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

echo "Building frenchfemales.csv"
echo "Merging french countries, building females"
python3 mergeinterfiles.py --file1="files/names/names_fr/frfemales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/tmp/frcafemales.csv
python3 mergeinterfiles.py --file1="files/tmp/frcafemales.csv" --file2="files/names/names_tg/tgfemales.csv" --output=files/tmp/frcatgfemales.csv
cp files/tmp/frcatgfemales.csv files/names/languages/frenchfemales.csv

echo "Building frenchmales.csv"
echo "Merging french countries, building males"
python3 mergeinterfiles.py --file1="files/names/names_fr/frmales.csv" --file2="files/names/names_ca/camales.csv" --output=files/tmp/frcamales.csv
python3 mergeinterfiles.py --file1="files/tmp/frcamales.csv" --file2="files/names/names_tg/tgmales.csv" --output=files/tmp/frcatgmales.csv
cp files/tmp/frcatgmales.csv files/names/languages/frenchmales.csv


echo "Cleaning temporal files"
rm files/tmp/*
