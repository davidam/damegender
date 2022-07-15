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

python3 orig2.py at &> /dev/null
git diff files/names/names_at/atmales.csv > files/tests/orig2at-$(date "+%Y-%m-%d").txt
git diff files/names/names_at/atfemales.csv >> files/tests/orig2at-$(date "+%Y-%m-%d").txt

if [ -s files/tests/orig2at-$(date "+%Y-%m-%d").txt ]
then
	echo -e  "austrian dataset is ${GREEN}updated${NC}"    
fi

echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt


