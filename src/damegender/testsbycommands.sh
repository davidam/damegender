#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.



# First, we save the current config and create the config for the tests

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

python3 main.py David --total=es > files/tests/maindavid-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/maindavid.txt files/tests/maindavid-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "maindavid test is failing"
else
    echo "maindavid test is ok"
fi

python3 main.py Jesús --total=es > files/tests/mainjesus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjesus.txt files/tests/mainjesus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "mainjesus test is failing"
else
    echo "mainjesus test is ok"
fi

python3 main.py Inés --total=es > files/tests/mainines-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainines.txt files/tests/mainines-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainines test is failing"
else
	echo "mainines test is ok"
fi

python3 main.py Alex --total=es > files/tests/mainalex-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainalex.txt files/tests/mainalex-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainalex test is failing"
else
	echo "mainalex test is ok"
fi

python3 main.py Andrea --total=es > files/tests/mainandrea-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainandrea.txt files/tests/mainandrea-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainandrea test is failing"
else
	echo "mainandrea test is ok"
fi

python3 main.py "Jesús María" --total=es > files/tests/mainjesusmaria-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjesusmaria.txt files/tests/mainjesusmaria-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjesusmaria test is failing"
else
	echo "mainjesusmaria test is ok"
fi

python3 main.py "José María" --total=es > files/tests/mainjosemaria-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjosemaria.txt files/tests/mainjosemaria-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjosemaria test is failing"
else
	echo "mainjosemaria test is ok"
fi

python3 main.py Elena --total=luciahelena > files/tests/mainelenaluciahelena-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainelenaluciahelena.txt files/tests/mainelenaluciahelena-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainelenaluciahelena test is failing"
else
	echo "mainelenaluciahelena test is ok"
fi

python3 main.py Julia --total=us > files/tests/mainjuliaus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjuliaus.txt files/tests/mainjuliaus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjuliaus test is failing"
else
	echo "mainjuliaus test is ok"
fi

python3 main.py Julia --total=uk > files/tests/mainjuliauk-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjuliauk.txt files/tests/mainjuliauk-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjuliauk test is failing"
else
	echo "mainjuliauk test is ok"
fi

python3 main.py Julia --total=uy > files/tests/mainjuliauy-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjuliauy.txt files/tests/mainjuliauy-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjuliauy test is failing"
else
	echo "mainjuliauy test is ok"
fi

echo "I am launching a ml test is slow. Please wait"

python3 main.py Amorosa --ml=sgd > files/tests/mainamorosa-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/mainamorosa.txt files/tests/mainamorosa-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "mainamorosa test is failing"
else
    echo "mainamorosa test is ok"
fi

python3 nameincountries.py David > files/tests/nameincountriesdavid-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesdavid.txt files/tests/nameincountriesdavid-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "nameincountries david test is failing"
else
	echo "nameincountries david test is ok"
fi

python3 nameincountries.py david > files/tests/nameincountriesdavid2-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesdavid2.txt files/tests/nameincountriesdavid2-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "nameincountries david donwcase test is failing"
else
	echo "nameincountries david donwcase test is ok"
fi


python3 nameincountries.py Jesús > files/tests/nameincountriesjesus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesjesus.txt files/tests/nameincountriesjesus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "nameincountries jesus test is failing"
else
	echo "nameincountries jesus test is ok"
fi

python3 infofeatures.py es > files/tests/infofeatures-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/infofeatures.txt files/tests/infofeatures-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "infofeatures test is failing"
else
	echo "infofeatures test is ok"
fi

python3 csv2gender.py files/names/partial.csv --first_name_position=0 --dataset=us --noshow > files/tests/csv2genderpartial-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/csv2genderpartial.txt files/tests/csv2genderpartial-$(date "+%Y-%m-%d-%H").txt
then
	echo "csv2genderpartial test is failing"
else
	echo "csv2genderpartial test is ok"
fi

if [ -f files/images/pca_components_files_features_list.csv.png ]; then
    rm files/images/pca_components_files_features_list.csv.png
fi

python3 pca-components.py --csv='files/features_list.csv' --no-show
if [ -f files/images/pca_components_files_features_list.csv.png ]; then
	echo "pca-components test is ok"
else
	echo "pca-components test is failing"
fi

python3 pca-features.py --categorical="both" --components=7 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "pca-features-both test is failing"
else
	echo "pca-features-both test is ok"
fi

if [ -f files/images/pca_components_files_features_list_no_cat.csv.png ]; then
    rm files/images/pca_components_files_features_list_no_cat.csv.png
fi

python3 pca-components.py --csv='files/features_list_no_cat.csv' --no-show
if [ -f files/images/pca_components_files_features_list_no_cat.csv.png ]; then
	echo "pca-components-nocategorical test is ok"
else
	echo "pca-components-nocategorical test is failing"
fi

python3 pca-features.py --categorical="nocategorical" --components=7 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "pca-features-nocategorical test is failing"
else
	echo "pca-features-nocategorical test is ok"
fi

if [ -f files/images/pca_components_files_features_list_cat.csv.png ]; then
    rm files/images/pca_components_files_features_list_cat.csv.png
fi

python3 pca-components.py --csv='files/features_list_cat.csv' --no-show
if [ -f files/images/pca_components_files_features_list_cat.csv.png ]; then
	echo "pca-components-categorical test is ok"
else
	echo "pca-components-categorical test is failing"
fi

python3 pca-features.py --categorical="noletters" --components=3 > files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "pca-features-nocategorical test is failing"
else
	echo "pca-features-nocategorical test is ok"
fi

if [ -f files/images/pca_components_files_features_list_no_undefined.csv.png ]; then
    rm files/images/pca_components_files_features_list_no_undefined.csv.png
fi

python3 pca-components.py --csv='files/features_list_no_undefined.csv' --no-show
if [ -a files/images/pca_components_files_features_list_no_undefined.csv.png ]; then
	echo "pca-components-no-undefined test is ok"
else
	echo "pca-components-no-undefined test is failing"
fi

python3 pca-features.py --categorical="both" --components=3 > files/tests/pca-features-both-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-both.txt files/tests/pca-features-both-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "pca-features-both test is failing"
else
	echo "pca-features-both test is ok"
fi


python3 pca-features.py --categorical="noletters" --components=3 > files/tests/pca-features-categorical-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/pca-features-nocategorical.txt files/tests/pca-features-nocategorical-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "pca-features-nocategorical test is failing"
else
	echo "pca-features-nocategorical test is ok"
fi

python3 confusion.py --csv="files/names/min.csv" --api=damegender --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusion test is failing"
else
	echo "confusion test is ok"
fi

python3 confusion.py --csv="files/names/min.csv" --api=damegender --jsondownloaded=files/names/min.csv.json > files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusion nltk test is failing"
else
	echo "confusion nltk test is ok"
fi

python3 confusion.py --csv="files/names/min.csv" --api=genderapi --jsondownloaded="files/names/genderapifiles_names_min.csv.json" --reverse > files/tests/confusiongenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusiongenderapijsondownloaded.txt files/tests/confusiongenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusion genderapi jsondonwloaded test is failing"
else
	echo "confusion genderapi jsondonwloaded test is ok"
fi


python3 confusion.py --csv=files/names/partialnoundefined.csv --api=genderize --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --reverse > files/tests/confusion-genderize-partialnoun-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusion-genderize-partialnoun.txt files/tests/confusion-genderize-partialnoun-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusion genderize jsondonwloaded test is failing"
else
	echo "confusion genderize jsondonwloaded test is ok"
fi


python3 confusion.py --csv="files/names/partial.csv" --api=nameapi --jsondownloaded="files/names/nameapifiles_names_partial.csv.json" --reverse > files/tests/confusionnameapijsondownloaded-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/confusionnameapijsondownloaded.txt files/tests/confusionnameapijsondownloaded-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusion nameapi jsondonwloaded test is failing"
else
	echo "confusion nameapi jsondonwloaded test is ok"
fi


python3 accuracy.py --csv="files/names/min.csv" --api=genderapi --jsondownloaded="files/names/genderapifiles_names_min.csv.json" > files/tests/accuracygenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderapijsondownloaded.txt files/tests/accuracygenderapijsondownloaded-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "accuracy genderapi jsondonwloaded test is failing"
else
	echo "accuracy genderapi jsondonwloaded test is ok"
fi

python3 accuracy.py --csv=files/names/partial.csv --api=nameapi --json="files/names/nameapifiles_names_partial.csv.json" > files/tests/accuracypartialjsonnameapi-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracypartialjsonnameapi.txt files/tests/accuracypartialjsonnameapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "accuracy nameapi jsondonwloaded test is failing"
else
	echo "accuracy nameapi jsondonwloaded test is ok"
fi

python3 accuracy.py --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=f1score --api=genderize --csv=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonf1score-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizepartialjsonf1score.txt files/tests/accuracygenderizepartialjsonf1score-$(date "+%Y-%m-%d-%H").txt
then
	echo "accuracy genderize f1score jsondonwloaded test is failing"
else
	echo "accuracy genderize f1score jsondonwloaded test is ok"
fi

python3 accuracy.py --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=precision --api=genderize --csv=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonprecision-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizepartialjsonprecision.txt files/tests/accuracygenderizepartialjsonprecision-$(date "+%Y-%m-%d-%H").txt
then
	echo "accuracy genderize precision jsondonwloaded test is failing"
