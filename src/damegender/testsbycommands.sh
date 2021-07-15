#!/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.



# First, we save the current config and create the config for the tests

cp config.cfg config.cfg.backup

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


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

python3 main.py David --total=es > files/tests/maindavid-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/maindavid.txt files/tests/maindavid-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo -e  "maindavid test is ${RED}failing${NC}"
else
    echo -e  "maindavid test is ${GREEN}ok${NC}"
fi

python3 main.py Jesús --total=es > files/tests/mainjesus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjesus.txt files/tests/mainjesus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo -e  "mainjesus test is ${RED}failing${NC}"
else
    echo -e  "mainjesus test is ${GREEN}ok${NC}"
fi

python3 main.py Inés --total=es > files/tests/mainines-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainines.txt files/tests/mainines-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainines test is ${RED}failing${NC}"
else
	echo -e  "mainines test is ${GREEN}ok${NC}"
fi

python3 main.py Alex --total=es > files/tests/mainalex-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainalex.txt files/tests/mainalex-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainalex test is ${RED}failing${NC}"
else
	echo -e  "mainalex test is ${GREEN}ok${NC}"
fi

python3 main.py Andrea --total=es > files/tests/mainandrea-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainandrea.txt files/tests/mainandrea-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainandrea test is ${RED}failing${NC}"
else
	echo -e  "mainandrea test is ${GREEN}ok${NC}"
fi

python3 main.py "Jesús María" --total=es > files/tests/mainjesusmaria-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjesusmaria.txt files/tests/mainjesusmaria-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainjesusmaria test is ${RED}failing${NC}"
else
	echo -e  "mainjesusmaria test is ${GREEN}ok${NC}"
fi

python3 main.py "José María" --total=es > files/tests/mainjosemaria-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjosemaria.txt files/tests/mainjosemaria-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainjosemaria test is ${RED}failing${NC}"
else
	echo -e  "mainjosemaria test is ${GREEN}ok${NC}"
fi

# Deprecating luciahelena
# python3 main.py Elena --total=luciahelena > files/tests/mainelenaluciahelena-$(date "+%Y-%m-%d-%H").txt

# if ! cmp files/tests/mainelenaluciahelena.txt files/tests/mainelenaluciahelena-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
# then
# 	echo -e  "mainelenaluciahelena test is ${RED}failing${NC}"
# else
# 	echo -e  "mainelenaluciahelena test is ${GREEN}ok${NC}"
# fi

python3 main.py Julia --total=us > files/tests/mainjuliaus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjuliaus.txt files/tests/mainjuliaus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainjuliaus test is ${RED}failing${NC}"
else
	echo -e  "mainjuliaus test is ${GREEN}ok${NC}"
fi

python3 main.py Julia --total=gb > files/tests/mainjuliagb-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjuliagb.txt files/tests/mainjuliagb-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainjuliauk test is ${RED}failing${NC}"
else
	echo -e  "mainjuliauk test is ${GREEN}ok${NC}"
fi

python3 main.py Julia --total=uy > files/tests/mainjuliauy-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjuliauy.txt files/tests/mainjuliauy-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "mainjuliauy test is ${RED}failing${NC}"
else
	echo -e  "mainjuliauy test is ${GREEN}ok${NC}"
fi

echo -e  "I am launching a ml test is slow. Please wait"

python3 main.py Amorosa --ml=sgd --total=us > files/tests/mainamorosa-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/mainamorosa.txt files/tests/mainamorosa-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo -e  "mainamorosa test is ${RED}failing${NC}"
else
    echo -e  "mainamorosa test is ${GREEN}ok${NC}"
fi

python3 main.py 阿 --total=cn > files/tests/mainchina-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainchina.txt files/tests/mainchina-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo -e  "mainchina test is ${RED}failing${NC}"
else
    echo -e  "mainchina test is ${GREEN}ok${NC}"
fi


python3 nameincountries.py David > files/tests/nameincountriesdavid-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesdavid.txt files/tests/nameincountriesdavid-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "nameincountries david test is ${RED}failing${NC}"
else
	echo -e  "nameincountries david test is ${GREEN}ok${NC}"
fi

python3 nameincountries.py david > files/tests/nameincountriesdavid2-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesdavid2.txt files/tests/nameincountriesdavid2-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "nameincountries david donwcase test is ${RED}failing${NC}"
else
	echo -e  "nameincountries david donwcase test is ${GREEN}ok${NC}"
