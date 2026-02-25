total = 0

for item in range(1, 101, 1):
    if item == 10:
        break
    total += item
else:
    print(f"1부터 100까지의 합은 {total}입니다.")