
def input_num():
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    return num1, num2

def min_max_num(num1, num2):
    if num1 > num2:
        min_num = num2
        max_num = num1
    else:
        min_num = num1
        max_num = num2

    return min_num, max_num

def print_cnt(finish=True):
    global cnt
    if not finish:
        cnt += 1
        if cnt % 10 == 0:  # 소수의 갯수가 10의 배수이면 줄바꿈 수행
            print()
    else:
        if cnt % 10 != 0:
            print()

        print("총소수의 갯수 = %d" % cnt)

def main(min_num, max_num):
    for i in range(min_num, max_num + 1):
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:  # 소수인 경우 수행
            print("%5d " % i, end="")
            print_cnt(False)  # 소수의 갯수 카운트

    print_cnt()

if __name__ == "__main__":
    min_num, max_num = input_num()
    min_num, max_num = min_max_num(min_num, max_num)
    cnt = 0
    main(min_num, max_num)







