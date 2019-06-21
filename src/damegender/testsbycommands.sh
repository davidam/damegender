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

python3 main.py David > files/tests/maindavid-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/maindavid.txt files/tests/maindavid-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "maindavid test is failing"
else
    echo "maindavid test is ok"
fi

python3 main.py Inés > files/tests/mainines-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainines.txt files/tests/mainines-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainines test is failing"
else
	echo "mainines test is ok"
fi

python3 main.py Alex > files/tests/mainalex-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainalex.txt files/tests/mainalex-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainalex test is failing"
else
	echo "mainalex test is ok"
fi

python3 main.py Andrea > files/tests/mainandrea-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainandrea.txt files/tests/mainandrea-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainandrea test is failing"
else
	echo "mainandrea test is ok"
fi

python3 main.py "Jesús María" > files/tests/mainjesusmaria-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjesusmaria.txt files/tests/mainjesusmaria-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjesusmaria test is failing"
else
	echo "mainjesusmaria test is ok"
fi

python3 main.py "José María" > files/tests/mainjosemaria-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjosemaria.txt files/tests/mainjosemaria-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjosemaria test is failing"
else
	echo "mainjosemaria test is ok"
fi

python3 main.py "Jesús" --total=genderguesser > files/tests/mainjesusgenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainjesusgenderguesser.txt files/tests/mainjesusgenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainjesusgenderguesser test is failing"
else
	echo "mainjesusgenderguesser test is ok"
fi

python3 main.py "Sara" --total=genderguesser > files/tests/mainsaragenderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainsaragenderguesser.txt files/tests/mainsaragenderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainsaragenderguesser test is failing"
else
	echo "mainsaragenderguesser test is ok"
fi

python3 main.py sara --total=genderguesser > files/tests/mainsara2genderguesser-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainsara2genderguesser.txt files/tests/mainsara2genderguesser-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mainsara2genderguesser test is failing"
else
	echo "mainsara2genderguesser test is ok"
fi


python3 main.py Mesa --ml=nltk > files/tests/mainmesa-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mainmesa.txt files/tests/mainmesa-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "mainmesa test is failing"
else
    echo "mainmesa test is ok"
fi

python3 nameincountries.py David > files/tests/nameincountriesdavid-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/nameincountriesdavid.txt files/tests/nameincountriesdavid-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "nameincountries test is failing"
else
	echo "nameincountries test is ok"
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
