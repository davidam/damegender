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

echo "
[DEFAULT]
" > config.cfg

# genderapi = yes
# genderize = yes
# nameapi = yes
# namsor = yes
# customsearch = yes

# [FILES]
# genderapi = files/apikeys/genderapipass.txt
# genderize = files/apikeys/genderizepass.txt
# genderguesser = files/apikeys/genderguesserpass.txt
# namsor = files/apikeys/namsorpass.txt
# nameapi = files/apikeys/nameapipass.txt
# "

if [ -a files/apikeys/genderapipass.txt ]; then
    echo "genderapi = yes" >> config.cfg
else
    echo "genderapi = no" >> config.cfg
fi

if [ -a files/apikeys/genderizepass.txt ]; then
    echo "genderize = yes" >> config.cfg
else
    echo "genderize = no" >> config.cfg
fi

if [ -a files/apikeys/genderguesserpass.txt ]; then
    echo "genderguesser = yes" >> config.cfg
else
    echo "genderguesser = no" >> config.cfg
fi

if [ -a files/apikeys/namsorpass.txt ]; then
    echo "namsor = yes" >> config.cfg
else
    echo "namsor = no" >> config.cfg
fi

if [ -a files/apikeys/nameapipass.txt ]; then
    echo "nameapi = yes" >> config.cfg
else
    echo "nameapi = no" >> config.cfg
fi

echo "
[FILES]
genderapi = files/apikeys/genderapipass.txt
genderize = files/apikeys/genderizepass.txt
genderguesser = files/apikeys/genderguesserpass.txt
namsor = files/apikeys/namsorpass.txt
nameapi = files/apikeys/nameapipass.txt
" >> config.cfg

python3 git2gender.py https://github.com/davidam/orgguide-es.git --directory="/tmp/clonedir" > files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/git2gender1.txt files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "git2gender1 test is failing"
else
	echo "git2gender1 test is ok"
fi

cd files/mbox
wget -c http://mail-archives.apache.org/mod_mbox/httpd-announce/201706.mbox
cd ../..
python3 mail2gender.py http://mail-archives.apache.org/mod_mbox/httpd-announce/ > files/tests/mail2gender-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mail2gender.txt files/tests/mail2gender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mail2gender test is failing"
else
	echo "mail2gender test is ok"
fi

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
