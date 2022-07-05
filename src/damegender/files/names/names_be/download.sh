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

cd orig
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_MALE_2021.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_FEMALE_2021.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_FEMALE_2020.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_MALE_2020.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2018_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2018_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2018_F_0.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2018_M_0.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2017_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2017_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2016_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2016_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2015_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2015_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2014_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2014_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2013_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2013_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2012_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2012_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2011_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2011_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2010_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2010_F.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2009_M.zip
wget -c https://statbel.fgov.be/sites/default/files/files/opendata/Voornamen%20bevolking%20per%20gemeente/TA_POP_2009_F.zip

for i in $(ls *zip); do unzip $i; done

for i in $(ls *txt)
do
    sed '1d' $i > out.txt
    mv out.txt $i
done
