
# -*- coding = UTF-8 -*-

import os

if os.path.exists("sangpum_data.txt"):
    fp = open("sangpum_data.txt", "r", encoding="UTF-8")
    lst = []
    for line in fp:
        dct = {}
        res = line.strip("\n").split(", ")
        dct["code"] = res[0]
        dct["irum"] = res[1]
        dct["su"] = int(res[2])
        dct["price"] = int(res[3])
        dct["kumack"] = dct["su"] * dct["price"]
        lst.append(dct)

    fp.close()
    print("\n\t\t\t *** 제품관리 ***")
    print("========================================")
    print("제품코드    제품명    수량    단가    판매금액")
    print("========================================")

    total = 0

    for dct in lst:
        total += dct["kumack"]
        print(f"{dct['code']}   {dct['irum']}   {dct['su']}   {dct['price']}   {dct['kumack']}")

    print("========================================")
    print(f"                        총 금액 : {total}")

else:
    print("파일이 존재하지 않습니다!!!")