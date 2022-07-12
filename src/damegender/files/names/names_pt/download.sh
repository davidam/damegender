#!/bin/sh

#  Copyright (C) 2022 David Arroyo Menéndez

#  Author: Luz Galvis <newdaycodecontacto@gmail.com>
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
wget -c http://centraldedados.pt/nomes-registados-2014.csv
grep ",M" nomes-registados-2014.csv > hombres-2014.csv
grep ",F" nomes-registados-2014.csv > mujeres-2014.csv
wget -c http://centraldedados.pt/nomes-registados-2015.csv
grep ",M," nomes-registados-2015.csv > hombres-2015.csv
grep ",F," nomes-registados-2015.csv > mujeres-2015.csv
wget -c http://centraldedados.pt/nomes-registados-2016.csv
grep ",M," nomes-registados-2016.csv > hombres-2016.csv
grep ",F," nomes-registados-2016.csv > mujeres-2016.csv

cd ..
