f_num = int(input("첫번째 숫자를 입력하시오. : "))
s_num = int(input("두번째 숫자를 입력하시오. : "))
min_num = None
max_num = None

if f_num > s_num:
    max_num = f_num
    min_num = s_num
else:
    max_num = s_num
    min_num = f_num

for i in range(min_num, max_num + 1):
    print(f"\n ** {i}단 **")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")