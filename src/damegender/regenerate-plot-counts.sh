#!/usr/bin/bash
# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

python3 csv2gender.py files/forbes2020.csv --first_name_position=0 --title="118 forbes people grouped by gender" --dataset="inter" --outcsv="files/forbes2020.gender.csv" --outimg="files/forbes2020.gender.png" --noshow

python3 csv2gender.py files/gnu-maintainers.csv --first_name_position=0 --title="GNU maintainers grouped by gender" --dataset="inter" --outcsv="files/gnu-maintainers.gender.csv" --outimg="files/gnu-maintainers.gender.png" --noshow --delete_duplicated

# python3 csv2gender.py files/linux-maintainers.csv --first_name_position=0 --title="Linux maintaners grouped by gender" --dataset="inter" --outcsv="files/linux-maintainers.gender.csv" --outimg="files/gnu-maintainers.gender.png" --noshow --delete_duplicated

# python3 csv2gender.py files/debian-maintainers-gpg-2020-04-01.csv --first_name_position=0 --title="Debian maintaners grouped by gender" --dataset="inter" --outcsv="files/debian-maintainers.gender.csv" --outimg="files/debian-maintainers.gender.png" --noshow --delete_duplicated
