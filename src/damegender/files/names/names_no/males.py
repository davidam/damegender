import codecs
import csv

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
        fo.write(str(i[0].replace('"', '')) + "," + str(i[1].replace('"', '')) + "\n")
    count = count + 1
fo.close()
