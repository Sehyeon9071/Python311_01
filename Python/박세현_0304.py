# [문제] 아래 메뉴를 참고하여 성적을 관리할수 있는 프로그램을 완성하시오.
# 저장할 파일은 sungjuk_data.csv 로 한다.

# 제출파일 : 홍길동_0304.py

# *** 성적관리 ***
# 1. 성적정보 입력
# 2. 성적정보 출력
# 3. 성적정보 조회
# 4. 성적정보 수정
# 5. 성적정보 삭제
# 6: 프로그램 종료

# <처리조건>
# 1. 성적정보 입력: input_sungjuk()
#   - 학번,이름,국어,영어,수학 점수를 입력 받아 총점, 평균, 등급을 계산한 다음 파일에 저장한다.
# 2. 성적정보 출력: print_sungjuk()
#   - 파일에 저장된 데이터를 전부 출력한다.
#   - 마지막에 학생수와 전체 평균을 출력한다.
# 3. 성적정보 조회: search_sungjuk()
#   - 학번을 입력받아 해당 학생의 정보를 파일에서 찾아 출력한다.
# 4. 성적정보 수정: update_sungjuk()
#   - 학번을 입력받아 해당 학생의 정보를 파일에서 찾아 국어, 영어, 수학 점수를 새로 입력받아 총점, 평균, 등급을 계산한 후 파일에 저장한다.
# 5. 성적정보 삭제: delete_sungjuk()
#   - 학번을 입력받아 해당 학생의 정보를 파일에서 찾아 삭제한 후 파일에 저장한다.

import os, csv

def menu_title():
    print("*** 성적관리 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")
    print()

def input_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv", "at", encoding="UTF-8")
        fieldnames = ["code", "irum", "kor", "eng", "math", "total", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)

    else:
        fp = open("sungjuk_data.csv", "at", encoding="utf-8", newline='')  # w(write), r(read), a(append), b(binary)
        fieldnames = ["code", "irum", "kor", "eng", "math", "total", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    dct = {}
    dct["code"] = input("학번 입력 => ")
    dct["irum"] = input("이름 입력 => ")
    dct["kor"] = int(input("국어 점수 입력 => "))
    dct["eng"] = int(input("영어 점수 입력 => "))
    dct["math"] = int(input("수학 점수 입력 => "))
    dct["total"] = dct["kor"] + dct["eng"] + dct["math"]
    dct["avg"] = float(dct["total"] / 3)

    if dct["avg"] >= 90:
      dct["grade"] = "수"
    elif dct["avg"] >= 80:
      dct["grade"] = "우"
    elif dct["avg"] >= 70:
      dct["grade"] = "미"
    elif dct["avg"] >= 60:
      dct["grade"] = "양"
    else:
      dct["grade"] = "가"

    wr.writerow(dct)

    fp.close()

    print("\n성적정보 입력 성공!!\n")

def print_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        total_avg = 0

        print("\n\t\t\t *** 성적관리 ***")
        print("===============================================")
        print("학번   이름   국어   영어   수학   총점   평균   등급")
        print("===============================================")

        for data in lst:
            print(f" {data['code']}   {data['irum']}"
                  f"   {data['kor']}    {data['eng']}    {data['math']}"
                  f"    {data['total']}   {data['avg']}    {data['grade']}")
            total_avg += float(data['avg'])
        print("===============================================")
        print(f"학생수 : {len(lst)}, 전체 평균 : {total_avg / len(lst)}")

        fp.close()

    else:
        print("\n출력할 학생 정보가 없음!!!")

def search_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        pr_code = input("조회할 학번을 입력하세요. => ")

        for data in lst:
            if data["code"] == pr_code:
              print("학번   이름   국어   영어   수학   총점   평균   등급")
              print("===============================================")
              print(f" {data['code']}   {data['irum']}"
                    f"   {data['kor']}    {data['eng']}    {data['math']}"
                    f"    {data['total']}    {data['avg']}    {data['grade']}")
              print("===============================================\n")
              break
        else:
            print("학번이 존재하지 않습니다.")

        fp.close()

    else:
        print("\n출력할 학생 정보가 없음!!!")

def update_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        pr_code = input("수정할 학번을 입력하세요. => ")

        for data in lst:
            if data["code"] == pr_code:
                data["kor"] = int(input("수정할 국어 점수를 입력하세요. => "))
                data["eng"] = int(input("수정할 영어 점수를 입력하세요. => "))
                data["math"] = int(input("수정할 수학 점수를 입력하세요. => "))
                data["total"] = int(data["kor"] + data["eng"] + data["math"])
                data["avg"] = float(data["total"] / 3)

                if data["avg"] >= 90:
                  data["grade"] = "수"
                elif data["avg"] >= 80:
                  data["grade"] = "우"
                elif data["avg"] >= 70:
                  data["grade"] = "미"
                elif data["avg"] >= 60:
                  data["grade"] = "양"
                else:
                  data["grade"] = "가"

                fp.close()

                fp = open("sungjuk_data.csv", "w", encoding="UTF-8", newline="")
                fieldnames = ["code", "irum", "kor", "eng", "math", "total", "avg", "grade"]
                wr = csv.DictWriter(fp, fieldnames=fieldnames)

                wr.writeheader()
                wr.writerows(lst)

                fp.close()

                print("\n수정이 완료되었습니다.\n")
                break
        else:
            print("학번이 존재하지 않습니다.")

    else:
        print("\n출력할 학생 정보가 없음!!!")

def delete_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv", "r", encoding="UTF-8")
        lst = list(csv.DictReader(fp))

        pr_code = input("삭제할 학번을 입력하세요. => ")

        for data in lst:
            if data["code"] == pr_code:
                lst.remove(data)

                fp.close()

                fp = open("sungjuk_data.csv", "w", encoding="UTF-8", newline="")
                fieldnames = ["code", "irum", "kor", "eng", "math", "total", "avg", "grade"]
                wr = csv.DictWriter(fp, fieldnames=fieldnames)

                wr.writeheader()
                wr.writerows(lst)

                fp.close()
                print("\n삭제가 완료되었습니다.\n")
                break
        else:
            print("학번이 존재하지 않습니다.")

    else:
        print("\n출력할 학생 정보가 없음!!!")

if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("메뉴를 선택하세요(1 ~ 6) => "))
        if menu == 1:
            input_sungjuk()
        elif menu == 2:
            print_sungjuk()
        elif menu == 3:
            search_sungjuk()
        elif menu == 4:
            update_sungjuk()
        elif menu == 5:
            delete_sungjuk()
        elif menu == 6:
            print("\n프로그램 종료!!")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")


