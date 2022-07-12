#!/bin/bash
# Copyright (C) 2022  David Arroyo Menéndez (davidam@gmail.com)
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

echo "Do you prefer nose or pytest? (nose|pytest)"

read testing

if [[ "nose" == "$testing" ]]; then
    echo "Launching test using nose unit testing system"
    echo "Write nose command (ex: nosetests)"
    read nose
    $nose test/test_dame_environment.py
    $nose test/test_dame_ethnicity.py
    $nose test/test_dame_gender.py
    $nose test/test_dame_genderapi.py
    $nose test/test_dame_genderguesser.py
    $nose test/test_dame_genderize.py
    $nose test/test_dame_nameapi.py
    $nose test/test_dame_namsor.py
    $nose test/test_dame_nltk.py
    $nose test/test_dame_perceval.py
    $nose test/test_dame_sexmachine.py
    $nose test/test_dame_statistics.py
    $nose test/test_dame_utils.py
fi

if [[ "pytest" == "$testing" ]]; then
    echo "Launching test using pytest unit testing system"
    echo "Write pytest command (ex: pytest)"
    read PYTEST
    $PYTEST test/test_dame_environment.py
    $PYTEST test/test_dame_ethnicity.py
    $PYTEST test/test_dame_gender.py
    $PYTEST test/test_dame_genderapi.py
    $PYTEST test/test_dame_genderguesser.py
    $PYTEST test/test_dame_genderize.py
    $PYTEST test/test_dame_nameapi.py
    $PYTEST test/test_dame_namsor.py
    $PYTEST test/test_dame_nltk.py
    $PYTEST test/test_dame_perceval.py
    $PYTEST test/test_dame_sexmachine.py
    $PYTEST test/test_dame_statistics.py
    $PYTEST test/test_dame_utils.py
fi


