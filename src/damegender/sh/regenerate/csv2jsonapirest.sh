#!/bin/bash
# Copyright (C) 2023  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is Free Software; you can redistribute it and/or modify
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

echo "Making the json files"
echo "This process can take many hours, please be patient"
echo "If you are bored you can to use ls -l | wc -l to count if the number of files is augmenting"

cd ../..

# RED='\033[0;31m'
# GREEN='\033[0;32m'
# NC='\033[0m' # No Color

echo "To write the path where exists the csv:"
read csvpath

echo "To write the path where exists the output directory to store the json files:"
read outdir

if [ -a $csvpath ]; then
    echo "$csvpath exists"
    if [ -d $outdir ]; then
	echo "$outdir exists"
	python3 csv2jsonapirest.py $csvpath --outdir=$outdir --names_in_countries --gender=all --names_by_multiple_files=1
    else
	echo "$outdir doesn't exist"
    fi
else
    echo "$csvpath doesn't exist"
fi

# echo "cleaning temporary files"
# rm files/tests/*$(date "+%Y")*.txt

