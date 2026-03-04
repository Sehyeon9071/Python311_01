# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv형식으로 저장

import os, csv

def menu_title():
    print("*** 제품관리 ***")
    print("1. 제품정보 입력")
    print("2. 제품정보 출력")
    print("3. 제품정보 조회")
    print("4. 제품정보 수정")
    print("5. 제품정보 삭제")
    print("6. 제품정보 종료")
    print()

def input_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "at", encoding="UTF-8")
        fieldnames = ["code", "irum", "su", "price", "kumack"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)

    else:
        fp = open("sangpum_data.csv", "at", encoding="utf-8", newline='')  # w(write), r(read), a(append), b(binary)
        fieldnames = ["code", "irum", "su", "price", "kumack"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    dct = {}
    dct["code"] = input("제품코드 입력 => ")
    dct["irum"] = input("제품명 입력 => ")
    dct["su"] = int(input("수량 입력 => "))
    dct["price"] = int(input("단가 입력 => "))
    dct["kumack"] = dct["su"] * dct["price"]

    wr.writerow(dct)

    fp.close()

    print("\n제품정보 입력 성공!!\n")

def print_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        print("\n\t\t\t *** 제품관리 ***")
        print("=============================================")
        print("제품코드   제품명     수량      단가    판매금액")
        print("=============================================")
        total = 0
        for data in lst:
            total += int(data["kumack"])
            print("%4s     %4s    %4d    %4d    %6d" %
                  (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
        print("=============================================")
        print("\t\t\t\t\t\t 총금액 : %7d\n" % total)

        fp.close()

    else:
        print("\n출력할 제품 정보가 없음!!!")

def search_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        pr_code = input("조회할 제품코드를 입력하세요. => ")

        for data in lst:
            if data["code"] == pr_code:
                print("제품코드   제품명     수량      단가    판매금액")
                print("=============================================")
                print("%4s     %4s    %4d    %4d    %6d" %
                      (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
                print("=============================================\n")
                break
        else:
            print("제품이 존재하지 않습니다.")

        fp.close()

    else:
        print("\n출력할 제품 정보가 없음!!!")

def update_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        pr_code = input("수정할 제품코드를 입력하세요. => ")

        for data in lst:
            if data["code"] == pr_code:
                data["su"] = int(input("수정할 수량을 입력하세요. => "))
                data["price"] = int(input("수정할 단가을 입력하세요. => "))
                data["kumack"] = data["su"] * data["price"]

                fp.close()

                fp = open("sangpum_data.csv", "w", encoding="UTF-8", newline="")
                fieldnames = ["code", "irum", "su", "price", "kumack"]
                wr = csv.DictWriter(fp, fieldnames=fieldnames)

                wr.writeheader()
                wr.writerows(lst)

                fp.close()

                print("\n수정이 완료되었습니다.\n")
                break
        else:
            print("제품이 존재하지 않습니다.")

    else:
        print("\n출력할 제품 정보가 없음!!!")

def delete_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        pr_code = input("수정할 제품코드를 입력하세요. => ")

        for data in lst:
            if data["code"] == pr_code:
                lst.remove(data)

                fp.close()

                fp = open("sangpum_data.csv", "w", encoding="UTF-8", newline="")
                fieldnames = ["code", "irum", "su", "price", "kumack"]
                wr = csv.DictWriter(fp, fieldnames=fieldnames)

                wr.writeheader()
                wr.writerows(lst)

                fp.close()
                print("\n삭제가 완료되었습니다.\n")
                break
        else:
            print("제품이 존재하지 않습니다.")

    else:
        print("\n출력할 제품 정보가 없음!!!")

if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("메뉴를 선택하세요(1 ~ 6) => "))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            search_data()
        elif menu == 4:
            update_data()
        elif menu == 5:
            delete_data()
        elif menu == 6:
            print("\n프로그램 종료!!")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")
