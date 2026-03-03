import csv

f = open("output.csv", "w", encoding="UTF-8", newline="")
# quotechar = '"' : 데이터를 묶을 문자 지정
# csv.QUOTE_ALL : 모두 사용하겠다는 의미
wr = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL) # delimiter => 구분자, quotechar => ""로 묶음
wr.writerow((1, "김정수", False)) # writerow => 행단위로 출력
wr.writerow([2, "박상미", True])
f.close()