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
wget -c https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/general-statistics/name-statistics/pong/tables-and-graphs/newborn--given-names-alphabetical-overview/boys-names/ -O boys.xlsx
ssconvert -S boys.xlsx boys.csv
wget -c https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/general-statistics/name-statistics/pong/tables-and-graphs/newborn--given-names-alphabetical-overview/girls-names/ -O girls.xlsx
ssconvert -S girls.xlsx girls.csv
cd ..
