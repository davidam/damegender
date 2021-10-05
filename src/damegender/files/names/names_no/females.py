import codecs
import csv

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
fo = open(femalesoutput, "w")

count = 0
for i in list:
    if (count > 0):
        fo.write(str(i[0].replace('"', '')) + "," + str(i[1].replace('"', '')) + "\n")
    count = count +1
