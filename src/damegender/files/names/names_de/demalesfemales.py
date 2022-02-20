#!/usr/bin/python
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import csv

total = []

diccfemales = {}
diccmales = {}

# # We start collecting 2009 data for females
with open('Vornamen_Koeln_2010.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[0] in diccmales.keys()):
                val = diccmales[row[0]]
                diccmales[row[0]] = int(val) + int(row[1])
            else:
                diccmales[row[0]] = row[1]
        elif (row[2] == 'w'):
            if (row[0] in diccfemales.keys()):
                val = diccfemales[row[0]]
                diccfemales[row[0]] = int(val) + int(row[1])
            else:
                diccfemales[row[0]] = row[1]
            
#         # total = total + dicc
#         # print("name: %s" % row[3])        
#         # print("number: %s" % row[4])
#         # print(dicc)

# We start collecting 2009 data for females
with open('Vornamen_Koeln_2011.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[0] in diccmales.keys()):
                val = diccmales[row[0]]
                diccmales[row[0]] = int(val) + int(row[1])
            else:
                diccmales[row[0]] = row[1]
        elif (row[2] == 'w'):
            # print(row)
            # print(diccfemales.keys())
            if (row[0] in diccfemales.keys()):
#                print(row[1])
                val = diccfemales[row[0]]
                diccfemales[row[0]] = int(val) + int(row[1])
            else:
                diccfemales[row[0]] = row[1]


with open('Vornamen_Koeln_2012.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[0] in diccmales.keys()):
                val = diccmales[row[0]]
                diccmales[row[0]] = int(val) + int(row[1])
            else:
                diccmales[row[0]] = row[1]
        elif (row[2] == 'w'):
            if (row[0] in diccfemales.keys()):
                val = diccfemales[row[0]]
                diccfemales[row[0]] = int(val) + int(row[1])
            else:
                diccfemales[row[0]] = row[1]
                
with open('Vornamen_Koeln_2013.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[0] in diccmales.keys()):
                val = diccmales[row[0]]
                diccmales[row[0]] = int(val) + int(row[1])
            else:
                diccmales[row[0]] = row[1]
        elif (row[2] == 'w'):
            if (row[0] in diccfemales.keys()):
                val = diccfemales[row[0]]
                diccfemales[row[0]] = int(val) + int(row[1])
            else:
                diccfemales[row[0]] = row[1]
        

with open('Vornamen_Koeln_2014.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in sreader:
        print(row)
        if (row[2] == 'm'):
            if (row[0] in diccmales.keys()):
                val = diccmales[row[0]]
                diccmales[row[0]] = int(val) + int(row[1])
            else:
                diccmales[row[0]] = row[1]
        elif (row[2] == 'w'):
            if (row[0] in diccfemales.keys()):
                val = diccfemales[row[0]]
                diccfemales[row[0]] = int(val) + int(row[1])
            else:
                diccfemales[row[0]] = row[1]

with open('Vornamen_Koeln_2015.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[1] in diccmales.keys()):
                val = diccmales[row[1]]
                diccmales[row[1]] = int(val) + int(row[0])
            else:
                diccmales[row[1]] = int(row[0])
        elif (row[2] == 'w'):
            print(row)
            print(diccfemales.keys())
            if (row[1] in diccfemales.keys()):
                print(row[1])
                val = diccfemales[row[1]]
                diccfemales[row[1]] = int(val) + int(row[0])
            else:
                diccfemales[row[1]] = int(row[0])

with open('Vornamen_Koeln_2016.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[1] in diccmales.keys()):
                val = diccmales[row[1]]
                diccmales[row[1]] = int(val) + int(row[0])
            else:
                diccmales[row[1]] = int(row[0])
        elif (row[2] == 'w'):
            if (row[1] in diccfemales.keys()):
                val = diccfemales[row[1]]
                diccfemales[row[1]] = int(val) + int(row[0])
            else:
                diccfemales[row[1]] = int(row[0])

with open('Vornamen_Koeln_2017.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[1] in diccmales.keys()):
                val = int(diccmales[row[1]])
                diccmales[row[1]] = int(val) + int(row[0])
            else:
                diccmales[row[1]] = int(row[0])
        elif (row[2] == 'w'):
            if (row[1] in diccfemales.keys()):
                val = diccfemales[row[1]]
                diccfemales[row[1]] = int(val) + int(row[0])
            else:
                diccfemales[row[1]] = int(row[0])

#Vornamen_2018_Koeln.csv

with open('Vornamen_2018_Koeln.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')    
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[1] in diccmales.keys()):
                val = diccmales[row[1]]
                diccmales[row[1]] = int(val) + int(row[0])
            else:
                diccmales[row[1]] = int(row[0])
        elif (row[2] == 'w'):
            if (row[1] in diccfemales.keys()):
                val = diccfemales[row[1]]
                diccfemales[row[1]] = int(val) + int(row[0])
            else:
                diccfemales[row[1]] = int(row[0])

with open('Vornamen_2019_Koeln.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')    
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[1] in diccmales.keys()):
                val = diccmales[row[1]]
                diccmales[row[1]] = int(val) + int(row[0])
            else:
                diccmales[row[1]] = int(row[0])
        elif (row[2] == 'w'):
            if (row[1] in diccfemales.keys()):
                val = diccfemales[row[1]]
                diccfemales[row[1]] = int(val) + int(row[0])
            else:
                diccfemales[row[1]] = int(row[0])

with open('Vornamen_2020_Koeln.csv') as csvfile:
    next(csvfile) # skipping the header row, first row
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')    
    for row in sreader:
        #print(','.join(row))
        if (row[2] == 'm'):
            if (row[1] in diccmales.keys()):
                val = diccmales[row[1]]
                diccmales[row[1]] = int(val) + int(row[0])
            else:
                diccmales[row[1]] = int(row[0])
        elif (row[2] == 'w'):
            if (row[1] in diccfemales.keys()):
                val = diccfemales[row[1]]
                diccfemales[row[1]] = int(val) + int(row[0])
            else:
                diccfemales[row[1]] = int(row[0])


                
fofemales = open("defemales.csv", "w")
for i in diccfemales.keys():
    fofemales.write(str(i) + "," + str(diccfemales[i]) + "\n")

fofemales.close()    

fomales = open("demales.csv", "w")
for i in diccmales.keys():
    fomales.write(str(i) + "," + str(diccmales[i]) + "\n")

fomales.close()    
