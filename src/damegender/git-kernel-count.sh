#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.



i=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    printf "##### %s ######\n" "$line"
    python3 git2gender.py $line --directory="/tmp/clonedir$i"
	i=`expr $i + 1`
done < files/kernelgits.txt