fi


python3 nameincountries.py Jesús > files/tests/nameincountriesjesus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesjesus.txt files/tests/nameincountriesjesus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "nameincountries jesus test is ${RED}failing${NC}"
else
	echo -e  "nameincountries jesus test is ${GREEN}ok${NC}"
fi

python3 infofeatures.py es > files/tests/infofeatures-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/infofeatures.txt files/tests/infofeatures-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "infofeatures test is ${RED}failing${NC}"
else
	echo -e  "infofeatures test is ${GREEN}ok${NC}"
fi

python3 csv2gender.py files/names/partial.csv --first_name_position=0 --dataset=us --noshow > files/tests/csv2genderpartial-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/csv2genderpartial.txt files/tests/csv2genderpartial-$(date "+%Y-%m-%d-%H").txt
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

python3 pca-features.py --categorical="both" --components=7 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
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

python3 pca-features.py --categorical="nocategorical" --components=7 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
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

python3 pca-features.py --categorical="noletters" --components=3 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
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

python3 pca-features.py --categorical="both" --components=3 > files/tests/pca-features-both-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-both.txt files/tests/pca-features-both-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "pca-features-both test is ${RED}failing${NC}"
else
	echo -e  "pca-features-both test is ${GREEN}ok${NC}"
fi


python3 pca-features.py --categorical="noletters" --components=3 > files/tests/pca-features-categorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "pca-features-nocategorical test is ${RED}failing${NC}"
else
	echo -e  "pca-features-nocategorical test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv="files/names/min.csv" --api=damegender --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion test is ${RED}failing${NC}"
else
	echo -e  "confusion test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv="files/names/min.csv" --api=damegender --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion nltk test is ${RED}failing${NC}"
else
	echo -e  "confusion nltk test is ${GREEN}ok${NC}"
fi

python3 confusion.py --csv="files/names/min.csv" --api=genderapi --jsondownloaded="files/names/genderapifiles_names_min.csv.json" --reverse > files/tests/confusiongenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusiongenderapijsondownloaded.txt files/tests/confusiongenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion genderapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "confusion genderapi jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 confusion.py --csv=files/names/partialnoundefined.csv --api=genderize --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --reverse > files/tests/confusion-genderize-partialnoun-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusion-genderize-partialnoun.txt files/tests/confusion-genderize-partialnoun-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion genderize jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "confusion genderize jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 confusion.py --csv="files/names/partial.csv" --api=nameapi --jsondownloaded="files/names/nameapifiles_names_partial.csv.json" --reverse > files/tests/confusionnameapijsondownloaded-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusionnameapijsondownloaded.txt files/tests/confusionnameapijsondownloaded-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "confusion nameapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "confusion nameapi jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 accuracy.py --csv="files/names/min.csv" --api=genderapi --jsondownloaded="files/names/genderapifiles_names_min.csv.json" > files/tests/accuracygenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderapijsondownloaded.txt files/tests/accuracygenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracy genderapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderapi jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --csv=files/names/partial.csv --api=nameapi --json="files/names/nameapifiles_names_partial.csv.json" > files/tests/accuracypartialjsonnameapi-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracypartialjsonnameapi.txt files/tests/accuracypartialjsonnameapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "accuracy nameapi jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy nameapi jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=f1score --api=genderize --csv=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonf1score-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizepartialjsonf1score.txt files/tests/accuracygenderizepartialjsonf1score-$(date "+%Y-%m-%d-%H").txt
then
	echo -e  "accuracy genderize f1score jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize f1score jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=precision --api=genderize --csv=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonprecision-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizepartialjsonprecision.txt files/tests/accuracygenderizepartialjsonprecision-$(date "+%Y-%m-%d-%H").txt
then
	echo -e  "accuracy genderize precision jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize precision jsondonwloaded test is ${GREEN}ok${NC}"
fi

python3 accuracy.py --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=accuracy --api=genderize --csv=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonaccuracy-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizepartialjsonaccuracy.txt files/tests/accuracygenderizepartialjsonaccuracy-$(date "+%Y-%m-%d-%H").txt
then
	echo -e  "accuracy genderize accuracy jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize accuracy jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 accuracy.py --jsondownloaded=files/names/min.csv.json --measure=recall --api=damegender --csv=files/names/min.csv > files/tests/accuracygenderizeminjsonrecall-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizeminjsonrecall.txt files/tests/accuracygenderizeminjsonrecall-$(date "+%Y-%m-%d-%H").txt
