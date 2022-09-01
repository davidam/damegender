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



# First, we save the current config and create the config for the tests

cp config.cfg config.cfg.backup
cp config.disabled.cfg config.cfg

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


python3 main.py David --total=es > files/tests/maindavid-$(date "+%Y-%m-%d").txt

if ! diff files/tests/maindavid.txt files/tests/maindavid-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
    echo -e  "maindavid test is ${RED}failing${NC}"
else
    echo -e  "maindavid test is ${GREEN}ok${NC}"
fi

python3 main.py Jesús --total=es > files/tests/mainjesus-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainjesus.txt files/tests/mainjesus-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
    echo -e  "mainjesus test is ${RED}failing${NC}"
else
    echo -e  "mainjesus test is ${GREEN}ok${NC}"
fi

python3 main.py Inés --total=es > files/tests/mainines-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainines.txt files/tests/mainines-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainines test is ${RED}failing${NC}"
else
	echo -e  "mainines test is ${GREEN}ok${NC}"
fi

python3 main.py Alex --total=es > files/tests/mainalex-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainalex.txt files/tests/mainalex-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainalex test is ${RED}failing${NC}"
else
	echo -e  "mainalex test is ${GREEN}ok${NC}"
fi

python3 main.py Andrea --total=es > files/tests/mainandrea-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainandrea.txt files/tests/mainandrea-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainandrea test is ${RED}failing${NC}"
else
	echo -e  "mainandrea test is ${GREEN}ok${NC}"
fi

python3 main.py "Jesús María" --total=es > files/tests/mainjesusmaria-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainjesusmaria.txt files/tests/mainjesusmaria-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainjesusmaria test is ${RED}failing${NC}"
else
	echo -e  "mainjesusmaria test is ${GREEN}ok${NC}"
fi

python3 main.py "José María" --total=es > files/tests/mainjosemaria-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainjosemaria.txt files/tests/mainjosemaria-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainjosemaria test is ${RED}failing${NC}"
else
	echo -e  "mainjosemaria test is ${GREEN}ok${NC}"
fi

# Deprecating luciahelena
# python3 main.py Elena --total=luciahelena > files/tests/mainelenaluciahelena-$(date "+%Y-%m-%d").txt

# if ! diff files/tests/mainelenaluciahelena.txt files/tests/mainelenaluciahelena-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
# then
# 	echo -e  "mainelenaluciahelena test is ${RED}failing${NC}"
# else
# 	echo -e  "mainelenaluciahelena test is ${GREEN}ok${NC}"
# fi

python3 main.py Julia --total=us > files/tests/mainjuliaus-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainjuliaus.txt files/tests/mainjuliaus-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainjuliaus test is ${RED}failing${NC}"
else
	echo -e  "mainjuliaus test is ${GREEN}ok${NC}"
fi

python3 main.py Алла --total=ru > files/tests/mainanaru-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainanaru.txt files/tests/mainanaru-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainanaru test is ${RED}failing${NC}"
else
	echo -e  "mainanaru test is ${GREEN}ok${NC}"
fi


python3 main.py Julia --total=gb > files/tests/mainjuliagb-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainjuliagb.txt files/tests/mainjuliagb-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainjuliagb test is ${RED}failing${NC}"
else
	echo -e  "mainjuliagb test is ${GREEN}ok${NC}"
fi

python3 main.py Julia --total=uy > files/tests/mainjuliauy-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainjuliauy.txt files/tests/mainjuliauy-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "mainjuliauy test is ${RED}failing${NC}"
else
	echo -e  "mainjuliauy test is ${GREEN}ok${NC}"
fi

echo -e  "I am launching a ml test is slow. Please wait"

python3 main.py Amorosa --ml=sgd --total=us > files/tests/mainamorosa-$(date "+%Y-%m-%d").txt
if ! diff files/tests/mainamorosa.txt files/tests/mainamorosa-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
    echo -e  "mainamorosa test is ${RED}failing${NC}"
