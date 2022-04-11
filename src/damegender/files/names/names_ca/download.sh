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
wget -c https://open.alberta.ca/dataset/11245675-b047-49fc-8bd1-cc2ce8314a6d/resource/e8aac308-c754-484c-b446-0c57ed0e8d37/download/baby-names-frequency.xlsx -O baby-names-frequency.xlsx
ssconvert -S baby-names-frequency.xlsx baby-names-frequency.csv
sed -n '5,$p' baby-names-frequency.csv.0 > baby-names-frequency.csv 
