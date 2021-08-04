#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

cp $1 new.txt
FILE=$1
LICENSE=$2

if [ -f "$FILE" ]; then
    echo "File exists"
else
    echo "Insert a file as argument, please"
fi

if [ -f "$LICENSE" ]; then
    echo "FL header file exists"
else
    echo "Insert a FL header file as argument, please"
fi

sed '1,25d' new.txt > tmp.txt
cp $2 nuevo_fichero.txt
cat tmp.txt >> nuevo_fichero.txt
echo "Going to replace gplv3 to feminist license"
cp nuevo_fichero.txt $1

rm tmp*txt nuevo_fichero.txt
