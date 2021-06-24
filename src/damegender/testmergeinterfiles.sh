#!/usr/bin/bash

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color



python3 mergeinterfiles.py --file1="files/names/names_inter/dkfemales10.csv" --file2="files/names/names_inter/defemales10.csv" --output=files/tests/testdkde-$(date "+%Y-%m-%d-%H").csv
# simple test adding elements and making some sum
if ! cmp files/tests/testdkde.csv files/tests/testdkde-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "test is ${RED}failing${NC}"
else
    echo "test is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="files/names/names_inter/befemales10.csv" --file2="files/names/names_inter/dkfemales10.csv" --output=files/tests/testbedk-$(date "+%Y-%m-%d-%H").csv
# test cheking white space and upcase and downcase merging files
if ! cmp files/tests/testbedk.csv files/tests/testbedk-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "testbedk is ${RED}failing${NC}"
else
    echo "testbedk is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="files/names/names_inter/atfemales10.csv" --file2="files/names/names_inter/defemales10.csv" --output=files/tests/testatde-$(date "+%Y-%m-%d-%H").csv
# test checking only upcase and downcase merging files
if ! cmp files/tests/testatde.csv files/tests/testatde-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "testatde is ${RED}failing${NC}"
else
    echo "testatde is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1=files/names/names_inter/esfemeninos10.csv --file2=files/names/names_inter/ptfemales10.csv --output=files/tests/testptes-$(date "+%Y-%m-%d-%H").csv
# checking accents
if ! cmp files/tests/testptes.csv files/tests/testptes-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "testptes is ${RED}failing${NC}"
else
    echo "testptes is ${GREEN}ok${NC}"
fi


rm *-2021-*
