#!/usr/bin/sh
#  Copyright (C) 2020 David Arroyo Menendez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  You can share, copy and modify this software if you are a woman or you
#  are David Arroyo Menéndez and you include this note.


cp $1 new.txt
FILE=$1
if [ -f "$FILE" ]; then
    echo "File exists"
fi    

sed '1,5d' new.txt > tmp.txt
sed '/Author:/d' tmp.txt > tmp2.txt
sed '/Maintainer:/d' tmp2.txt > tmp3.txt
sed '/You can share, copy and modify this software if you are a woman or you/d' tmp3.txt > tmp4.txt
sed '/and you include this note/d' tmp4.txt > tmp5.txt
cp files/gpl.txt nuevo_fichero.txt
cat tmp5.txt >> nuevo_fichero.txt
echo "Going to replace feminist license to gplv3"
cp nuevo_fichero.txt $1

rm tmp*txt nuevo_fichero.txt 
