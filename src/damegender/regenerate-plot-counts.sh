#!/usr/bin/bash
# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.



echo "Warning: you could need more than 24h for the next scripts"
echo "You will receive messages about the state of the work"
echo "Regenerating plot counting males, females and unknows about forbes people"
python3 csv2gender.py files/forbes2020.csv --first_name_position=0 --title="118 forbes people grouped by gender" --dataset="inter" --outcsv="files/forbes2020.gender.csv" --outimg="files/forbes2020.gender.png" --noshow

echo "Regenerating plot counting males, females and unknows about gnu maintainers"
python3 csv2gender.py files/gnu-maintainers.csv --first_name_position=0 --title="GNU maintainers grouped by gender" --dataset="inter" --outcsv="files/gnu-maintainers.gender.csv" --outimg="files/gnu-maintainers.gender.png" --noshow --delete_duplicated

echo "Regenerating plot counting males, females and unknows about linux maintainers"
python3 csv2gender.py files/linux-maintainers.csv --first_name_position=0 --title="Linux maintaners grouped by gender" --dataset="inter" --outcsv="files/linux-maintainers.gender.csv" --outimg="files/linux-maintainers.gender.png" --noshow --delete_duplicated

echo "Regenerating plot counting males, females and unknows about debian maintainers"
python3 csv2gender.py files/debian-maintainers-gpg-2020-04-01.csv --first_name_position=0 --title="Debian maintaners grouped by gender" --dataset="inter" --outcsv="files/debian-maintainers.gender.csv" --outimg="files/debian-maintainers.gender.png" --noshow --delete_duplicated

echo "Regenerating plot counting males, females and unknows about academic people"
echo "Warning: you could need more than 24h for the next script"
python3 csv2gender.py files/scientifics.csv --first_name_position=0 --title="Academic people collected by webometrics and grouped by gender" --dataset="inter" --outcsv=files/scientifics.gender.csv --outimg=files/scientifics.gender.png --noshow
