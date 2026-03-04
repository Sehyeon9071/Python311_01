# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv형식으로 저장

import os, csv

def input_data():
    fp = open("sangpum_data.csv", "at", encoding="utf-8", newline='')  # w(write), r(read), a(append), b(binary)
    wr = csv.writer(fp, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)

    dct = {}
    dct["code"] = input("제품코드 입력 => ")
    dct["irum"] = input("제품명 입력 => ")
    dct["su"] = int(input("수량 입력 => "))
    dct["price"] = int(input("단가 입력 => "))
    dct["kumack"] = dct["su"] * dct["price"]

    wr.writerow((dct["code"], dct["irum"], dct["su"], dct["price"], dct["kumack"]))

    fp.close()

    print("\n제품정보 입력 성공!!\n")

def print_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="UTF-8")
        lst = list(csv.reader(fp))

        print("\n\t\t\t *** 제품관리 ***")
        print("=============================================")
        print("제품코드   제품명     수량      단가    판매금액")
        print("=============================================")
        total = 0
        for data in lst:
            total += int(data[4])
            print("%4s     %4s    %4d    %4d    %6d" %
                  (data[0], data[1], int(data[2]), int(data[3]), int(data[4])))
        print("=============================================")
        print("\t\t\t\t\t\t 총금액 : %7d\n" % total)

        fp.close()

    else:
        print("\n출력할 제품 정보가 없음!!!")

if __name__ == "__main__":
    while True:
        menu = int(input("메뉴를 선택하세요(1 ~ 3) => "))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            print("\n프로그램 종료!!")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")