else
    echo -e  "mainamorosa test is ${GREEN}ok${NC}"
fi

python3 main.py 阿 --total=cn > files/tests/mainchina-$(date "+%Y-%m-%d").txt

if ! diff files/tests/mainchina.txt files/tests/mainchina-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
    echo -e  "mainchina test is ${RED}failing${NC}"
else
    echo -e  "mainchina test is ${GREEN}ok${NC}"
fi


python3 nameincountries.py David > files/tests/nameincountriesdavid-$(date "+%Y-%m-%d").txt

if ! diff files/tests/nameincountriesdavid.txt files/tests/nameincountriesdavid-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "nameincountries david test is ${RED}failing${NC}"
else
	echo -e  "nameincountries david test is ${GREEN}ok${NC}"
fi

python3 nameincountries.py david > files/tests/nameincountriesdavid2-$(date "+%Y-%m-%d").txt

if ! diff files/tests/nameincountriesdavid2.txt files/tests/nameincountriesdavid2-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "nameincountries david donwcase test is ${RED}failing${NC}"
else
	echo -e  "nameincountries david donwcase test is ${GREEN}ok${NC}"
fi


python3 nameincountries.py Jesús > files/tests/nameincountriesjesus-$(date "+%Y-%m-%d").txt

if ! diff files/tests/nameincountriesjesus.txt files/tests/nameincountriesjesus-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "nameincountries jesus test is ${RED}failing${NC}"
else
	echo -e  "nameincountries jesus test is ${GREEN}ok${NC}"
fi

python3 infofeatures.py es > files/tests/infofeatures-$(date "+%Y-%m-%d").txt

if ! diff files/tests/infofeatures.txt files/tests/infofeatures-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "infofeatures test is ${RED}failing${NC}"
else
	echo -e  "infofeatures test is ${GREEN}ok${NC}"
fi

python3 csv2gender.py files/names/partial.csv --first_name_position=0 --dataset=us --noshow > files/tests/csv2genderpartial-$(date "+%Y-%m-%d").txt

if ! diff files/tests/csv2genderpartial.txt files/tests/csv2genderpartial-$(date "+%Y-%m-%d").txt
then
	echo -e  "csv2genderpartial test is ${RED}failing${NC}"
else
	echo -e  "csv2genderpartial test is ${GREEN}ok${NC}"
fi

if [ -f files/images/pca_components_files_features_list.csv.png ]; then
    rm files/images/pca_components_files_features_list.csv.png
fi

python3 pca-components.py --csv='files/features_list.csv' --no-show
if [ -f files/images/pca_components_files_features_list.csv.png ]; then
	echo -e  "pca-components test is ${GREEN}ok${NC}"
else
	echo -e  "pca-components test is ${RED}failing${NC}"
fi

python3 pca-features.py --categorical="both" --components=7 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt
if ! diff files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "pca-features-both test is ${RED}failing${NC}"
else
	echo -e  "pca-features-both test is ${GREEN}ok${NC}"
fi

if [ -f files/images/pca_components_files_features_list_no_cat.csv.png ]; then
    rm files/images/pca_components_files_features_list_no_cat.csv.png
fi

python3 pca-components.py --csv='files/features_list_no_cat.csv' --no-show
if [ -f files/images/pca_components_files_features_list_no_cat.csv.png ]; then
	echo -e  "pca-components-nocategorical test is ${GREEN}ok${NC}"
else
	echo -e  "pca-components-nocategorical test is ${RED}failing${NC}"
fi

python3 pca-features.py --categorical="nocategorical" --components=7 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt
if ! diff files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "pca-features-nocategorical test is ${RED}failing${NC}"
else
	echo -e  "pca-features-nocategorical test is ${GREEN}ok${NC}"
fi

if [ -f files/images/pca_components_files_features_list_cat.csv.png ]; then
    rm files/images/pca_components_files_features_list_cat.csv.png
fi

