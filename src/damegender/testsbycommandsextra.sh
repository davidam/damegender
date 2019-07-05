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

python3 git2gender.py https://github.com/davidam/workingclasslicense --directory="/tmp/clonedir" > files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/git2gender1.txt files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "git2gender1 test is failing"
else
	echo "git2gender1 test is ok"
fi

python3 api2gender.py David --api="genderize" > files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/api2genderDavidgenderize.txt files/tests/api2genderDavidgenderize-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "api2genderDavidgenderize test is failing"
else
	echo "api2genderDavidgenderize test is ok"
fi

python3 api2gender.py Leticia --surname="Martin" --api="namsor" > files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/api2genderLeticianamsor.txt files/tests/api2genderLeticianamsor-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "api2genderLeticianamsor test is failing"
else
	echo "api2genderLeticianamsor test is ok"
fi

python3 api2gender.py David --api="genderguesser" > files/tests/api2genderDavidgenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/api2genderDavidgenderguesser.txt files/tests/api2genderDavidgenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "api2genderDavidgenderguesser test is failing"
else
	echo "api2genderDavidgenderize test is ok"
fi

python3 api2gender.py Inés --api="genderapi" > files/tests/api2genderInésgenderapi-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/api2genderInésgenderapi.txt files/tests/api2genderInésgenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "api2genderInésgenderapi test is failing"
else
	echo "api2genderInésgenderapi test is ok"
fi


python3 accuracy.py --csv=files/names/min.csv > files/tests/accuracymin-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/accuracymin.txt files/tests/accuracymin-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "accuracymin test is failing"
else
	echo "accuracymin test is ok"
fi

python3 accuracy.py --api="genderguesser" --csv=files/names/min.csv > files/tests/accuracygenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/accuracygenderguesser.txt files/tests/accuracygenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "accuracygenderguesser test is failing"
else
	echo "accuracygenderguesser test is ok"
fi

python3 accuracy.py --api="damegender" --csv=files/names/partial.csv > files/tests/accuracypartialdamegender-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/accuracypartialdamegender.txt files/tests/accuracypartialdamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "accuracypartialdamegender test is failing"
else
	echo "accuracypartialdamegender test is ok"
fi


python3 accuracy.py --api="genderapi" > files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/accuracygenderapi.txt files/tests/accuracygenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "accuracygenderapi test is failing"
else
	echo "accuracygenderapi test is ok"
fi

python3 confusion.py --api="damegender" --dimensions=3x2 --csv=files/names/min.csv > files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusiondamegender.txt files/tests/confusiondamegender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusiondamegender test is failing"
else
	echo "confusiondamegender test is ok"
fi

python3 confusion.py --api="genderguesser" --dimensions=3x2 --csv=files/names/min.csv > files/tests/confusiongenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusiongenderguesser.txt files/tests/confusiongenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusiongenderguesser test is failing"
else
	echo "confusiongenderguesser test is ok"
fi

python3 confusion.py --api="genderapi" > files/tests/confusiongenderapi-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusiongenderapi.txt files/tests/confusiongenderapi-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusiongenderapi test is failing"
else
	echo "confusiongenderapi test is ok"
fi

python3 confusion.py --api="genderize" > files/tests/confusiongenderize-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusiongenderize.txt files/tests/confusiongenderize-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusiongenderize test is failing"
else
	echo "confusiongenderize test is ok"
fi


python3 confusion.py --api="all" > files/tests/confusionall-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/confusionall.txt files/tests/confusionall-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "confusionall test is failing"
else
	echo "confusionall test is ok"
fi


python3 errors.py > files/tests/errors-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/errors.txt files/tests/errors-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "errors test is failing"
else
    echo "errors test is ok"
fi

python3 errors.py --csv="files/names/partial.csv" > files/tests/errorspartial-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/errorspartial.txt files/tests/errorspartial-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "errorspartial test is failing"
else
    echo "errorspartial test is ok"
fi

python3 errors.py --csv="files/names/partial.csv" --api="genderguesser" > files/tests/errorsgenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/errorsgenderguesser.txt files/tests/errorsgenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "errorsgenderguesser test is failing"
else
	echo "errorsgenderguesser test is ok"
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



rm -rf /tmp/clonedir
echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt
