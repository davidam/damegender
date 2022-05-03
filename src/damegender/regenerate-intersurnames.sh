#!/bin/sh

# Copyright (C) 2022 David Arroyo Menéndez

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

echo "Building intersurnames.csv"

touch files/names/names_inter/intersurnames.csv

for i in $(ls files/names/names_*/*surnames.csv); do
    if [ $i != "files/names/names_inter/intersurnames.csv" ] || [ $i != "files/names/names_us/surnames.csv" ]
    then
	python3 mergeinterfiles.py --file1="files/names/names_inter/intersurnames.csv" --file2=$i --output="files/names/names_inter/intersurnames.csv"
    fi
done