python3 pca-components.py --csv='files/features_list_cat.csv' --no-show
if [ -f files/images/pca_components_files_features_list_cat.csv.png ]; then
	echo -e  "pca-components-categorical test is ${GREEN}ok${NC}"
else
	echo -e  "pca-components-categorical test is ${RED}failing${NC}"
fi

python3 pca-features.py --categorical="noletters" --components=3 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt
if ! diff files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "pca-features-nocategorical test is ${RED}failing${NC}"
else
	echo -e  "pca-features-nocategorical test is ${GREEN}ok${NC}"
fi

if [ -f files/images/pca_components_files_features_list_no_undefined.csv.png ]; then
    rm files/images/pca_components_files_features_list_no_undefined.csv.png
fi

python3 pca-components.py --csv='files/features_list_no_undefined.csv' --no-show
if [ -a files/images/pca_components_files_features_list_no_undefined.csv.png ]; then
	echo -e  "pca-components-no-undefined test is ${GREEN}ok${NC}"
else
	echo -e  "pca-components-no-undefined test is ${RED}failing${NC}"
fi

python3 pca-features.py --categorical="both" --components=3 > files/tests/pca-features-both-$(date "+%Y-%m-%d").txt
if ! diff files/tests/pca-features-both.txt files/tests/pca-features-both-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "pca-features-both test is ${RED}failing${NC}"
else
	echo -e  "pca-features-both test is ${GREEN}ok${NC}"
fi


python3 pca-features.py --categorical="noletters" --components=3 > files/tests/pca-features-categorical-$(date "+%Y-%m-%d").txt
if ! diff files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "pca-features-nocategorical test is ${RED}failing${NC}"
else
	echo -e  "pca-features-nocategorical test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv="files/names/min.csv" --api=damegender --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d").txt
if ! diff files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "confusion test is ${RED}failing${NC}"
else
	echo -e  "confusion test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv="files/names/min.csv" --api=damegender --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d").txt
if ! diff files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "confusion nltk test is ${RED}failing${NC}"
else
	echo -e  "confusion nltk test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv="files/names/min.csv" --api=genderapi --jsondownloaded="files/names/genderapifiles_names_min.csv.json" --reverse > files/tests/confusiongenderapijsondownloaded-$(date "+%Y-%m-%d").txt
if ! diff files/tests/confusiongenderapijsondownloaded.txt files/tests/confusiongenderapijsondownloaded-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "confusion genderapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "confusion genderapi jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 confusion.py --csv=files/names/partialnoundefined.csv --api=genderize --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --reverse > files/tests/confusion-genderize-partialnoun-$(date "+%Y-%m-%d").txt

if ! diff files/tests/confusion-genderize-partialnoun.txt files/tests/confusion-genderize-partialnoun-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "confusion genderize jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "confusion genderize jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 confusion.py --csv="files/names/partial.csv" --api=nameapi --jsondownloaded="files/names/nameapifiles_names_partial.csv.json" --reverse > files/tests/confusionnameapijsondownloaded-$(date "+%Y-%m-%d").txt
if ! diff files/tests/confusionnameapijsondownloaded.txt files/tests/confusionnameapijsondownloaded-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "confusion nameapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "confusion nameapi jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 accuracy.py --dataset_guess="files/names/min.csv" --api=genderapi --dataset_test="files/names/genderapifiles_names_min.csv.json" > files/tests/accuracygenderapijsondownloaded-$(date "+%Y-%m-%d").txt
if ! diff files/tests/accuracygenderapijsondownloaded.txt files/tests/accuracygenderapijsondownloaded-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "accuracy genderapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderapi jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_guess=files/names/partial.csv --api=nameapi --dataset_test="files/names/nameapifiles_names_partial.csv.json" > files/tests/accuracypartialjsonnameapi-$(date "+%Y-%m-%d").txt
if ! diff files/tests/accuracypartialjsonnameapi.txt files/tests/accuracypartialjsonnameapi-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "accuracy nameapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy nameapi jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_test=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=f1score --api=genderize --dataset_guess=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonf1score-$(date "+%Y-%m-%d").txt
if ! diff files/tests/accuracygenderizepartialjsonf1score.txt files/tests/accuracygenderizepartialjsonf1score-$(date "+%Y-%m-%d").txt
then
	echo -e  "accuracy genderize f1score jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize f1score jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_test=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=precision --api=genderize --dataset_guess=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonprecision-$(date "+%Y-%m-%d").txt
