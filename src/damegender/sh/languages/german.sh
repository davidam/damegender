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

echo "Building germanfemales.csv"
echo "Merging German Females Datasets"
python3 mergeinterfiles.py --file1="files/names/names_de/defemales.csv" --file2="files/names/names_at/atfemales.csv" --output=files/tmp/deatfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/deatfemales.csv" --file2="files/names/names_li/lifemales.csv" --output=files/tmp/deatlifemales.csv
cp files/tmp/deatlifemales.csv files/names/languages/germanfemales.csv

echo "Building germanmales.csv"
echo "Merging German Males Datasets"
python3 mergeinterfiles.py --file1="files/names/names_de/demales.csv" --file2="files/names/names_at/atmales.csv" --output=files/tmp/deatmales.csv
python3 mergeinterfiles.py --file1="files/tmp/deatmales.csv" --file2="files/names/names_li/limales.csv" --output=files/tmp/deatlimales.csv
cp files/tmp/deatlimales.csv files/names/languages/germanmales.csv

echo "Building germansurnames.csv"
echo "Merging German Surnames Datasets"
python3 mergeinterfiles.py --file1="files/names/names_de/desurnames.csv" --file2="files/names/names_at/atsurnames.csv" --output=files/tmp/deatsurnames.csv
python3 mergeinterfiles.py --file1="files/tmp/deatsurnames.csv" --file2="files/names/names_li/lisurnames.csv" --output=files/tmp/deatlisurnames.csv
cp files/tmp/deatlisurnames.csv files/names/languages/germansurnames.csv

echo "Cleaning temporal files"
rm files/tmp/*
