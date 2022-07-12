#!/bin/bash

# Copyright (C) 2021 David Arroyo Menéndez

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


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color



python3 mergeinterfiles.py --file1="files/names/names_inter/dkfemales10.csv" --file2="files/names/names_inter/defemales10.csv" --output=files/tests/testdkde-$(date "+%Y-%m-%d-%H").csv
# simple test adding elements and making some sum
if ! cmp files/tests/testdkde.csv files/tests/testdkde-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo -e "test is ${RED}failing${NC}"
else
    echo -e "test is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="files/names/names_inter/befemales10.csv" --file2="files/names/names_inter/dkfemales10.csv" --output=files/tests/testbedk-$(date "+%Y-%m-%d-%H").csv
# test cheking white space and upcase and downcase merging files
if ! cmp files/tests/testbedk.csv files/tests/testbedk-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo -e "testbedk is ${RED}failing${NC}"
else
    echo -e "testbedk is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="files/names/names_inter/atfemales10.csv" --file2="files/names/names_inter/defemales10.csv" --output=files/tests/testatde-$(date "+%Y-%m-%d-%H").csv
# test checking only upcase and downcase merging files
if ! cmp files/tests/testatde.csv files/tests/testatde-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo -e "testatde is ${RED}failing${NC}"
else
    echo -e "testatde is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1=files/names/names_inter/esfemeninos10.csv --file2=files/names/names_inter/ptfemales10.csv --output=files/tests/testptes-$(date "+%Y-%m-%d-%H").csv
# checking accents
if ! cmp files/tests/testptes.csv files/tests/testptes-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo -e "testptes is ${RED}failing${NC}"
else
    echo -e "testptes is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1=files/names/names_inter/dkmales10.csv --file2=files/names/names_inter/dkfemales10.csv --output=files/tests/dkmalesfemales10-$(date "+%Y-%m-%d-%H").csv --malefemale
# checking malefemale argument
if ! cmp files/tests/dkmalesfemales10.csv files/tests/dkmalesfemales10-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo -e "dkmalesfemales10 is ${RED}failing${NC}"
else
    echo -e "dkmalesfemales10 is ${GREEN}ok${NC}"
fi


python3 mergeinterfiles.py --file1=files/names/names_inter/dkmales5.csv --file2=files/names/names_inter/dkfemales10.csv --output=files/tests/dkmalesfemales5and10-$(date "+%Y-%m-%d-%H").csv --malefemale
# checking few males and many females
if ! cmp files/tests/dkmalesfemales5and10.csv files/tests/dkmalesfemales5and10-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo -e "dkmalesfemales5and10 is ${RED}failing${NC}"
else
    echo -e "dkmalesfemales5and10 is ${GREEN}ok${NC}"
fi



rm files/tests/*-2021-*
