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

# nombres permitidos (nombres y género)

wget -c https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-gobierno/nombres/nombres-permitidos.csv

# nombres usados (nombres y género)

wget -c https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-gobierno/nombres/nombres-usados.xlsx
ssconvert -S nombres-usados.xlsx nombres-usados.csv

# nombres, apellidos, género

wget -c https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/8ab77b16-f1a8-4d3f-b664-67becf83a9b9/download/personas.csv 
sed "1d" personas.csv > aux.csv
mv aux.csv personas.csv

# nombres y frecuencias (sin género)

wget -c https://infra.datos.gob.ar/catalog/otros/dataset/2/distribution/2.1/download/historico-nombres.zip

unzip historico-nombres.zip

sed "1d" historico-nombres.csv > aux.csv

mv aux.csv historico-nombres.csv

cd ..
