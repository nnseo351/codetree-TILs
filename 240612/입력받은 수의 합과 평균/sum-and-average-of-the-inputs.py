sum = 0
cnt = 0
n = int(input())

for i in range(n):
    z = int(input())
    if 1 <= z <= 1000:
        sum += z  # 각 정수를 더합니다.
        cnt += 1  # 입력된 정수의 개수를 증가시킵니다.

print(sum, round(sum / cnt, 1))  # 합계와 평균을 출력합니다.