if ! diff files/tests/accuracygenderizepartialjsonprecision.txt files/tests/accuracygenderizepartialjsonprecision-$(date "+%Y-%m-%d").txt
then
	echo -e  "accuracy genderize precision jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize precision jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --dataset_test=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=accuracy --api=genderize --dataset_guess=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonaccuracy-$(date "+%Y-%m-%d").txt
if ! diff files/tests/accuracygenderizepartialjsonaccuracy.txt files/tests/accuracygenderizepartialjsonaccuracy-$(date "+%Y-%m-%d").txt
then
	echo -e  "accuracy genderize accuracy jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize accuracy jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 accuracy.py --dataset_test=files/names/min.csv.json --measure=recall --api=damegender --dataset_guess=files/names/min.csv > files/tests/accuracygenderizeminjsonrecall-$(date "+%Y-%m-%d").txt
if ! diff files/tests/accuracygenderizeminjsonrecall.txt files/tests/accuracygenderizeminjsonrecall-$(date "+%Y-%m-%d").txt
then
	echo -e  "accuracy genderize recall jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize recall jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 damegender2json.py --notoutput --csv=files/names/min.csv --jsonoutput=files/names/min.csv.$(date "+%Y-%m-%d").json

if ! diff files/names/min.csv.json files/names/min.csv.$(date "+%Y-%m-%d").json
then
	echo -e  "damegender2json test is ${RED}failing${NC}"
else
	echo -e  "damegender2json test is ${GREEN}ok${NC}"
fi


python3 damegender2json.py --notoutput --csv=files/names/partial.csv --ml=svc --jsonoutput=files/names/partial.csv.svc.$(date "+%Y-%m-%d").json

if ! diff files/names/partial.csv.svc.json files/names/partial.csv.svc.$(date "+%Y-%m-%d").json
then
	echo -e  "damegender2json test svc is ${RED}failing${NC}"
else
	echo -e  "damegender2json test svc is ${GREEN}ok${NC}"
fi

python3 main.py David --verbose > files/tests/maindavidverbose-$(date "+%Y-%m-%d").txt

if ! diff files/tests/maindavidverbose.txt files/tests/maindavidverbose-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "maindavidverbose test is ${RED}failing${NC}"
else
	echo -e  "maindavidverbose test is ${GREEN}ok${NC}"
fi

python3 surname.py Gil --total=es > files/tests/surnamegil-$(date "+%Y-%m-%d").txt

if ! diff files/tests/surnamegil.txt files/tests/surnamegil-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "surnamegil test is ${RED}failing${NC}"
else
	echo -e  "surnamegil test is ${GREEN}ok${NC}"
fi

python3 surname.py López --total=us > files/tests/surnamelopezus-$(date "+%Y-%m-%d").txt

if ! diff files/tests/surnamelopezus.txt files/tests/surnamelopezus-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "surnamelopez test is ${RED}failing${NC}"
else
	echo -e  "surnamelopez test is ${GREEN}ok${NC}"
fi

python3 ethnicity.py Walls > files/tests/ethnicitywalls-$(date "+%Y-%m-%d").txt

if ! diff files/tests/ethnicitywalls.txt files/tests/ethnicitywalls-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "ethnicitywalls test is ${RED}failing${NC}"
else
	echo -e  "ethnicitywalls test is ${GREEN}ok${NC}"
fi

python3 surnameincountries.py Arroyo > files/tests/surnameincountries-arroyo-$(date "+%Y-%m-%d").txt

