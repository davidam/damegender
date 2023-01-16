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

echo "Building englishfemales.csv"
echo "Merging Ireland and United Kingdom"
python3 mergeinterfiles.py --file1="files/names/names_ie/iefemales.csv" --file2="files/names/names_gb/gbfemales.csv" --output=files/tmp/iegbfemales.csv
echo "Merging USA"
python3 mergeinterfiles.py --file1="files/tmp/iegbfemales.csv" --file2="files/names/names_us/usfemales.csv" --output=files/tmp/iegbusfemales.csv
echo "Merging Australia"
python3 mergeinterfiles.py --file1="files/tmp/iegbfemales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/tmp/iegbusaufemales.csv
cp files/tmp/iegbusaufemales.csv files/names/languages/englishfemales.csv

echo "Building englishmales.csv"
echo "Merging Ireland and United Kingdom"
python3 mergeinterfiles.py --file1="files/names/names_ie/iemales.csv" --file2="files/names/names_gb/gbmales.csv" --output=files/tmp/iegbmales.csv
echo "Merging USA"
python3 mergeinterfiles.py --file1="files/tmp/iegbmales.csv" --file2="files/names/names_us/usmales.csv" --output=files/tmp/iegbusmales.csv
cp files/tmp/iegbusmales.csv files/names/languages/englishmales.csv
echo "Merging Australia"
python3 mergeinterfiles.py --file1="files/tmp/iegbmales.csv" --file2="files/names/names_au/aumales.csv" --output=files/tmp/iegbusaumales.csv
cp files/tmp/iegbusaumales.csv files/names/languages/englishmales.csv


echo "Cleaning temporal files"
rm files/tmp/*
