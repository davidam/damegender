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

rm -rf /tmp/clonedir
echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt
