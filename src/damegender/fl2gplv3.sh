#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.



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
