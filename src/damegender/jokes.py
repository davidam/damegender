#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


import re
import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('--total', default="es", choices=['en', 'es'])
args = parser.parse_args()


filepath_es = "files/jokes.es.txt"
filepath_en = "files/jokes.en.txt"

if (args.total == "es"):
    filepath = filepath_es
else:
    filepath = filepath_en

lines_count = 0

with open(filepath, 'r') as f:
    for i in f:
        lines_count = lines_count + 1

num_sentence = randint(1, lines_count + 1)

with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if (cnt == num_sentence):
            print(line)
