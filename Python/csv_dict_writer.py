import csv

fieldnames = ["id", "name", "price", "amount"]
data = [
    {"id" : "1", "name" : "apple", "price" : "5000", "amount" : "5"},
    {"id" : "2", "name" : "pencil", "price" : "500", "amount" : "42"},
    {"id" : "3", "name" : "pineapple", "price" : "8000", "amount" : "5"},
    {"id" : "4", "name" : "pen", "price" : "1500", "amount" : "10"}
]

f = open("data2.csv", "w")
writer = csv.DictWriter(f, fieldnames=fieldnames)       # 딕셔너리 형식으로 쓰겠다.

writer.writeheader()        # fieldnames 머릿말 출력
# writer.writerows(data)

for row in data:              # 한 줄씩 출력
    writer.writerow(row)

f.close()