dic = {
    "학번" : input("학번을 입력하시오. : "),
    "이름" : input("이름을 입력하시오. : "),
    "국어" : int(input("국어 점수를 입력하시오. : ")),
    "영어" : int(input("영어 점수를 입력하시오. : ")),
    "수학" : int(input("수학 점수를 입력하시오. : "))
}

kor = dic.get("국어")
eng = dic.get("영어")
math = dic.get("수학")
total = kor + eng + math
avg = total / 3

dic["총점"] = total
dic["평균"] = avg

print(dic)
