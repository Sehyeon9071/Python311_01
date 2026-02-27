a = int(input("첫번째 숫자를 입력하시오. : "))
b = int(input("첫번째 숫자를 입력하시오. : "))

li = []
prime_num = []

cnt = 0

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if a < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)
        cnt += 1

for i in range(0, len(prime_num), 10):
    li.append(prime_num[i:i+10])

for i in li:
    for j in i :
        print(f"{j}" ,end = " ")
    print()

print(f"소수의 개수 = {cnt}")

