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

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/534d13f2-237c-4448-a6a3-93c07b1bb614/download/baby-names-1944-2013.zip

unzip baby-names-1944-2013.zip

mv "Baby Names 1944-2013" "baby-names"

cd baby-names

for i in $(ls *csv); do
    sed "1d" $i > aux.csv
    mv aux.csv $i
done

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/c11d4aff-fcb5-48a9-aa19-8e04bb8b716e/download/femalecy2014top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/85f2d731-74bd-43fe-8895-f5f65e356c42/download/malecy2014top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/90e682d9-3c82-4265-a5eb-87fa5a034375/download/femalecy2015top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/954188d0-e5a9-469f-9356-ac340bd4eeff/download/malecy2015top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/5e58668a-8150-4c0a-b17e-d55636a318be/download/femalecy2016top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/138f3cf7-edd6-4af2-85c6-2639dbbf04ae/download/malecy2016top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/8a1895d3-d5e1-425d-b89e-f394537763cc/download/cusersjacksm01desktopfemalecy2017top.csv

wget -c https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/920f9134-c32e-48b2-aaae-278dfb0a8ff4/download/cusersjacksm01desktopmalecy2017top.csv

