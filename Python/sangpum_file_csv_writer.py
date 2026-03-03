import csv

# -*- coding: UTF-8 -*-

# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv형식으로 저장

fp = open("sangpum_data.txt", "w", encoding="UTF-8", newline="")    # w(write) => 쓰기, r(read) => 읽기, a(append) => 추가, b(binary) => 2진법
wr = csv.writer(fp, delimiter=",", quotechar = '"', quoting=csv.QUOTE_ALL)

lst = []

total = 0

while True:
    dct = {}
    dct["code"] = input("제품코드 입력 => ")
    if dct["code"].lower() == "exit":
        break
    else:
        dct["irm"] = input("제품명 입력 => ")
        dct["su"] = int(input("수량 입력 => "))
        dct["price"] = int(input("단가 입력 => "))
        dct["kumack"] = dct["su"] * dct["price"]
        lst.append(dct)

        wr.writerow((dct["code"], dct["irm"], dct["su"], dct["price"]))
        print()

fp.close()
# print("\n\t\t\t *** 제품관리 ***")
# print("============================================")
# print("제품코드    제품명    수량    단가        판매금액")
# print("============================================")
#
# for dct in lst:
#     total += dct["kumack"]
#     print(f"{dct['code']}      {dct['irm']}     {dct['su']}   {dct['price']:,}   {dct['kumack']:,}")
#
# print("============================================")
# print(f"                           총 금액 : {total:,}")
