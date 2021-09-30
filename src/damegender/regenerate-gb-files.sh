#!/usr/bin/sh

# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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


echo "Building gbfemales.csv"
python3 mergeinterfiles.py --file1="files/names/names_gb/ukfemales.csv" --file2="files/names/names_gb/scotland.females.csv" --output=files/tmp/ukscotlandfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ukscotlandfemales.csv" --file2="files/names/names_gb/northerireland.females.csv" --output=files/tmp/ukscotlandnortherirelandfemales.csv
# python3 mergeinterfiles.py --file1="files/tmp/ukscotlandnortherirelandfemales.csv" --file2="files/names/names_gb/walesfemales.csv" --output=files/tmp/ukscotlandnortherirelandwalesfemales.csv
# cp files/tmp/ukscotlandnortherirelandwalesfemales.csv files/names/names_gb/gbfemales.csv

echo "Building gbmales.csv"
python3 mergeinterfiles.py --file1="files/names/names_gb/ukmales.csv" --file2="files/names/names_gb/scotland.males.csv" --output=files/tmp/ukscotlandmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ukscotlandmales.csv" --file2="files/names/names_gb/northerireland.males.csv" --output=files/tmp/ukscotlandnortherirelandmales.csv
# python3 mergeinterfiles.py --file1="files/tmp/ukscotlandnortherirelandmales.csv" --file2="files/names/names_gb/walesmales.csv" --output=files/tmp/ukscotlandnortherirelandwalesmales.csv
# cp files/tmp/ukscotlandnortherirelandwalesmales.csv files/names/names_gb/gbmales.csv


echo "Cleaning temporal files"
rm files/tmp/uk*

