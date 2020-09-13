#!/bin/bash
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

cp config.cfg config.cfg.backup

echo "We need enable apis to execute this script, we are trying to do it for you..."

cp config.enabled.cfg config.cfg

if [ -f files/apikeys/genderizepass.txt ]; then

    python3 api2gender.py David --api="genderize" > files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt

    if ! cmp files/tests/api2genderDavidgenderize.txt files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo "api2genderDavidgenderize test is failing"
    else
	echo "api2genderDavidgenderize test is ok"
    fi

    python3 downloadjson.py --api=genderize --csv=files/names/min.csv

    if [ -f files/names/genderizefiles_names_min.csv.json ]; then
	echo "download genderize files names min is ok"
    else
	echo "download genderize files names min is failing"
    fi
else
    echo "Doesn't exist files/apikeys/genderizepass.txt. You must introduce the api key in this file"
fi

if [ -f files/apikeys/namsorpass.txt ]; then
    python3 api2gender.py Leticia --surname="Martin" --api="namsor" > files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt

    if ! cmp files/tests/api2genderLeticianamsor.txt files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo "api2genderLeticianamsor test is failing"
    else
	echo "api2genderLeticianamsor test is ok"
    fi

    python3 downloadjson.py --api=namsor --csv=files/names/min.csv

    if [ -f files/names/namsorfiles_names_min.csv.json ]; then
	echo "download namsor files names min is ok"
    else
	echo "download namsor files names min is failing"
    fi
else
    echo "Doesn't exist files/apikeys/namsorpass.txt. You must introduce the api key in this file"

fi

if [ -f files/apikeys/genderapipass.txt ]; then

    python3 downloadjson.py --api=genderapi --csv=files/names/min.csv

    if [ -f files/names/genderapifiles_names_min.csv.json ]; then
	echo "download genderapi files names min is ok"
    else
	echo "download genderapi files names min is failing"
    fi

    python3 api2gender.py Inés --api="genderapi" > files/tests/api2genderInésgenderapi-$(date "+%Y-%m-%d-%H").txt

    if ! cmp files/tests/api2genderInésgenderapi.txt files/tests/api2genderInésgenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo "api2genderInésgenderapi test is failing"
    else
	echo "api2genderInésgenderapi test is ok"
    fi

    # python3 accuracy.py --api="genderapi" --csv="files/names/min.csv" > files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt

    # if ! cmp files/tests/accuracygenderapi.txt files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
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
