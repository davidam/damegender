#!/usr/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color



python3 mergeinterfiles.py --file1="dkfemales10.csv" --file2="defemales10.csv" --output=testdkde-$(date "+%Y-%m-%d-%H").csv
# simple test adding elements and making some sum
if ! cmp testdkde.csv testdkde-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "test is ${RED}failing${NC}"
else
    echo "test is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="befemales10.csv" --file2="dkfemales10.csv" --output=testbedk-$(date "+%Y-%m-%d-%H").csv
# test cheking white space and upcase and downcase merging files
if ! cmp testbedk.csv testbedk-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "testbedk is ${RED}failing${NC}"
else
    echo "testbedk is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="atfemales10.csv" --file2="defemales10.csv" --output=testatde-$(date "+%Y-%m-%d-%H").csv
# test checking only upcase and downcase merging files
if ! cmp testatde.csv testatde-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "testatde is ${RED}failing${NC}"
else
    echo "testatde is ${GREEN}ok${NC}"
fi

python3 mergeinterfiles.py --file1="esfemeninos10.csv" --file2="ptfemales10.csv" --output=testptes-$(date "+%Y-%m-%d-%H").csv
# checking accents
if ! cmp testptes.csv testptes-$(date "+%Y-%m-%d-%H").csv >/dev/null 2>&1
then
    echo "testptes is ${RED}failing${NC}"
else
    echo "testptes is ${GREEN}ok${NC}"
fi


rm *-2021-*
