#!/bin/sh

# Copyright (C) 2022 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
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

python3 mergeinterfiles.py --file1="files/names/languages/arabicmales.csv" --file2="files/names/languages/arabicfemales.csv" --output=files/names/languages/arabicall.csv --malefemale

python3 mergeinterfiles.py --file1="files/names/languages/englishmales.csv" --file2="files/names/languages/englishfemales.csv" --output=files/names/languages/englishall.csv --malefemale

python3 mergeinterfiles.py --file1="files/names/languages/finnishmales.csv" --file2="files/names/languages/finnishfemales.csv" --output=files/names/languages/finnishall.csv --malefemale

python3 mergeinterfiles.py --file1="files/names/languages/frenchmales.csv" --file2="files/names/languages/frenchfemales.csv" --output=files/names/languages/frenchall.csv --malefemale

python3 mergeinterfiles.py --file1="files/names/languages/germanmales.csv" --file2="files/names/languages/germanfemales.csv" --output=files/names/languages/germanall.csv --malefemale

python3 mergeinterfiles.py --file1="files/names/languages/portuguesemales.csv" --file2="files/names/languages/portuguesefemales.csv" --output=files/names/languages/portugueseall.csv --malefemale

