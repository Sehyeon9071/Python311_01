# random 모듈 : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈.

# random() 함수 : 0부터 1사이의 랜덤 실수를 반환한다.
# uniform() 함수 : 2개의 숫자 사이의 랜덤 실수를 반환한다.
# randint() 함수 : 2개의 숫자 사이의 랜덤 정수를 반환한다.
#                 (2번째 인자로 넘어온 변수도 범위에 포함시킴)
# choice() 함수 : 랜덤하게 하나의 원소를 선택한다.
# sample() 함수 : 랜덤하게 여러 개의 원소를 선택한다.
# shuffle() 함수 : 원소의 순서를 랜덤하게 변경한다.

import random

print(random.random()) # 0과 1사이 난수 생성
print("--------------------")
print(random.uniform(1, 10)) # 1과 10사이의 난수 생성
print("--------------------")
print(random.randint(1, 10)) # 1부터 10사이의 정수형 난수 반환
print("--------------------")
print(random.randrange(0, 100, 2)) # 0부터 100사이 짝수중(2증가) 하나 선택
print("--------------------")
print(random.choice("abcdefghij"))
print("--------------------")
print(random.sample([1, 2, 3, 4, 5], 3))
print("--------------------")
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items)