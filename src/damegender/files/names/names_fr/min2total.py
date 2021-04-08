import csv

l = []
with open('min.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    name = ""
    cnt = 0
    for row in reader:
        if (row[0] != name):
            print(name)
            print(cnt)
            l.append([name, cnt])
            name = str(row[0])
            cnt = int(row[2])
        else:
            cnt = cnt + int(row[2])
    l.append([name, cnt])
    print(name)
    print(cnt)

print(l)
fo = open("total.csv", "w")
ll = l[1:len(l)]
print(ll)
for i in ll:
    fo.write(str(i[0]) + "," + str(i[1]) + "\n");

# Cerramos el archivo fichero.txt
fo.close()
