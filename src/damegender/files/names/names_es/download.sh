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
wget -c https://www.ine.es/daco/daco42/nombyapel/nombres_por_edad_media.xls
ssconvert -S nombres_por_edad_media.xls nombres_por_edad_media.csv
wget -c https://www.ine.es/daco/daco42/nombyapel/apellidos_frecuencia.xls
ssconvert -S apellidos_frecuencia.xls apellidos_frecuencia.csv
awk -F'\t' '{print "\""$1"\""}' OFS='","' apellidos_frecuencia.csv.0 > essurnames.csv
sed -i 's/\"//g' essurnames.csv
