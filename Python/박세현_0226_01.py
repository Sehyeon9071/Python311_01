stds = []
total = 0

while True:
    hakbun = input("학번을 입력하시오. : ")
    if hakbun.lower() == "exit":
        break

    std = {
        "info" : {
            "학번" : hakbun,
            "이름" : input("이름을 입력하시오. : ")
        },
        "score" : {
            "국어" : int(input("국어 점수를 입력하시오. : ")),
            "영어": int(input("영어 점수를 입력하시오. : ")),
            "수학": int(input("수학 점수를 입력하시오. : "))
        },
        "grade" : {

        }
    }

    std["grade"]["총점"] = sum(std["score"].values())
    std["grade"]["평균"] = std["grade"]["총점"] / len(std["score"])
    total += std["grade"]["평균"]
    stds.append(std)

if len(stds) > 0:
    print("              *** 성적표 ***")
    print("========================================")
    print("학번   이름   국어   영어   수학   총점   평균")
    print("========================================")

    for i in stds:
        print(f"{i['info']['학번']}  {i['info']['이름']}"
            f"  {i['score']['국어']}    {i['score']['영어']}    {i['score']['수학']}"
            f"    {i['grade']['총점']}    {i['grade']['평균']}")

    print("========================================")
    print(f"      학생수 : {len(stds)}      전체 평균 : {round(total / len(stds), 2)}")

else:
    print("학생 정보가 없습니다.")