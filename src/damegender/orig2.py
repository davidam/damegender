#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidam@gmail.com>
#  Maintainer: David Arroyo Menendez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

import csv
import argparse
from app.dame_utils import DameUtils
from app.dame_wikidata import DameWikidata

dw = DameWikidata()
isocodes = dw.dicc_countries().keys()
codes = list(isocodes) + ["inter", "ine"]

parser = argparse.ArgumentParser()
parser.add_argument('total', default="es", choices=codes)
# More about iso codes on https://www.iso.org/obp/ui/
# You can set alphabet with sufix:
# So russian in latin alphabet would be ru_en
parser.add_argument('--version', action='version', version='0.4')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()

du = DameUtils()

country = args.total
outpath = "files/names/names_" + country + "/"
outmales = outpath + country + "males.csv"
outfemales = outpath + country + "females.csv"
outsurnames = outpath + country + "surnames.csv"

origpath = outpath + "orig/"

if (country == "ar"):
    origfile = origpath + "personas.csv"
    print(origfile)

    print("Processing Argentina names ....")

    with open(origfile) as csvfile:
        sreader2 = csv.reader(csvfile, delimiter=';', quotechar='|')
        diccfemales = {}
        diccmales = {}
        for row in sreader2:
            try:
                gender = str(row[3])
                name = str(row[1])
            except IndexError:
                print("The program has troubles with the array indexes")
            if (gender == '1'):
                if name in diccfemales.keys():
                    diccfemales[name] = int(diccfemales[name]) + 1
                else:
                    diccfemales[name] = 1
            elif (gender == '2'):
                if name in diccmales.keys():
                    diccmales[name] = int(diccmales[name]) + 1
                else:
                    diccmales[name] = 1
    filefem = open(outfemales, 'w')
    filemal = open(outmales, 'w')

    for i in diccfemales.keys():
        str1 = str(i) + ","
        str1 = str1 + str(diccfemales[i]) + "\n"
        filefem.write(str1)
    for j in diccmales.keys():
        str2 = str(j) + ","
        str2 = str2 + str(diccmales[j]) + "\n"
        filemal.write(str2)

    filefem.close()
    filemal.close()

    print("Processing Argentina surnames ....")

    with open(origfile) as csvfile:
        sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(sreader, None)
        filesurnames = open(outsurnames,'w')
        diccsurnames = {}
        for row in sreader:
            if row[2] in diccsurnames.keys():
                diccsurnames[row[2]] = diccsurnames[row[2]] + 1
            else:
                diccsurnames[row[2]] = 1
        
        for i in diccsurnames.keys():
            filesurnames.write(str(i)+","+str(diccsurnames[i])+"\n")
    
    filesurnames.close()

elif (country == "be"):

    print("Belgium males")
    origfile = origpath + 'TA_POP_2009_M.txt'
    print(origfile)    
    dicc = {}
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2010_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2011_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2012_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2013_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2014_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2015_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2016_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2017_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    origfile = origpath + 'TA_POP_2018_M.txt'
    print(origfile)
    dicc = du.fill_befile_in_dicc(origfile, dicc, posname=3, posyear=4)
    fo = open(outpath + "bemales.csv", "w")
    for i in dicc.keys():
        fo.write(str(i) + "," + str(dicc[i]) + "\n")
    fo.close()
    
    print("Belgium females")    

elif (country == "ca"):
    origfile = origpath + "baby-names-frequency.csv"

    dicc = du.init_dicc_names_and_years(origfile, 1, 1980, 2020)

    with open(origfile) as csvfile3:
        reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
        next(reader3, None)
        for row3 in reader3:
            name = row3[1]
            symbols = [" ", "'", '"']
            print(name)
            name = du.drop_all_external_symbols(name, symbols)
            name = name.capitalize()
            if (row3[3] == 'Girl'):
                dicc[name][int(row3[4])]["females"] = row3[2]
            elif (row3[3] == 'Boy'):
                dicc[name][int(row3[4])]["males"] = row3[2]

    for i in dicc.keys():
        males = 0
        females = 0
        for j in dicc[i].keys():
            if (dicc[i][int(j)]["females"] == {}):
                num = 0
            else:
                num = dicc[i][int(j)]["females"]
            females = females + int(num)
            if (dicc[i][int(j)]["males"] == {}):
                num = 0
            else:
                num = dicc[i][int(j)]["males"]
            males = males + int(num)
        dicc[i]["females"] = females
        dicc[i]["males"] = males

    # # # print(dicc["Paula"]["females"])
    jsonvar = json.dumps(dicc)
    fo = open("canames.json", "w")
    fo.write(jsonvar)
    fo.close()

    file = open(outmales, "w")

    for i in dicc.keys():
        if (dicc[i]["males"] > 0):
            line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
            line = line + "," + str(dicc[i]["males"]) + "\n"
            file.write(line)
    file.close()

    file = open(outfemales, "w")
    for i in dicc.keys():
        if (dicc[i]["females"] > 0):
            line = du.drop_external_quotes(du.drop_white_space_around(str(i)))
            line = line + "," + str(dicc[i]["females"]) + "\n"
            file.write(line)
    file.close()

    
elif (country == "es"):
    origpath = outpath + "orig/"    
    origfile = origpath + "esmasculinos.csv"
    origfile2 = origpath + "esfemeninos.csv"

    du.reduce_csv_columns_to_name_and_freq(origfile, respath=outmales, name=1, freq=2)
    du.reduce_csv_columns_to_name_and_freq(origfile2, respath=outfemales, name=1, freq=2)

elif (country == "se"):
    origfemales = origpath + "girls.csv.0"
    
    input = csv.reader(open(origfemales, 'r'), delimiter=",", quotechar='|')
    fo = open(outfemales, "w")

    for cnt, row in enumerate(input):
        if (cnt >= 9):
            acum = 0
            for i in range(1, 24):
                if (row[i] == "-"):
                    x = 0
                else:
                    x = int(row[i])
                acum = acum + x
            fo.write(row[0] + "," + str(acum) + "\n")
    fo.close()

    origmales = origpath + "boys.csv.0"

    input = csv.reader(open(origmales, 'r'), delimiter=",", quotechar='|')
    fo = open(outmales, "w")

    for cnt, row in enumerate(input):
        if (cnt >= 9):
            acum = 0
            for i in range(1, 24):
                if (row[i] == "-"):
                    x = 0
                else:
                    x = int(row[i])                
                acum = acum + x
            fo.write(row[0] + "," + str(acum) + "\n")

    fo.close()

