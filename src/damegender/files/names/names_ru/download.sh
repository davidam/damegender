#!/bin/bash

#  Copyright (C) 2022 David Arroyo Menéndez

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
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

mkdir -p orig
cd orig

wget -c https://ngodata.ru/dataset/cbf99966-426a-462b-b493-e155209ceb86/resource/30269bb2-d58f-434d-a349-b968cf007b02/download/names_table.zip

unzip names_table.zip

python3 json2list.py

python3 ru2en.py

sed -i "s/'//g" rufemales.en.csv
sed -i "s/'//g" rumales.en.csv 

wget -c https://ngodata.ru/dataset/cbf99966-426a-462b-b493-e155209ceb86/resource/b9124ac0-9265-40db-8258-5b9cfe28aef9/download/surnames_table.zip

unzip surnames_table.zip

wget -c https://ngodata.ru/dataset/cbf99966-426a-462b-b493-e155209ceb86/resource/95b922d4-c033-412c-8bca-b7e0297dcccb/download/midnames_table.zip

unzip midnames_table.zip