then
	echo -e  "accuracy genderize recall jsondonwloaded test is ${RED}failing${NC}"
else
	echo -e  "accuracy genderize recall jsondonwloaded test is ${GREEN}ok${NC}"
fi


python3 damegender2json.py --notoutput --csv=files/names/min.csv --jsonoutput=files/names/min.csv.$(date "+%Y-%m-%d-%H").json

if ! cmp files/names/min.csv.json files/names/min.csv.$(date "+%Y-%m-%d-%H").json
then
	echo -e  "damegender2json test is ${RED}failing${NC}"
else
	echo -e  "damegender2json test is ${GREEN}ok${NC}"
fi


python3 damegender2json.py --notoutput --csv=files/names/partial.csv --ml=svc --jsonoutput=files/names/partial.csv.svc.$(date "+%Y-%m-%d-%H").json

if ! cmp files/names/partial.csv.svc.json files/names/partial.csv.svc.$(date "+%Y-%m-%d-%H").json
then
	echo -e  "damegender2json test svc is ${RED}failing${NC}"
else
	echo -e  "damegender2json test svc is ${GREEN}ok${NC}"
fi

python3 main.py David --verbose > files/tests/maindavidverbose-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/maindavidverbose.txt files/tests/maindavidverbose-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "maindavidverbose test is ${RED}failing${NC}"
else
	echo -e  "maindavidverbose test is ${GREEN}ok${NC}"
fi

python3 surname.py Gil --total=es > files/tests/surnamegil-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnamegil.txt files/tests/surnamegil-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "surnamegil test is ${RED}failing${NC}"
else
	echo -e  "surnamegil test is ${GREEN}ok${NC}"
fi

python3 surname.py López --total=us > files/tests/surnamelopezus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnamelopezus.txt files/tests/surnamelopezus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "surnamelopez test is ${RED}failing${NC}"
else
	echo -e  "surnamelopez test is ${GREEN}ok${NC}"
fi

python3 ethnicity.py Walls > files/tests/ethnicitywalls-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/ethnicitywalls.txt files/tests/ethnicitywalls-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "ethnicitywalls test is ${RED}failing${NC}"
else
	echo -e  "ethnicitywalls test is ${GREEN}ok${NC}"
fi

python3 surnameincountries.py Arroyo > files/tests/surnameincountries-arroyo-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnameincountries-arroyo.txt files/tests/surnameincountries-arroyo-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "surnamearroyo test is ${RED}failing${NC}"
else
	echo -e  "surnamearroyo test is ${GREEN}ok${NC}"
fi

python3 surnameincountries.py Gil > files/tests/surnameincountries-gil-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnameincountries-gil.txt files/tests/surnameincountries-gil-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "surnameincountriesgil test is ${RED}failing${NC}"
else
	echo -e  "surnameincountriesgil test is ${GREEN}ok${NC}"
fi

python3 surname.py Menendez --total=es --spanish_provinces > files/tests/surnamemenendezprovinces-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnamemenendezprovinces.txt files/tests/surnamemenendezprovinces-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "surnamemenendezprovinces test is ${RED}failing${NC}"
else
	echo -e  "surnamemenendezprovinces test is ${GREEN}ok${NC}"
fi

python3 surnameincountries.py Menéndez > files/tests/surnameincountries-menendez-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnameincountries-menendez.txt files/tests/surnameincountries-menendez-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "surnamemenendez test is ${RED}failing${NC}"
else
	echo -e  "surnamemenendez test is ${GREEN}ok${NC}"
fi


python3 errors.py --csv=files/names/partial.csv --jsondownloaded=files/names/partial.csv.nltk.json > files/tests/errorspartialnltk-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/errorspartialnltk.txt files/tests/errorspartialnltk-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e  "errors test is ${RED}failing${NC}"
else
	echo -e  "errors test is ${GREEN}ok${NC}"
fi

python3 top.py es > files/tests/topes-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/topes.txt files/tests/topes-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
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

echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt

echo "restoring the config"
cp config.cfg.backup config.cfg
rm config.cfg.backup
