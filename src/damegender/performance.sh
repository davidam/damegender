#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


echo "These performance metrics requires and csv json downloaded"
time python3 accuracy.py --measure="accuracy" --api="damegender" --csv="files/names/min.csv" --jsondownloaded="files/names/min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="genderize" --csv="files/names/min.csv" --jsondownloaded="files/names/genderizefiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="genderapi" --csv="files/names/min.csv" --jsondownloaded="files/names/genderapifiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="namsor" --csv="files/names/min.csv" --jsondownloaded="files/names/namsorfiles_names_min.csv.json"
time python3 accuracy.py --measure="accuracy" --api="nameapi" --csv="files/names/min.csv" --jsondownloaded="files/names/nameapifiles_names_min.csv.json"

time python3 confusion.py --api="damegender" --csv="files/names/min.csv" --jsondownloaded="files/names/min.csv.json"

time python3 errors.py --api="damegender" --csv="files/names/partial.csv" --jsondownloaded="files/names/partial.csv.json"