if ! diff files/tests/surnameincountries-arroyo.txt files/tests/surnameincountries-arroyo-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "surnamearroyo test is ${RED}failing${NC}"
else
	echo -e  "surnamearroyo test is ${GREEN}ok${NC}"
fi

python3 surnameincountries.py Gil > files/tests/surnameincountries-gil-$(date "+%Y-%m-%d").txt

if ! diff files/tests/surnameincountries-gil.txt files/tests/surnameincountries-gil-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "surnameincountriesgil test is ${RED}failing${NC}"
else
	echo -e  "surnameincountriesgil test is ${GREEN}ok${NC}"
fi

python3 surname.py Menendez --total=es --spanish_provinces > files/tests/surnamemenendezprovinces-$(date "+%Y-%m-%d").txt

if ! diff files/tests/surnamemenendezprovinces.txt files/tests/surnamemenendezprovinces-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "surnamemenendezprovinces test is ${RED}failing${NC}"
else
	echo -e  "surnamemenendezprovinces test is ${GREEN}ok${NC}"
fi

python3 surnameincountries.py Menéndez > files/tests/surnameincountries-menendez-$(date "+%Y-%m-%d").txt

if ! diff files/tests/surnameincountries-menendez.txt files/tests/surnameincountries-menendez-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "surnamemenendez test is ${RED}failing${NC}"
else
	echo -e  "surnamemenendez test is ${GREEN}ok${NC}"
fi


python3 errors.py --csv=files/names/partial.csv --jsondownloaded=files/names/partial.csv.nltk.json > files/tests/errorspartialnltk-$(date "+%Y-%m-%d").txt

if ! diff files/tests/errorspartialnltk.txt files/tests/errorspartialnltk-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "errors test is ${RED}failing${NC}"
else
	echo -e  "errors test is ${GREEN}ok${NC}"
fi

python3 top.py es > files/tests/topes-$(date "+%Y-%m-%d").txt

if ! diff files/tests/topes.txt files/tests/topes-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "top test is ${RED}failing${NC}"
else
	echo -e  "top test is ${GREEN}ok${NC}"
fi

if [ -f files/images/roc_gaussianNB.png ]; then
    rm files/images/roc_gaussianNB.png
fi

python3 roc.py gaussianNB --noshow
if [ -f files/images/roc_gaussianNB.png ]; then
	echo -e  "roc test is ${GREEN}ok${NC}"
else
	echo -e  "roc test is ${RED}failing${NC}"
fi

mkdir -p files/tmp

python3 csv2jsonapirest.py files/names/names_inter/dkfemales10.csv --outdir="files/tmp" --gender=female --names_by_multiple_files=1 

ls -l files/tmp/*female.json > files/tests/tmpfemalejson-$(date "+%Y-%m-%d").txt

if ! diff files/tests/tmpfemalejson.txt files/tests/tmpfemalejson-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
    echo -e "csv2json test is ${GREEN}ok${NC}"
else
    echo -e "csv2json test is ${RED}failing${NC}"
fi


python3 percentage2names.py 50 --outcsv=files/tests/50-$(date "+%Y-%m-%d").txt

if ! diff files/tests/50.txt files/tests/50-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "percentage2names test is ${RED}failing${NC}"
else
	echo -e  "percentage2names test is ${GREEN}ok${NC}"
fi

python3 percentage2names.py 40 --percentage_until=70 --outcsv=files/tests/40-70-$(date "+%Y-%m-%d").txt

if ! diff files/tests/40-70.txt files/tests/40-70-$(date "+%Y-%m-%d").txt >/dev/null 2>&1
then
	echo -e  "percentage2names test is ${RED}failing${NC}"
else
	echo -e  "percentage2names test is ${GREEN}ok${NC}"
fi



echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt
rm -rf files/tmp/*

echo "restoring the config"
cp config.cfg.backup config.cfg
rm config.cfg.backup
