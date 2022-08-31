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
wget -c https://catalogodatos.gub.uy/dataset/6183293e-6ebc-4d7f-ac38-94a232c2881a/resource/8e125978-c9f6-43cd-8f06-064aab942e3e/download/nombre_nacim_x_anio_sexo.csv
sed '1d' nombre_nacim_x_anio_sexo.csv > out.csv
sed "/NORM\,A/d" out.csv > out2.csv
mv out2.csv nombre_nacim_x_anio_sexo.csv
grep ',"F",' nombre_nacim_x_anio_sexo.csv > origfemales.csv
grep ',"M",' nombre_nacim_x_anio_sexo.csv > origmales.csv
cd ..
