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

echo "Building portuguesefemales.csv"
echo "Merging Portuguese and Canada"
python3 mergeinterfiles.py --file1="files/names/names_pt/ptfemales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/tmp/ptcafemales.csv
echo "Adding Angola"
python3 mergeinterfiles.py --file1="files/tmp/ptcafemales.csv" --file2="files/names/names_st/stfemales.csv" --output=files/tmp/ptcaaofemales.csv
echo "Adding Sao Tome and Principe"
python3 mergeinterfiles.py --file1="files/tmp/ptcaaofemales.csv" --file2="files/names/names_st/stfemales.csv" --output=files/tmp/ptcaaoftfemales.csv
cp files/tmp/ptcaaoftfemales.csv files/names/languages/portuguesefemales.csv


echo "Building portuguesemales.csv"
echo "Merging Portuguese and Canada"
python3 mergeinterfiles.py --file1="files/names/names_pt/ptmales.csv" --file2="files/names/names_ca/camales.csv" --output=files/tmp/ptcamales.csv
echo "Adding Angola"
python3 mergeinterfiles.py --file1="files/tmp/ptcamales.csv" --file2="files/names/names_st/stmales.csv" --output=files/tmp/ptcaaomales.csv
echo "Adding Sao Tome and Principe"
python3 mergeinterfiles.py --file1="files/tmp/ptcaaomales.csv" --file2="files/names/names_st/stmales.csv" --output=files/tmp/ptcaaoftmales.csv
cp files/tmp/ptcaaoftmales.csv files/names/languages/portuguesemales.csv


echo "Cleaning temporal files"
rm files/tmp/*
