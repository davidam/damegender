#!/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.



RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

cp config.cfg config.cfg.backup

echo "We need enable apis to execute this script, we are trying to do it for you..."

cp config.enabled.cfg config.cfg

if [ -f files/apikeys/genderizepass.txt ]; then

    python3 api2gender.py David --api="genderize" > files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt

    if ! diff files/tests/api2genderDavidgenderize.txt files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo -e "api2genderDavidgenderize test is ${RED}failing${NC}"
    else
	echo -e "api2genderDavidgenderize test is ${GREEN}ok${NC}"
    fi

    python3 downloadjson.py --api=genderize --csv=files/names/min.csv

    if [ -f files/names/genderizefiles_names_min.csv.json ]; then
	echo -e "download genderize files names min is ${GREEN}ok${NC}"
    else
	echo -e "download genderize files names min is ${RED}failing${NC}"
    fi
else
    echo -e "Doesn't exist files/apikeys/genderizepass.txt. You must introduce the api key in this file"
fi

if [ -f files/apikeys/namsorpass.txt ]; then
    python3 api2gender.py Leticia --surname="Martin" --api="namsor" > files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt

    if ! diff files/tests/api2genderLeticianamsor.txt files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo -e "api2genderLeticianamsor test is ${RED}failing${NC}"
    else
	echo -e "api2genderLeticianamsor test is ${GREEN}ok${NC}"
    fi

    python3 downloadjson.py --api=namsor --csv=files/names/min.csv

    if [ -f files/names/namsorfiles_names_min.csv.json ]; then
	echo -e "download namsor files names min is ${GREEN}ok${NC}"
    else
	echo -e "download namsor files names min is ${RED}failing${NC}"
    fi
else
    echo -e "Doesn't exist files/apikeys/namsorpass.txt. You must introduce the api key in this file"

fi

if [ -f files/apikeys/genderapipass.txt ]; then

    python3 downloadjson.py --api=genderapi --csv=files/names/min.csv

    if [ -f files/names/genderapifiles_names_min.csv.json ]; then
	echo -e "download genderapi files names min is ${GREEN}ok${NC}"
    else
	echo -e "download genderapi files names min is ${RED}failing${NC}"
    fi

    python3 api2gender.py Inés --api="genderapi" > files/tests/api2genderInésgenderapi-$(date "+%Y-%m-%d-%H").txt

    if ! diff files/tests/api2genderInésgenderapi.txt files/tests/api2genderInésgenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo -e "api2genderInésgenderapi test is ${RED}failing${NC}"
    else
	echo -e "api2genderInésgenderapi test is ${GREEN}ok${NC}"
    fi

    # python3 accuracy.py --api="genderapi" --csv="files/names/min.csv" > files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt

    # if ! diff files/tests/accuracygenderapi.txt files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    # then
    # 	echo "accuracygenderapi test is failing"
    # else
    # 	echo "accuracygenderapi test is ok"
    # fi
else
    echo "Doesn't exist files/apikeys/genderapipass.txt. You must introduce the api key in this file"

fi

echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt

echo "restoring config.cfg"
cp config.cfg.backup config.cfg
