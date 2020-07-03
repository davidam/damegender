#!/bin/bash

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

cp config.cfg config.cfg.backup

echo "We need enable apis to execute this script, we are trying to do it for you..."

cp config.enabled.cfg config.cfg

python3 api2gender.py David --api="genderize" > files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/api2genderDavidgenderize.txt files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "api2genderDavidgenderize test is failing"
else
	echo "api2genderDavidgenderize test is ok"
fi

python3 downloadjson.py --api=genderize --csv=files/names/min.csv

if [ -a files/names/genderizefiles_names_min.csv.json ]; then
    echo "download genderize files names min is ok"
else
    echo "download genderize files names min is failing"
fi

if [ -a files/apikeys/namsorpass.txt ]; then
    python3 api2gender.py Leticia --surname="Martin" --api="namsor" > files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt

    if ! cmp files/tests/api2genderLeticianamsor.txt files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo "api2genderLeticianamsor test is failing"
    else
	echo "api2genderLeticianamsor test is ok"
    fi

    python3 downloadjson.py --api=namsor --csv=files/names/min.csv

    if [ -a files/names/namsorfiles_names_min.csv.json ]; then
	echo "download namsor files names min is ok"
    else
	echo "download namsor files names min is failing"
    fi


fi

if [ -a files/apikeys/genderapipass.txt ]; then

    python3 downloadjson.py --api=genderapi --csv=files/names/min.csv

    if [ -a files/names/genderapifiles_names_min.csv.json ]; then
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

    python3 accuracy.py --api="genderapi" --csv="files/names/min.csv" > files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt

    if ! cmp files/tests/accuracygenderapi.txt files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
    then
	echo "accuracygenderapi test is failing"
    else
	echo "accuracygenderapi test is ok"
    fi

fi

rm -rf /tmp/clonedir
echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt

echo "restoring config.cfg"
cp config.cfg.backup config.cfg
