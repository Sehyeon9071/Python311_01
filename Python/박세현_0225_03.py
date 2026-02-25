li = []
li.append(int(input("첫번째 숫자를 입력하시오. : ")))
li.append(int(input("두번째 숫자를 입력하시오. : ")))
li.sort()

f_num = li[0]
s_num = li[-1]

for i in range(f_num, s_num + 1):
    print(f" ** {i}단 ** ", end="    ")

for j in range (1, 10):
    print("")
    for k in range(li[0], li[-1] + 1):
        print(f"{k} * {j} = {k * j} ", end="    ")