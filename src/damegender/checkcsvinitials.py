#  Copyright (C) 2023 David Arroyo Menéndez

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
#  along with DameGender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,


import re
import csv
import argparse

from app.dame_utils import DameUtils

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
args = parser.parse_args()

du = DameUtils()

filepath=args.path

count = 0
with open(filepath) as csvfile:
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        if (du.initial_letters(row[0])):
            count = count + 1
            print(row[0])

print("Rows with initials: %s" % str(count))
