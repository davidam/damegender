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
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_2020_Koeln.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_2019_Koeln.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_2018_Koeln.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2017.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2016.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2015.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamensstatistik_2014.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2013.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2012.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2011.csv
wget -c https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2010.csv

sed -i '/^,.*/d' Vornamen_Koeln_2013.csv > out.csv
mv out.csv Vornamen_Koeln_2013.csv

cd ..




