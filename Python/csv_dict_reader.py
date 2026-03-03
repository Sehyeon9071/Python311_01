import csv

f = open("data2.csv", "r")
reader = csv.DictReader(f)      # 딕셔너리 형식으로 읽어들임.

print(list(reader))

# for row in reader:
#     print(row)

f.close()