# 내 코드

li = []

code = input("제품코드 입력 => ")
irum = input("제품명 입력 => ")
su = int(input("수량 입력 => "))
price = int(input("단가 입력 => "))

kumack = su * price

li.append(code)
li.append(irum)
li.append(su)
li.append(price)

print("\n제품코드    제품명    수량    단가    판매금액")
print("==========================================")

i = 0
while i < len(li):
    if len(li) % 5 == 0 :
        print("\n")

    else :
        print("%4s    %4s    %4d    %4d    %6d" % (code, irum, su, price, kumack))
        i += 1

print("==========================================")


## 교수님 코드

# lst = []
# lst.append(input("제품코드 입력 => "))
# lst.append(input("제품명 입력 => "))
# lst.append(input("제품수량 입력 => "))
# lst.append(input("제품단가 입력 => "))
# lst.append(lst[2] * lst[3])
#
# print("\n제품코드    제품명    수량    단가    판매금액")
# print("==========================================")
# print("%4s    %4s    %4d    %4d    %6d" % (lst[0], lst[1], lst[2], lst[3], lst[4]))
# print("==========================================")

## 근데 반복문 사용해서 프로그램 하나 만들라 하시지 않았나...