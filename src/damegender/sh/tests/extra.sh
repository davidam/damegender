#!/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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

cd ../..

cp config.cfg config.cfg.backup

echo "
[DEFAULT]
genderapi = no
genderize = no
nameapi = no
namsor = no
customsearch = no

[FILES]
genderapi = files/apikeys/genderapipass.txt
genderize = files/apikeys/genderizepass.txt
genderguesser = files/apikeys/genderguesserpass.txt
namsor = files/apikeys/namsorpass.txt
nameapi = files/apikeys/nameapipass.txt
" > config.cfg

python3 main.py "Jesús" --total=namdict > files/tests/mainjesusnamdict-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/mainjesusnamdict.txt files/tests/mainjesusnamdict-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainjesusnamdict test is ${RED}failing${NC}"
else
	echo -e  "mainjesusnamdict test is ${GREEN}ok${NC}"
fi

python3 main.py "Sara" --total=namdict > files/tests/mainsaranamdict-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/mainsaranamdict.txt files/tests/mainsaranamdict-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainsaranamdict test is ${RED}failing${NC}"
else
	echo -e  "mainsaranamdict test is ${GREEN}ok${NC}"
fi

python3 main.py sara --total=namdict > files/tests/mainsara2namdict-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/mainsaranamdict.txt files/tests/mainsara2namdict-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainsara2namdict test is ${RED}failing${NC}"
else
	echo -e  "mainsara2namdict test is ${GREEN}ok${NC}"
fi

python3 api2gender.py David --api="genderguesser" > files/tests/api2genderDavidgenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/api2genderDavidgenderguesser.txt files/tests/api2genderDavidgenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "api2genderDavidgenderguesser test is ${RED}failing${NC}"
else
	echo -e  "api2genderDavidgenderguesser test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --measure="precision" --dataset_test="files/names/min.csv" --api=genderize --dataset_guess="files/names/genderizefiles_names_min.csv.json" --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="f,m" > files/tests/accuracygenderizeminjsonprecision-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracygenderizeminjsonprecision.txt files/tests/accuracygenderizeminjsonprecision-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracygenderizeminjsonprecision test is ${RED}failing${NC}"
else
	echo -e  "accuracygenderizeminjsonprecision test is ${GREEN}ok${NC}"
fi


python3 accuracy.py --api="genderguesser" --dataset_guess=files/names/min.csv --dataset_test=files/names/min.csv.json --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="f,m" > files/tests/accuracygenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracygenderguesser.txt files/tests/accuracygenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracygenderguesser test is ${RED}failing${NC}"
else
	echo -e  "accuracygenderguesser test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --api="genderguesser" --measure="precision" --dataset_guess=files/names/partialnoundefined.csv --dataset_test=files/names/partialnoundefined.csv.json --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="f,m" > files/tests/accuracygenderguesserpartialnoundefinedjsonprecision-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracygenderguesserpartialnoundefinedjsonprecision.txt files/tests/accuracygenderguesserpartialnoundefinedjsonprecision-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracypartialprecisiongenderguesser test is ${RED}failing${NC}"
else
	echo -e  "accuracypartialprecisiongenderguesser test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --api="genderguesser" --measure="f1score" --dataset_guess=files/names/partialnoundefined.csv --dataset_test=files/names/partialnoundefined.csv.json --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="f,m" > files/tests/accuracygenderguesserpartialnoundefinedjsonf1score-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracygenderguesserpartialnoundefinedjsonf1score.txt files/tests/accuracygenderguesserpartialnoundefinedjsonf1score-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracypartialf1scoregenderguesser test is ${RED}failing${NC}"
else
	echo -e  "accuracypartialf1scoregenderguesser test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --api="genderguesser" --measure="recall" --dataset_guess=files/names/partialnoundefined.csv --dataset_test=files/names/partialnoundefined.csv.json --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4  --dataset_test_gender_chars="f,m" > files/tests/accuracypartialrecallgenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracypartialrecallgenderguesser.txt files/tests/accuracypartialrecallgenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracypartialrecallgenderguesser test is ${RED}failing${NC}"
