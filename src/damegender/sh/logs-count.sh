#!/bin/bash
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
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

python3 count-debian-gender.py > files/logs/count-debian-gender-$(date "+%Y-%m-%d").txt

python3 count-gnu.py --show=all > files/logs/count-gnu-all-$(date "+%Y-%m-%d").txt

python3 count-gnu.py > files/logs/count-gnu-$(date "+%Y-%m-%d").txt

python3 count-forbes.py > files/logs/count-forbes-$(date "+%Y-%m-%d").txt

python3 count-kernel.py > files/logs/count-kernel-$(date "+%Y-%m-%d").txt

python3 count-kernel.py --show=all > files/logs/count-kernel-all-$(date "+%Y-%m-%d").txt

python3 count-kernel.py > files/logs/count-kernel-$(date "+%Y-%m-%d").txt


#python3 count-scientifics.py > files/logs/count-scientifics-$(date "+%Y-%m-%d").txt
