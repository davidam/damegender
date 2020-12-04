#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


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
