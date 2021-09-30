#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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


echo "These performance metrics requires and csv json downloaded"
time python3 accuracy.py --measure="accuracy" --api="damegender" --csv="files/names/min.csv" --jsondownloaded="files/names/min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="genderize" --csv="files/names/min.csv" --jsondownloaded="files/names/genderizefiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="genderapi" --csv="files/names/min.csv" --jsondownloaded="files/names/genderapifiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="namsor" --csv="files/names/min.csv" --jsondownloaded="files/names/namsorfiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="nameapi" --csv="files/names/min.csv" --jsondownloaded="files/names/nameapifiles_names_min.csv.json"

time python3 confusion.py --api="damegender" --csv="files/names/min.csv" --jsondownloaded="files/names/min.csv.json"

time python3 errors.py --api="damegender" --csv="files/names/partial.csv" --jsondownloaded="files/names/partial.csv.json"
