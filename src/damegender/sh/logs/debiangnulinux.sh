#!/bin/sh

# Copyright (C) 2023 David Arroyo Menéndez

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

cd ../..

python3 csv2gender.py files/linux-maintainers.csv --first_name_position=0  --title="Linux maintaners grouped by gender" --dataset="inter"  --outcsv="files/logs/linux.gender.$(date "+%Y-%m-%d").csv"  --outimg="files/images/linux.gender.$(date "+%Y-%m-%d").png" --noshow --delete_duplicated

python3 csv2gender.py files/gnu-maintainers.csv --first_name_position=0 --title="GNU maintainers grouped by gender" --dataset="inter" --outcsv="files/logs/gnu.gender.$(date "+%Y-%m-%d").csv" --outimg="files/images/gnu.gender.$(date "+%Y-%m-%d").png" --noshow --delete_duplicated 

python3 csv2gender.py files/debian-maintainers-gpg-2020-04-01.csv --first_name_position=0 --title="Debian maintainers grouped by gender" --dataset="inter" --outcsv="files/logs/debian.gender.$(date "+%Y-%m-%d").csv" --outimg="files/images/debian.gender.$(date "+%Y-%m-%d").png" --noshow --delete_duplicated
