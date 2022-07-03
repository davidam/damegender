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
# boys
wget -c https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSA11/CSV/1.0/en -O vsa10.csv
sed '1d' vsa10.csv > out.csv
mv out.csv vsa10.csv
# girls
wget -c https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSA10/CSV/1.0/en -O vsa11.csv
sed '1d' vsa11.csv > out.csv
mv out.csv vsa11.csv
cd ..
