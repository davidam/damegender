import codecs
import csv
import re

with codecs.open('Personer_20211005-184237.csv', 'r') as file:
    input = csv.reader(file, delimiter=",", quotechar='|')
    list = []
    count = 0
    for row in input:
        if (count > 1):
            print(row[0])
            print(row[-1])            
            list.append([row[0], row[-1]])
        count = count + 1
        print(count)

malesoutput = "nomales.csv"
fo = open(malesoutput, "w")

count = 0
for i in list:
    if (count > 1):
        name = str(i[0].replace('"', ''))
        freq = str(i[1].replace('"', ''))
        freq = re.sub(r'(\.)', r'0', freq)
        fo.write(name + "," + freq + "\n")
    count = count + 1
fo.close()