else
	echo -e  "accuracypartialrecallgenderguesser test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_guess=files/names/partialnoundefined.csv.json --measure=precision --api=damegender --dataset_test=files/names/partialnoundefined.csv.json --dataset_test_gender_chars="f,m" --dataset_guess_gender_chars="f,m" --dataset_guess_position_gender=4 --dataset_test_position_gender=4 > files/tests/accuracypartialnound-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracypartialnound.txt files/tests/accuracypartialnound-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracypartialdamegender test is ${RED}failing${NC}"
else
	echo -e  "accuracypartialdamegender test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_guess=files/names/min.csv.json --measure=precision --api=damegender --dataset_test=files/names/min.csv.json --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_position_gender=4 --dataset_test_gender_chars="f,m" > files/tests/accuracyminjsonjson-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracyminjsonjson.txt files/tests/accuracyminjsonjson-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracyminjsonjson test is ${RED}failing${NC}"
else
	echo -e  "accuracyminjsonjson test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_guess=files/names/min.csv --measure=accuracy --api=damegender --dataset_test=files/names/min.csv.json --dataset_guess_position_gender=4 --dataset_test_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="f,m" > files/tests/accuracymincsvjson-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracymincsvjson.txt files/tests/accuracymincsvjson-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracymincsvjson test is ${RED}failing${NC}"
else
	echo -e  "accuracymincsvjson test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_guess=files/names/min.csv.json --measure=precision --api=damegender --dataset_test=files/names/min.csv --dataset_test_position_gender=4 --dataset_guess_position_gender=4 --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="f,m" > files/tests/accuracyminjsoncsv-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracyminjsoncsv.txt files/tests/accuracyminjsoncsv-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracyminjsoncsv test is ${RED}failing${NC}"
else
	echo -e  "accuracyminjsoncsv test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_guess=files/names/min.csv --dataset_guess_position_gender=4 --measure=accuracy --api=damegender --dataset_test=files/names/min.csv --dataset_test_position_gender=4  --dataset_guess_gender_chars="f,m" --dataset_test_gender_chars="f,m" > files/tests/accuracycsv-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/accuracycsv.txt files/tests/accuracycsv-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracycsv test is ${RED}failing${NC}"
else
	echo -e  "accuracycsv test is ${GREEN}ok${NC}"
fi

python3 confusion.py --api="damegender" --dimensions=2x3 --csv=files/names/min.csv --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusiondamegender test is ${RED}failing${NC}"
else
	echo -e  "confusiondamegender test is ${GREEN}ok${NC}"
fi

python3 confusion.py --api="genderguesser" --dimensions=2x3 --csv=files/names/min.csv --jsondownloaded=files/names/min.csv.json > files/tests/confusiongenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/confusiongenderguesser.txt files/tests/confusiongenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusiongenderguesser test is ${RED}failing${NC}"
else
	echo -e  "confusiongenderguesser test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv=files/names/min.csv --jsondownloaded=files/names/namsorfiles_names_min.csv.json --api=namsor > files/tests/confusionnamsorjson-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/confusionnamsorjson.txt files/tests/confusionnamsorjson-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion namsor test is ${RED}failing${NC}"
else
	echo -e  "confusion namsor test is ${GREEN}ok${NC}"
fi


python3 confusion.py --csv=files/names/min.csv --jsondownloaded=files/names/genderizefiles_names_min.csv.json --api=genderize > files/tests/confusiongenderizejson-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/confusiongenderizejson.txt files/tests/confusiongenderizejson-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion genderize test is ${RED}failing${NC}"
else
	echo -e  "confusion genderize test is ${GREEN}ok${NC}"
fi

python3 errors.py --csv="files/names/partial.csv" --api="genderguesser" > files/tests/errorsgenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/errorsgenderguesser.txt files/tests/errorsgenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "errorsgenderguesser test is ${RED}failing${NC}"
else
	echo -e  "errorsgenderguesser test is ${GREEN}ok${NC}"
fi


rm -rf /tmp/clonedir
echo -e  "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt

echo -e  "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt

echo -e  "restoring the config"
cp config.cfg.backup config.cfg
rm config.cfg.backup
