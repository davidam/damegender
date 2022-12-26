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


rm -rf /tmp/clonedir

python3 git2gender.py https://github.com/davidam/orgguide-es.git --directory="/tmp/clonedir" > files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/git2gender1.txt files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e "git2gender1 test is ${RED}failing${NC}"
else
	echo -e "git2gender1 test is ${GREEN}ok${NC}"
fi

rm -rf /tmp/clonedrupal

python3 git2gender.py  https://git.drupalcode.org/project/orgmode.git --directory="/tmp/clonedrupal" --language=us > files/tests/git2genderdrupal-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/git2genderdrupal.txt files/tests/git2genderdrupal-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e "git2genderdrupal test is ${RED}failing${NC}"
else
	echo -e "git2genderdrupal test is ${GREEN}ok${NC}"
fi

python3 git2gender.py  https://git.drupalcode.org/project/orgmode.git --directory="/tmp/clonedrupal" --show=all --verbose --language=es > files/tests/git2genderverbose-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/git2genderverbose.txt files/tests/git2genderverbose-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e "git2genderverbose test is ${RED}failing${NC}"
else
	echo -e "git2genderverbose test is ${GREEN}ok${NC}"
fi

cd files/mbox
wget -c http://mail-archives.apache.org/mod_mbox/httpd-announce/201706.mbox
cd ../..
python3 mail2gender.py http://mail-archives.apache.org/mod_mbox/httpd-announce/ > files/tests/mail2gender-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/mail2gender.txt files/tests/mail2gender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo -e "mail2gender test is ${RED}failing${NC}"
else
	echo -e "mail2gender test is ${GREEN}ok${NC}"
fi

python3 newspaper2gender.py https://elpais.com/espana/catalunya/2021-11-23/el-presupuesto-de-cataluna-rompe-la-unidad-del-bloque-independentista.html > files/tests/newspaper2gender-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/newspaper2gender-$(date "+%Y-%m-%d-%H").txt files/tests/newspaper2gender.txt >/dev/null 2>&1
then
	echo -e  "newspaper2gender test is ${RED}failing${NC}"
else
	echo -e  "newspaper2gender test is ${GREEN}ok${NC}"
fi

python3 newspaper2gender.py https://elpais.com/espana/catalunya/2021-11-23/el-presupuesto-de-cataluna-rompe-la-unidad-del-bloque-independentista.html --total=es > files/tests/newspaper2gender.es-$(date "+%Y-%m-%d-%H").txt

if ! diff files/tests/newspaper2gender.es-$(date "+%Y-%m-%d-%H").txt files/tests/newspaper2gender.es.txt >/dev/null 2>&1
then
	echo -e  "newspaper2gender spanish test is ${RED}failing${NC}"
else
	echo -e  "newspaper2gender spanish test is ${GREEN}ok${NC}"
fi

python3 get-wikidata-names.py female --total=ad

if [ -f names.csv ]
then
       echo -e  "get-wikidata-names.py test is ${GREEN}ok${NC}"
else
       echo -e  "get-wikidata-names.py test is ${RED}failing${NC}"
fi

python3 get-wikidata-surnames.py --total=ad

if [ -f surnames.csv ]
then
       echo -e  "get-wikidata-surnames.py test is ${GREEN}ok${NC}"
else
       echo -e  "get-wikidata-surnames.py test is ${RED}failing${NC}"    
fi

	
rm -rf /tmp/clonedir
rm -rf files/tmp
echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt
