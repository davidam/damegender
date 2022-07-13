#!/bin/sh

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
wget -c https://www.wien.gv.at/gogv/l9ogdvornamentop500

wget -c https://www.statistik.at/fileadmin/pages/426/Vornamen_syn-top.ods

ssconvert -S Vornamen_syn-top.ods Vornamen_syn-top.csv

for i in $(ls Vornamen_syn-top.csv.*); do
    sed "1,4d" $i > aux.csv
    mv aux.csv $i
done

cd ..
