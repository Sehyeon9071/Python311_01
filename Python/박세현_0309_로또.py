# [문제] 1부터 45사이의 숫자를 사용하여 로또 번호 6개를 출력하는 프로그램을 작성하시오.
# 단, 중복되는 값을 허용하지 않는다.
# 제출파일명 : 박세현_0309_로또.py

import random

lst = []

while True:
    num = random.randint(1, 45)

    if num in lst:
        continue
    elif len(lst) == 6:
        break
    else:
        lst.append(num)

print(sorted(lst))
