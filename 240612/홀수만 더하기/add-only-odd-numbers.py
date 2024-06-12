# 변수 선언, 입력
n = int(input())
sum_val = 0

for _ in range(n):
    a = int(input())
    if a % 2 == 1 and a % 3 == 0:
        sum_val += a

# 출력
print(sum_val)