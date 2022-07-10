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
echo "Downloading Norway names..."
# One year

wget -c https://www.ssb.no/en/statbank/sq/10069599
sed "1,3d" 10069599 > aux
mv aux 10069599
sed 's/"//g' 10069599 > aux
mv aux 10069599
sed "s/;/,/g" 10069599 > aux
mv aux 10069599
sed "s/\./0/g" 10069599 > aux
mv aux 10069599


wget -c https://www.ssb.no/en/statbank/sq/10070388
sed "1,3d" 10070388 > aux
mv aux 10070388
sed 's/"//g' 10070388 > aux
mv aux 10070388
sed "s/;/,/g" 10070388 > aux
mv aux 10070388
sed "s/\./0/g" 10070388 > aux
mv aux 10070388

# Range of years (2013-2021)
wget -c https://www.ssb.no/en/statbank/sq/10070383
sed "1,3d" 10070383 > aux
mv aux 10070383
wget -c https://www.ssb.no/en/statbank/sq/10070384
sed "1,3d" 10070384 > aux
mv aux 10070384
echo "Downloading Norway surnames..."
wget -c https://www.ssb.no/en/statbank/sq/10070379
sed "1d" 10070379 > aux
mv aux 10070379
wget -c https://www.ssb.no/en/statbank/sq/10070387
sed "1,3d" 10070387 > aux
mv aux 10070387
wget -c https://www.ssb.no/en/statbank/sq/10070381
sed "1,3d" 10070381 > aux
mv aux 10070381

cd ..
