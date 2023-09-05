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

echo "Countries where spanish is the majoritary language:"
echo "Chile, Colombia, Costa Rica, Cuba, Dominican Republic, Ecuador, El Salvador, Guatemala, Honduras, Mexico, Nicaragua, Panama, Paraguay, Peru, Puerto Rico, Uruguay, and Venezuela" 

echo "Building spanishfemales.csv"
echo "Merging Argentina (statistics office) and Spanish (statistic office)"
python3 mergeinterfiles.py --file1="files/names/names_ar/arfemales.csv" --file2="files/names/names_es/esfemales.csv" --output=files/tmp/aresfemales.csv
echo "Merging Uruguay (statistics office)"
python3 mergeinterfiles.py --file1="files/tmp/aresfemales.csv" --file2="files/names/names_uy/uyfemales.csv" --output=files/tmp/aresuyfemales.csv
echo "Merging Mexico (statistics office)"
python3 mergeinterfiles.py --file1="files/tmp/aresuyfemales.csv" --file2="files/names/names_mx/mxfemales.csv" --output=files/tmp/aresuymxfemales.csv
echo "Merging Venezuela (wikidata)"
python3 mergeinterfiles.py --file1="files/tmp/aresuymxfemales.csv" --file2="files/names/names_ve/vefemales.csv" --output=files/tmp/aresuymxvefemales.csv
echo "Merging Chile (statistics office)"
python3 mergeinterfiles.py --file1="files/tmp/aresuymxvefemales.csv" --file2="files/names/names_cl/clfemales.csv" --output=files/tmp/aresuymxveclfemales.csv
cp files/tmp/aresuymxveclfemales.csv files/names/languages/spanishfemales.csv


echo "Building spanishmales.csv"
echo "Merging Argentina (statistics office) and Spanish (statistic office)"
python3 mergeinterfiles.py --file1="files/names/names_ar/armales.csv" --file2="files/names/names_es/esmales.csv" --output=files/tmp/aresmales.csv
echo "Merging Uruguay (statistics office)"
python3 mergeinterfiles.py --file1="files/tmp/aresmales.csv" --file2="files/names/names_uy/uymales.csv" --output=files/tmp/aresuymales.csv
echo "Merging Mexico (statistics office)"
python3 mergeinterfiles.py --file1="files/tmp/aresuymales.csv" --file2="files/names/names_mx/mxmales.csv" --output=files/tmp/aresuymxmales.csv
echo "Merging Venezuela (wikidata)"
python3 mergeinterfiles.py --file1="files/tmp/aresuymxmales.csv" --file2="files/names/names_ve/vemales.csv" --output=files/tmp/aresuymxvemales.csv
echo "Merging Chile (statistics office)"
python3 mergeinterfiles.py --file1="files/tmp/aresuymxvefemales.csv" --file2="files/names/names_cl/clmales.csv" --output=files/tmp/aresuymxveclfemales.csv

cp files/tmp/aresuymxveclmales.csv files/names/languages/spanishmales.csv


echo "Cleaning temporal files"
rm files/tmp/*
