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
import json
import argparse
import subprocess
import os

from app.dame_utils import DameUtils
from app.dame_wikidata import DameWikidata

dw = DameWikidata()
isocodes = dw.dicc_countries().keys()
codes = list(isocodes) + ["inter", "ine"]

parser = argparse.ArgumentParser()
parser.add_argument('total', default="es", choices=codes)
# parser.add_argument('--regen', default=False, action="store_true")
parser.add_argument('--download', default=False, action="store_true")
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

    if (args.download):
        print("Downloading Argentina names ...")        
        subprocess.call(outpath + "download.sh", shell=True)
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

    du.simple_dicc_to_file(diccmales, outmales)
    du.simple_dicc_to_file(diccmales, outfemales)    

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

    if (args.download):
        print("Downloading Belgium datasets ...")
        subprocess.call(outpath + "download.sh", shell=True) 
   
    print("Belgium males")
    origfile = origpath + 'TA_POP_2009_M.txt'
    print(origfile)    
    dicc = {}

    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2010_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2011_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2012_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2013_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2014_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2015_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2016_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2017_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2018_M.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)

    du.simple_dicc_to_file(dicc, outpath + "bemales.csv")
    
    print("Belgium females")    

    origfile = origpath + 'TA_POP_2009_F.txt'
    print(origfile)    
    dicc = {}
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2010_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2011_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2012_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2013_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2014_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2015_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2016_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2017_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)
    origfile = origpath + 'TA_POP_2018_F.txt'
    print(origfile)
    dicc = du.dump_name_and_quantity_in_dicc(origfile, 3, 4, dicc=dicc)

    du.simple_dicc_to_file(dicc, outpath + "befemales.csv")

elif (country == "ca"):
    origfile = origpath + "baby-names-frequency.csv"

    if (args.download):
        print("Downloading Canada datasets ...")        
        subprocess.call(outpath + "download.sh", shell=True)

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

    if (args.download):
        print("Downloading spanish datasets ...")
        subprocess.call(outpath + "download.sh", shell=True)
    
    du.reduce_csv_columns_to_name_and_freq(origfile, respath=outmales, name=1, freq=2)
    du.reduce_csv_columns_to_name_and_freq(origfile2, respath=outfemales, name=1, freq=2)

elif (country == "ch"):

    if (args.download):
        print("Downloading swiss datasets ...")
        subprocess.call(outpath + "download.sh", shell=True)

    origfile0 = origpath + 'orig.csv.0'
    origfile1 = origpath + 'orig.csv.1'
    origfile2 = origpath + 'orig.csv.2'
    origfile3 = origpath + 'orig.csv.3'
    origfile4 = origpath + 'orig.csv.4'
    origfile5 = origpath + 'orig.csv.5'    

    print("Swiss names ...")
    
    diccmales = {}
    diccmales = du.dump_name_and_quantity_in_dicc(origfile0, 0, 2, dicc=diccmales, delimiter=",")
    diccmales = du.dump_name_and_quantity_in_dicc(origfile1, 0, 2, dicc=diccmales, delimiter=",")
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2, 0, 2, dicc=diccmales, delimiter=",")
    diccmales = du.dump_name_and_quantity_in_dicc(origfile3, 0, 2, dicc=diccmales, delimiter=",")
    diccmales = du.dump_name_and_quantity_in_dicc(origfile4, 0, 2, dicc=diccmales, delimiter=",")
    diccmales = du.dump_name_and_quantity_in_dicc(origfile5, 0, 2, dicc=diccmales, delimiter=",")
    du.simple_dicc_to_file(diccmales, outmales)

    diccfemales = {}
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile0, 0, 1, dicc=diccfemales, delimiter=",")
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile1, 0, 1, dicc=diccfemales, delimiter=",")
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2, 0, 1, dicc=diccfemales, delimiter=",")
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile3, 0, 1, dicc=diccfemales, delimiter=",")
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile4, 0, 1, dicc=diccfemales, delimiter=",")
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile5, 0, 1, dicc=diccfemales, delimiter=",")
    du.simple_dicc_to_file(diccfemales, outfemales)
    
elif (country == "ie"):

    if (args.download):
        print("Downloading ireland datasets ...")
        subprocess.call(outpath + "download.sh", shell=True)

    origfile10 = origpath + 'vsa10.csv'
    origfile11 = origpath + 'vsa11.csv'

    print("Ireland names ...")
    
    diccmales = {}
    diccmales = du.dump_name_and_quantity_in_dicc(origfile11, 5, 7, delimiter=",")

    du.simple_dicc_to_file(diccmales, outmales)
            
    diccfemales = {}
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile10, 5, 7, delimiter=",")

    du.simple_dicc_to_file(diccmales, outmales)

    
