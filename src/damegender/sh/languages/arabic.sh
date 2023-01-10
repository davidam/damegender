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
python3 mergeinterfiles.py --file1="files/names/names_ae/aefemales.csv" --file2="files/names/names_sa/safemales.csv" --output=files/tmp/aesafemales.csv
python3 mergeinterfiles.py --file1="files/tmp/aesafemales.csv" --file2="files/names/names_sy/syfemales.csv" --output=files/tmp/aesasyfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/aesasyfemales.csv" --file2="files/names/names_ye/yefemales.csv" --output=files/tmp/aesasyyefemales.csv
cp files/tmp/aesasyyefemales.csv files/names/languages/arabicfemales.csv

#echo "Cleaning temporal files"
#rm files/tmp/*
