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


cd ../..

mkdir -p files/tmp/

ARR=("ar" "at" "au" "be" "ca" "ch" "cl" "de" "dk" "es" "fi" "fr" "gb" "ie" "is" "no" "mx" "pt" "ru" "se" "uy" "us")

for i in "${ARR[@]}"; do
    python3 top.py $i --sex=female --outjson='files/tmp/'$i'fem.json' --number=200
    python3 top.py $i --sex=male --outjson='files/tmp/'$i'mal.json' --number=200
    python3 top.py $i --sex=all --outjson='files/tmp/'$i'all.json' --number=200
done
