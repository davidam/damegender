#!/bin/sh
#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <darroyome@MacBook-Pro-de-David.local> 
#  Maintainer: David Arroyo Menendez <darroyome@MacBook-Pro-de-David.local> 
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

wget -c http://datamx.io/dataset/2f4f2e93-fb20-423b-bf44-e68256bcc635/resource/df9d4714-a5a3-469f-ae9a-d4c28b34d954/download/hombres.csv
sed '1d' hombres.csv > aux.csv
mv aux.csv hombres.csv

wget -c http://datamx.io/dataset/2f4f2e93-fb20-423b-bf44-e68256bcc635/resource/8047ffa2-dac3-4675-87e1-e7eb4de09825/download/mujeres.csv
sed '1d' mujeres.csv > aux.csv
mv aux.csv mujeres.csv

wget -c http://datamx.io/dataset/2f4f2e93-fb20-423b-bf44-e68256bcc635/resource/56f84bf5-8255-4b15-949d-912fc79477ce/download/apellidos.csv
sed '1d' apellidos.csv > aux.csv
mv aux.csv apellidos.csv

cd ..
