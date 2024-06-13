# 입력 받기
n = int(input())

# 1부터 n까지 반복
for i in range(1, n + 1):
    # 조건에 해당하면 continue
    if i % 2 == 0:
        continue
    if i % 10 == 5:
        continue
    if i % 3 == 0 and i % 9 != 0:
        continue
    
    # 조건에 해당하지 않으면 출력
    print(i, end=' ')