#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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
#  along with damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,




cp $1 new.txt
FILE=$1
LICENSE=$2
if [ -f "$FILE" ]; then
    echo "File exists"
else
    echo "Insert a file as argument, please"
fi

if [ -f "$LICENSE" ]; then
    echo "GPL header file exists"
else
    echo "Insert a GPL header file as argument, please"
fi



sed '1,5d' new.txt > tmp.txt
cp $2 nuevo_fichero.txt
cat tmp.txt >> nuevo_fichero.txt
echo "Going to replace feminist license to gplv3"
cp nuevo_fichero.txt $1

rm tmp*txt nuevo_fichero.txt
