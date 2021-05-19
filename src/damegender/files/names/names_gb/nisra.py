import codecs
import csv

# fo = open("/tmp/fichero.txt", "w")
# fo.write("Gora python\n");

input = csv.reader(open('northerireland.females.csv', 'r'), delimiter=",", quotechar='|')

print(input)

list =[]

for row in input:
    list.append(row)

fo = open("females.nisra.csv", "w")

for i in list:
#    Name,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016
    # print(i[1])
    # print(i[2])
    # print(i[3])
    # print(i[4])
    name = str(i[0])
    if (str(i[1]) != "-") and (str(i[1]) != ".."):
        i1 = i[1]
    else:
        i1 = 0

    if (str(i[2]) != "-") and (str(i[2]) != ".."):
        i2 = i[2]
    else:
        i2 = 0

    if (str(i[3]) != "-") and (str(i[3]) != ".."):
        i3 = i[3]
    else:
        i3 = 0

    if (str(i[4]) != "-") and (str(i[4]) != ".."):
        #        print(str(i[4]))
        i4 = i[4]
        #       print(i4)
    else:
        i4 = 0

    if (str(i[5]) != "-") and (str(i[5]) != ".."):
        i5 = i[5]
    else:
        i5 = 0

    if (str(i[6]) != "-") and (str(i[6]) != ".."):
        i6 = i[6]
    else:
        i6 = 0

    if (str(i[7]) != "-") and (str(i[7]) != ".."):
        i7 = i[7]
    else:
        i7 = 0

    if (str(i[8]) != "-") and (str(i[8]) != ".."):
        i8 = i[8]
    else:
        i8 = 0

    if (str(i[9]) != "-") and (str(i[9]) != ".."):
        i9 = i[9]
    else:
        i9 = 0

    if (str(i[10]) != "-") and (str(i[10]) != ".."):
        i10 = i[10]
    else:
        i10 = 0

    if (str(i[11]) != "-") and (str(i[11]) != ".."):
        i11 = i[11]
    else:
        i11 = 0

    if (str(i[12]) != "-") and (str(i[12]) != ".."):
        i12 = i[12]
    else:
        i12 = 0

    if (str(i[13]) != "-") and (str(i[13]) != ".."):
        i13 = i[13]
    else:
        i13 = 0

    if (str(i[14]) != "-") and (str(i[14]) != ".."):
        i14 = i[14]
    else:
        i14 = 0

    if (str(i[15]) != "-") and (str(i[15]) != ".."):
        i15 = i[15]
    else:
        i15 = 0

    if (str(i[16]) != "-") and (str(i[16]) != ".."):
        i16 = i[16]
    else:
        i16 = 0

    if (str(i[17]) != "-") and (str(i[17]) != ".."):
        i17 = i[17]
    else:
        i17 = 0

    if (str(i[18]) != "-") and (str(i[18]) != ".."):
        i18 = i[18]
    else:
        i18 = 0

    if (str(i[19]) != "-") and (str(i[19]) != ".."):
        i19 = i[19]
    else:
        i19 = 0

    if (str(i[20]) != "-") and (str(i[20]) != ".."):
        i20 = i[20]
    else:
        i20 = 0
    s = 0
    s = int(i1) + int(i2) + int(i3) + int(i4) + int(i5) + int(i6) + int(i7) + int(i8) + int(i9) + int(i10) + int(i11) + int(i12) + int(i13) + int(i14) + int(i15) + int(i16) + int(i17) + int(i18) + int(i19) + int(i20)
    if (name != "Name"):
        fo.write(name + ',' + str(s) + '\n')
fo.close()


#print(list)
# with codecs.open('females-by-year.csv', 'r', encoding='utf-8') as file:
#     input = csv.reader(file, delimiter=",", quotechar='|')
#     list = []
#     for row in input:
#         list.extend(row)

inputmales = csv.reader(open('northerireland.males.csv', 'r'), delimiter=",", quotechar='|')

print(inputmales)

listmales =[]
for row in inputmales:
    listmales.append(row)


fomales = open("males.nisra.csv", "w")

for i in listmales:
#    Name,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016
    # print(i[1])
    # print(i[2])
    # print(i[3])
    # print(i[4])
    name = str(i[0])
    if (str(i[1]) != "-") and (str(i[1]) != ".."):
        i1 = i[1]
    else:
        i1 = 0

    if (str(i[2]) != "-") and (str(i[2]) != ".."):
        i2 = i[2]
    else:
        i2 = 0

    if (str(i[3]) != "-") and (str(i[3]) != ".."):
        i3 = i[3]
    else:
        i3 = 0

    if (str(i[4]) != "-") and (str(i[4]) != ".."):
        #        print(str(i[4]))
        i4 = i[4]
        #       print(i4)
    else:
        i4 = 0

    if (str(i[5]) != "-") and (str(i[5]) != ".."):
        i5 = i[5]
    else:
        i5 = 0

    if (str(i[6]) != "-") and (str(i[6]) != ".."):
        i6 = i[6]
    else:
        i6 = 0

    if (str(i[7]) != "-") and (str(i[7]) != ".."):
        i7 = i[7]
    else:
        i7 = 0

    if (str(i[8]) != "-") and (str(i[8]) != ".."):
        i8 = i[8]
    else:
        i8 = 0

    if (str(i[9]) != "-") and (str(i[9]) != ".."):
        i9 = i[9]
    else:
        i9 = 0

    if (str(i[10]) != "-") and (str(i[10]) != ".."):
        i10 = i[10]
    else:
        i10 = 0

    if (str(i[11]) != "-") and (str(i[11]) != ".."):
        i11 = i[11]
    else:
        i11 = 0

    if (str(i[12]) != "-") and (str(i[12]) != ".."):
        i12 = i[12]
    else:
        i12 = 0

    if (str(i[13]) != "-") and (str(i[13]) != ".."):
        i13 = i[13]
    else:
        i13 = 0

    if (str(i[14]) != "-") and (str(i[14]) != ".."):
        i14 = i[14]
    else:
        i14 = 0

    if (str(i[15]) != "-") and (str(i[15]) != ".."):
        i15 = i[15]
    else:
        i15 = 0

    if (str(i[16]) != "-") and (str(i[16]) != ".."):
        i16 = i[16]
    else:
        i16 = 0

    if (str(i[17]) != "-") and (str(i[17]) != ".."):
        i17 = i[17]
    else:
        i17 = 0

    if (str(i[18]) != "-") and (str(i[18]) != ".."):
        i18 = i[18]
    else:
        i18 = 0

    if (str(i[19]) != "-") and (str(i[19]) != ".."):
        i19 = i[19]
    else:
        i19 = 0

    if (str(i[20]) != "-") and (str(i[20]) != ".."):
        i20 = i[20]
    else:
        i20 = 0
    s = 0
    s = int(i1) + int(i2) + int(i3) + int(i4) + int(i5) + int(i6) + int(i7) + int(i8) + int(i9) + int(i10) + int(i11) + int(i12) + int(i13) + int(i14) + int(i15) + int(i16) + int(i17) + int(i18) + int(i19) + int(i20)
    if (name != "Name"):
        fomales.write(name + ',' + str(s) + '\n')
fomales.close()
