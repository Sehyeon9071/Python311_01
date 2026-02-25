std_DB = {
    '학번' : input("학번을 입력하시오. : "),
    '이름' : input("이름을 입력하시오. : "),
    '국어' : int(input("국어 성적을 입력하시오. : ")),
    '영어' : int(input("국어 성적을 입력하시오. : ")),
    '수학' : int(input("국어 성적을 입력하시오. : ")),
}

std_DB['총점'] = std_DB.get('국어') + std_DB.get('영어') + std_DB.get('수학')
std_DB['평균'] = std_DB.get('총점') / 3

if std_DB["평균"] >= 90:
    std_DB["등급"] = "수"
elif 80 <= std_DB["평균"] < 90:
    std_DB["등급"] = "우"
elif 70 <= std_DB["평균"] < 80:
    std_DB["등급"] = "미"
elif 60 <= std_DB["평균"] < 70:
    std_DB["등급"] = "양"
else:
    std_DB["등급"] = "가"

print("          *** 성적표 ***")
print("========================================")
print("학번  이름  국어  영어  수학  총점  평균  등급")
print("========================================")
print("%s %s %d %4d %5d %4d %4.2f %2s" %
      (std_DB['학번'], std_DB['이름'], std_DB['국어'], std_DB['영어'], std_DB['수학'], std_DB['총점'], std_DB['평균'], std_DB['등급']))
print("========================================")

## 교수님 코드

# dct={}
# dct['hakbun'] = input('학번 입력 => ')
# dct['irum'] = input('이름 입력 => ')
# dct['kor'] = int(input('극어 점수 입력 => '))
# dct['eng'] = int(input('영어 점수 입력 => '))
# dct['math'] = int(input('수학 점수 입력 => '))
#
# dct['tot'] = dct['kor'] + dct['eng'] + dct['math']
# dct['avg'] = dct['tot'] / 3
#
# 등급(수, 우, 미, 양, 가)
#
# if dct["avg"] >= 90:
#     dct["grade"] = "수"
# elif dct["avg"] >= 80:
#     dct["grade"] = "우"
# elif dct["avg"] >= 70:
#     dct["grade"] = "미"
# elif dct["avg"] >= 60:
#     dct["grade"] = "양"
# else:
#     dct["grade"] = "가"
#
# print('\n\t\t\t *** 성적표 ***')
# print("========================================")
# print("학번  이름  국어  영어  수학  총점  평균  등급")
# print("========================================")
# print("%4s %3s %4d  %4d  %4d  %4d  %5.2f  %2s" %
#       (dct['hakbun'], dct['irum'], dct['kor'],dct['eng'], dct['math'], dct['tot'],dct['avg'],dct['grade']))
# print("===================================")
