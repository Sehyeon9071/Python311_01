from sungjuk_class import Sungjuk

lst = []

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
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    lst.append(obj)
    print("\n 성적 입력 성공!!!\n")

def print_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음!!\n")
        return
    else:
        print("\n\t\t\t *** 성적관리 ***")
        print("====================================================")
        print(" 학번    이름    국어   영어   수학   총점   평균    등급")
        print("====================================================")
        tot_avg = 0
        for obj in lst:
            obj.output_sungjuk()
            tot_avg += obj.avg
        print("====================================================")
        print(f"학생수 : {len(lst)}, 전체 평균 : {tot_avg / len(lst)}")

def search_sungjuk():
    hakbun = input("조회할 학번을 입력하세요. => ")

    for obj in lst:
        if obj.hakbun == hakbun:
            print(" 학번    이름    국어   영어   수학   총점   평균    등급")
            print("====================================================")
            obj.output_sungjuk()
            print("===============================================\n")
            break
    else:
        print("학번이 존재하지 않습니다.")
        return

def update_sungjuk():
    hakbun = input("수정할 학번을 입력하세요. => ")

    for obj in lst:
        if obj.hakbun == hakbun:
            obj.kor = int(input("수정할 국어 점수를 입력하세요. => "))
            obj.eng = int(input("수정할 영어 점수를 입력하세요. => "))
            obj.math = int(input("수정할 수학 점수를 입력하세요. => "))
            obj.tot = obj.kor + obj.eng + obj.math
            obj.avg = obj.tot / 3

            if obj.avg >= 90:
                obj.grade = "수"
            elif obj.avg >= 80:
                obj.grade = "우"
            elif obj.avg >= 70:
                obj.grade = "미"
            elif obj.avg >= 60:
                obj.grade = "양"
            else:
                obj.grade = "가"

            print("\n수정이 완료되었습니다.\n")
            break

    else:
        print("학번이 존재하지 않습니다.")
        return

def delete_sungjuk():
    hakbun = input("삭제할 학번을 입력하세요. => ")

    for obj in lst:
        if obj.hakbun == hakbun:
            lst.remove(obj)
            print("\n삭제가 완료되었습니다.\n")

    else:
        print("학번이 존재하지 않습니다.")
        return

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