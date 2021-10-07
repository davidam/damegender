import codecs
import csv
import re

with codecs.open('Personer_20211003-224940.csv', 'r', encoding='utf8') as file:
    input = csv.reader(file, delimiter=";", quotechar='|')
    list = []
    count = 0
    for row in input:
        if (count > 1):
            list.append([row[0], row[-1]])
        count = count + 1
        print(count)
#print(list)

femalesoutput = "nofemales.csv"

with open(femalesoutput, 'w', encoding='utf8') as fo:
    count = 0
    for i in list:
        if (count > 0):
            name = str(i[0].replace('"', ''))
            freq = str(i[1].replace('"', ''))
            freq = re.sub(r'(\.)', r'0', freq)
            if (name != ""):
                fo.write(name + "," + freq + "\n")
        count = count +1
    fo.close()