elif (country == "it"):
    origpath = outpath + "orig/"    

    if (args.download):
        print("Downloading italian datasets ...")
        subprocess.call(outpath + "download.sh", shell=True)

    origfile2008 = origpath + '2008.csv'
    origfile2009 = origpath + '2009.csv'
    origfile2010 = origpath + '2010.csv'
    origfile2011 = origpath + '2011.csv'
    origfile2012 = origpath + '2012.csv'
    origfile2013 = origpath + '2013.csv'
    origfile2014 = origpath + '2014.csv'
    origfile2015 = origpath + '2015.csv'
    origfile2016 = origpath + '2016.csv'
    origfile2017 = origpath + '2017.csv'
    origfile2018 = origpath + '2018.csv'    

    print("Italian names ...")
    
    diccmales = {}
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2008, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2009, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2010, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2011, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2012, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2013, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2014, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2015, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2016, 1, 2, delimiter=",", dicc=diccmales) 
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2017, 1, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfile2018, 1, 2, delimiter=",", dicc=diccmales)

    du.simple_dicc_to_file(dicc, outmales, dicc=diccmales)
    
    diccfemales = {}
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2008, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2009, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2010, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2011, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2012, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2013, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2014, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2015, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2016, 6, 7, delimiter=",", dicc=diccfemales) 
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2017, 6, 7, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfile2018, 6, 7, delimiter=",", dicc=diccfemales)    

    du.simple_dicc_to_file(dicc, outfemales)    

elif (country == "mx"):
    origmales = origpath + "hombres.csv"
    origfemales = origpath + "mujeres.csv"    

    posname = 0
    posquant = 1
    diccmales = du.dump_name_and_quantity_in_dicc(origmales, posname, posquant, delimiter=",")
    diccfemales = du.dump_name_and_quantity_in_dicc(origfemales, posname, posquant, delimiter=",")
    du.simple_dicc_to_file(diccfemales, outfemales)
    du.simple_dicc_to_file(diccmales, outmales)

    
elif (country == "se"):
    origfemales = origpath + "girls.csv.0"

    if (args.download):
        print("Downloading Sweden datasets ...")        
        subprocess.call(outpath + "download.sh", shell=True)

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

elif (country == "uy"):
    origmales = origpath + "origmales.csv"
    origfemales = origpath + "origfemales.csv"    

    posname = 2
    posquant = 3
    dicc0 = {}
    diccmales = du.dump_name_and_quantity_in_dicc(origmales, posname, posquant, dicc=dicc0, delimiter=",")
    dicc1 = {}
    diccfemales = du.dump_name_and_quantity_in_dicc(origfemales, posname, posquant, dicc=dicc1, delimiter=",")
    du.simple_dicc_to_file(diccfemales, outfemales)
    du.simple_dicc_to_file(diccmales, outmales)

elif (country == "pt"):

    if (args.download):
        print("Downloading datasets from Portugal ...")
        subprocess.call(outpath + "download.sh", shell=True)

    origfilem14 = origpath + 'hombres-2014.csv'
    origfilem15 = origpath + 'hombres-2015.csv'
    origfilem16 = origpath + 'hombres-2016.csv'
    
    origfilef14 = origpath + 'mujeres-2014.csv'
    origfilef15 = origpath + 'mujeres-2015.csv'
    origfilef16 = origpath + 'mujeres-2016.csv'    

    print("Portugal names ...")
    
    diccmales = {}
    diccmales = du.dump_name_and_quantity_in_dicc(origfilem14, 0, 1, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfilem15, 0, 2, delimiter=",", dicc=diccmales)
    diccmales = du.dump_name_and_quantity_in_dicc(origfilem16, 0, 2, delimiter=",", dicc=diccmales)

    du.simple_dicc_to_file(diccmales, outmales)

    diccfemales = {}
    diccfemales = du.dump_name_and_quantity_in_dicc(origfilef14, 0, 1, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfilef15, 0, 2, delimiter=",", dicc=diccfemales)
    diccfemales = du.dump_name_and_quantity_in_dicc(origfilef16, 0, 2, delimiter=",", dicc=diccfemales)

    du.simple_dicc_to_file(diccfemales, outfemales)
    
# if (args.regen):
#     curpath = os.getcwd()
#     subprocess.call(curpath + "/" + "regenerate-gb-files.sh", shell=True)
#     subprocess.call(curpath + "/" + "regenerate-inter-files.sh", shell=True)
#     print("Regenerating inter names and surnames ....")
#     subprocess.call(curpath + "/" + "regenerate-intersurnames.sh", shell=True)
#     subprocess.call(curpath + "/" + "regenerate-malefemale-files.sh", shell=True)
    
