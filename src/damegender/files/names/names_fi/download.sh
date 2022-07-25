#!/bin/bash

#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidam@gmail.com>
#  Maintainer: David Arroyo Menendez <davidam@gmail.com>
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
wget -c https://www.avoindata.fi/data/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/957d19a5-b87a-4c4d-8595-49c22d9d3c58/download/sukunimitilasto-2022-02-07-dvv.xlsx -O sukunimitilasto.xlsx
ssconvert -S sukunimitilasto.xlsx sukunimitilasto.csv
wget -c https://www.avoindata.fi/data/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/08c89936-a230-42e9-a9fc-288632e234f5/download/etunimitilasto-2022-02-07-dvv.xlsx -O etunimitilasto.xlsx
ssconvert -S etunimitilasto.xlsx etunimitilasto.csv
for i in $(ls *csv*); do
    sed "1d" $i > aux.csv
    mv aux.csv $i
done
rm aux.csv
cp sukunimitilasto.csv.0 ../fisurnames.csv
cd ..
