#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.





echo "These performance metrics requires and csv json downloaded"
time python3 accuracy.py --measure="accuracy" --api="damegender" --csv="files/names/min.csv" --jsondownloaded="files/names/min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="genderize" --csv="files/names/min.csv" --jsondownloaded="files/names/genderizefiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="genderapi" --csv="files/names/min.csv" --jsondownloaded="files/names/genderapifiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="namsor" --csv="files/names/min.csv" --jsondownloaded="files/names/namsorfiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="nameapi" --csv="files/names/min.csv" --jsondownloaded="files/names/nameapifiles_names_min.csv.json"

time python3 confusion.py --api="damegender" --csv="files/names/min.csv" --jsondownloaded="files/names/min.csv.json"

time python3 errors.py --api="damegender" --csv="files/names/partial.csv" --jsondownloaded="files/names/partial.csv.json"
