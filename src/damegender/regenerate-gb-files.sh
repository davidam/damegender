#!/usr/bin/sh

# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


echo "Building gbfemales.csv"
python3 mergeinterfiles.py --file1="files/names/names_gb/ukfemales.csv" --file2="files/names/names_gb/scotland.females.csv" --output=files/tmp/ukscotlandfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ukscotlandfemales.csv" --file2="files/names/names_gb/northerireland.females.csv" --output=files/tmp/ukscotlandnortherirelandfemales.csv
# python3 mergeinterfiles.py --file1="files/tmp/ukscotlandnortherirelandfemales.csv" --file2="files/names/names_gb/walesfemales.csv" --output=files/tmp/ukscotlandnortherirelandwalesfemales.csv
# cp files/tmp/ukscotlandnortherirelandwalesfemales.csv files/names/names_gb/gbfemales.csv

echo "Building gbmales.csv"
python3 mergeinterfiles.py --file1="files/names/names_gb/ukmales.csv" --file2="files/names/names_gb/scotland.males.csv" --output=files/tmp/ukscotlandmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ukscotlandmales.csv" --file2="files/names/names_gb/northerireland.males.csv" --output=files/tmp/ukscotlandnortherirelandmales.csv
# python3 mergeinterfiles.py --file1="files/tmp/ukscotlandnortherirelandmales.csv" --file2="files/names/names_gb/walesmales.csv" --output=files/tmp/ukscotlandnortherirelandwalesmales.csv
# cp files/tmp/ukscotlandnortherirelandwalesmales.csv files/names/names_gb/gbmales.csv


echo "Cleaning temporal files"
rm files/tmp/uk*

