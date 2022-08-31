#!/bin/bash
# Copyright (C) 2022  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is Free Software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# First, we save the current config and create the config for the tests

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

ARR=("ar" "at" "au" "be" "ca" "ch" "de" "dk" "es" "fi" "fr" "gb" "ie" "is" "no" "mx" "pt" "ru" "se" "uy" "us")

echo "Do you have internet connection and download new files (Y|N):"
read internet

if [[ "${internet}" == "Y" || "${internet}" == "y" ]]; then 
    echo "We are downloading datasets and checkig changes with your local files"
    echo "Please be patient"
    for i in "${ARR[@]}"; do
	pathmales='files/names/names_'${i}'/'${i}'males.csv'
	echo $pathmales
	pathfemales='files/names/names_'${i}'/'${i}'females.csv'
	echo $pathfemales
	pathtest='files/tests/orig2'${i}'-'$(date "+%Y-%m-%d")'.txt'
	echo $pathtest
	python3 orig2.py $i --download 
	git diff $pathmales > $pathtest
	git diff $pathfemales >> $pathtest
	if [ -s $pathtest ]
	then
	    echo -e "${i} dataset is not ${RED}updated${NC}"
	else
	    echo -e "${i} dataset is ${GREEN}updated${NC}"
	fi
    done
else
    echo "We are checkig changes with your local files"    
    for i in "${ARR[@]}"; do
	pathmales='files/names/names_'${i}'/'${i}'males.csv'
	echo $pathmales
	pathfemales='files/names/names_'${i}'/'${i}'females.csv'
	echo $pathfemales
	pathtest='files/tests/orig2'${i}'-'$(date "+%Y-%m-%d")'.txt'
	echo $pathtest	
	python3 orig2.py $i &> /dev/null
	git diff $pathmales > $pathtest
	git diff $pathfemales >> $pathtest
	if [ -s $pathtest ]
	then
	    echo -e "${i} dataset is not ${RED}updated${NC}"
	else
	    echo -e "${i} dataset is ${GREEN}updated${NC}"
	fi
    done
fi



# echo "cleaning temporary files"
# rm files/tests/*$(date "+%Y")*.txt

