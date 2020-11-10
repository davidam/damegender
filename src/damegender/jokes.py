#!/usr/bin/python3
# -*- coding: utf-8 -*-
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



import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--total', default="es", choices=['en', 'es'])
args = parser.parse_args()

import re

filepath_es="files/jokes.es.txt"
filepath_en="files/jokes.en.txt"

if (args.total == "es"):
    filepath = filepath_es
else:
    filepath = filepath_en

lines_count = 0

with open(filepath,'r') as f:
  for l in f:
    lines_count = lines_count +1

num_sentence = random.randint(1,lines_count+1)

with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if (cnt == num_sentence):
            print(line)
