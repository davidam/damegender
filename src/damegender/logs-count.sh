#!/bin/bash
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

python3 count-debian-gender.py > files/logs/count-debian-gender-$(date "+%Y-%m-%d").txt

python3 count-gnu.py --show=all > files/logs/count-gnu-all-$(date "+%Y-%m-%d").txt

python3 count-gnu.py > files/logs/count-gnu-$(date "+%Y-%m-%d").txt

python3 count-forbes.py > files/logs/count-forbes-$(date "+%Y-%m-%d").txt

python3 count-kernel.py > files/logs/count-kernel-$(date "+%Y-%m-%d").txt

python3 count-kernel.py --show=all > files/logs/count-kernel-all-$(date "+%Y-%m-%d").txt

python3 count-kernel.py > files/logs/count-kernel-$(date "+%Y-%m-%d").txt


#python3 count-scientifics.py > files/logs/count-scientifics-$(date "+%Y-%m-%d").txt