else
	echo "accuracy genderize precision jsondonwloaded test is ok"
fi

python3 accuracy.py --jsondownloaded=files/names/genderizefiles_names_partialnoundefined.csv.json --measure=accuracy --api=genderize --csv=files/names/partialnoundefined.csv > files/tests/accuracygenderizepartialjsonaccuracy-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizepartialjsonaccuracy.txt files/tests/accuracygenderizepartialjsonaccuracy-$(date "+%Y-%m-%d-%H").txt
then
	echo "accuracy genderize accuracy jsondonwloaded test is failing"
else
	echo "accuracy genderize accuracy jsondonwloaded test is ok"
fi


python3 accuracy.py --jsondownloaded=files/names/min.csv.json --measure=recall --api=damegender --csv=files/names/min.csv > files/tests/accuracygenderizeminjsonrecall-$(date "+%Y-%m-%d-%H").txt
if ! cmp files/tests/accuracygenderizeminjsonrecall.txt files/tests/accuracygenderizeminjsonrecall-$(date "+%Y-%m-%d-%H").txt
then
	echo "accuracy genderize recall jsondonwloaded test is failing"
else
	echo "accuracy genderize recall jsondonwloaded test is ok"
fi


# python3 damegender2json.py --notoutput --csv=files/names/min.csv --jsonoutput=files/names/min.csv.$(date "+%Y-%m-%d-%H").json

# if ! cmp files/names/min.csv.json files/names/min.csv.$(date "+%Y-%m-%d-%H").json
# then
# 	echo "damegender2json test is failing"
# else
# 	echo "damegender2json test is ok"
# fi


# python3 damegender2json.py --notoutput --csv=files/names/partial.csv --ml=svc --jsonoutput=files/names/partial.csv.svc.$(date "+%Y-%m-%d-%H").json

# if ! cmp files/names/partial.csv.svc.json files/names/partial.csv.svc.$(date "+%Y-%m-%d-%H").json
# then
# 	echo "damegender2json test svc is failing"
# else
# 	echo "damegender2json test svc is ok"
# fi

python3 main.py David --verbose > files/tests/maindavidverbose-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/maindavidverbose.txt files/tests/maindavidverbose-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "maindavidverbose test is failing"
else
	echo "maindavidverbose test is ok"
fi

python3 surname.py Gil --total=es > files/tests/surnamegil-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnamegil.txt files/tests/surnamegil-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "surnamegil test is failing"
else
	echo "surnamegil test is ok"
fi

python3 surname.py López --total=us > files/tests/surnamelopezus-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnamelopezus.txt files/tests/surnamelopezus-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "surnamelopez test is failing"
else
	echo "surnamelopez test is ok"
fi

python3 ethnicity.py Walls > files/tests/ethnicitywalls-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/ethnicitywalls.txt files/tests/ethnicitywalls-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "ethnicitywalls test is failing"
else
	echo "ethnicitywalls test is ok"
fi

python3 surnameincountries.py Arroyo > files/tests/surnameincountries-arroyo-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnameincountries-arroyo.txt files/tests/surnameincountries-arroyo-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "surnamearroyo test is failing"
else
	echo "surnamearroyo test is ok"
fi

python3 surnameincountries.py Gil > files/tests/surnameincountries-gil-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnameincountries-gil.txt files/tests/surnameincountries-gil-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "surnameincountriesgil test is failing"
else
	echo "surnameincountriesgil test is ok"
fi

python3 surname.py Menendez --total=es --spanish_provinces > files/tests/surnamemenendezprovinces-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnamemenendezprovinces.txt files/tests/surnamemenendezprovinces-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "surnamemenendezprovinces test is failing"
else
	echo "surnamemenendezprovinces test is ok"
fi

python3 surnameincountries.py Menéndez > files/tests/surnameincountries-menendez-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/surnameincountries-menendez.txt files/tests/surnameincountries-menendez-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "surnamemenendez test is failing"
else
	echo "surnamemenendez test is ok"
fi


python3 errors.py --csv=files/names/partial.csv --jsondownloaded=files/names/partial.csv.nltk.json > files/tests/errorspartialnltk-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/errorspartialnltk.txt files/tests/errorspartialnltk-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "errors test is failing"
else
	echo "errors test is ok"
fi

python3 top.py es > files/tests/topes-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/topes.txt files/tests/topes-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "top test is failing"
else
	echo "top test is ok"
fi

if [ -f files/images/roc_gaussianNB.png ]; then
    rm files/images/roc_gaussianNB.png
fi

python3 roc.py gaussianNB --noshow
if [ -f files/images/roc_gaussianNB.png ]; then
	echo "roc test is ok"
else
	echo "roc test is failing"
fi

echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt

echo "restoring the config"
cp config.cfg.backup config.cfg
rm config.cfg.backup
