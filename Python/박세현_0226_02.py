stds = []
grade = 0

while True:
    std = []
    hakbun = input("학번을 입력하세요. : ")
    if hakbun == "exit":
        break

    name = input("이름을 입력하시오. : ")
    std.append([hakbun, name])

    kor = int(input("국어 점수를 입력하시오. : "))
    eng = int(input("영어 점수를 입력하시오. : "))
    math = int(input("수학 점수를 입력하시오. : "))
    std.append([kor, eng, math])

    total = sum(std[1])
    avg = total / len(std[1])
    grade += avg
    std.append([total, avg])
    stds.append(std)

if len(stds) > 0:
    print("              *** 성적표 ***")
    print("========================================")
    print("학번   이름   국어   영어   수학   총점   평균")
    print("========================================")

    for i in stds:
        print(f"{i[0][0]}  {i[0][1]}  {i[1][0]}    {i[1][1]}    {i[1][2]}    {i[2][0]}    {i[2][1]}")

    print("========================================")
    print(f"      학생수 : {len(stds)}      전체 평균 : {round(grade / len(stds), 2)}")

