#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  You can share, copy and modify this software if you are a woman or you
#  are David Arroyo Menéndez and you include this note.

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="csv file")
parser.add_argument("--outjson", default="files/names/out.json", help="json file")
parser.add_argument("--outdir", default="files/names/", help="json file")
parser.add_argument('--skip_header', dest='skip_header', action='store_true')
parser.add_argument('--multiple_files', dest='multiple_files', action='store_true')
parser.add_argument('--gender', choices=["male", "female"])

args = parser.parse_args()

du = DameUtils()
s = Gender()

if (args.skip_header):
    csvlist = du.csv2list(args.path, header=True)
else:
    csvlist = du.csv2list(args.path, header=False)

# print(csvlist)

if (args.multiple_files):
    cnt = 0
    for i in csvlist:
        jsonfile = args.outdir + "/" + str(i[0].upper()) + "_" + args.gender + ".json"
        file = open(jsonfile, "w")
        file.write('[{\n')
        file.write('"name": "' + str(i[0].upper()) + '",\n')
        file.write('"frequency": ' + str(i[1]) + ',\n')
        file.write('"gender": "' + str(args.gender) + '"\n')
        file.write('}]\n')
        file.close()
else:
    file = open(str(args.outjson), "w")
    file.write('[')
    cnt = 0
    for i in csvlist:
        file.write('{\n')
        file.write('"name": "' + str(i[0].upper()) + '",\n')
        file.write('"frequency": ' + str(i[1]) + ',\n')
        file.write('"gender": "' + str(args.gender) + '"\n')
        cnt = cnt + 1
        if (len(csvlist) == cnt):
            file.write('}\n')
        else:
            file.write('},\n')
    file.write(']');
    file.close()
