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

echo "Building spanishfemales.csv"
echo "Merging Argentina and Spanish"
python3 mergeinterfiles.py --file1="files/names/names_ar/arfemales.csv" --file2="files/names/names_es/esfemales.csv" --output=files/tmp/aresfemales.csv
echo "Merging Uruguay"
python3 mergeinterfiles.py --file1="files/tmp/aresfemales.csv" --file2="files/names/names_uy/uyfemales.csv" --output=files/tmp/aresuyfemales.csv
echo "Merging Mexico"
python3 mergeinterfiles.py --file1="files/tmp/aresuyfemales.csv" --file2="files/names/names_mx/mxfemales.csv" --output=files/tmp/aresuymxfemales.csv
cp files/tmp/aresuyfemales.csv files/names/languages/spanishfemales.csv


echo "Building spanishmales.csv"
echo "Merging Argentina and Spanish"
python3 mergeinterfiles.py --file1="files/names/names_ar/armales.csv" --file2="files/names/names_es/esmales.csv" --output=files/tmp/aresmales.csv
echo "Merging Uruguay"
python3 mergeinterfiles.py --file1="files/tmp/aresmales.csv" --file2="files/names/names_uy/uymales.csv" --output=files/tmp/aresuymales.csv
echo "Merging Mexico"
python3 mergeinterfiles.py --file1="files/tmp/aresuymales.csv" --file2="files/names/names_mx/mxmales.csv" --output=files/tmp/aresuymxmales.csv
cp files/tmp/aresuymales.csv files/names/languages/spanishmales.csv


echo "Cleaning temporal files"
rm files/tmp/*
