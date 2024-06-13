# 입력 받기
n = int(input())

# 친근하지 않은 수의 개수를 세기 위한 변수 초기화
count = 0

# 1부터 n까지 반복
for i in range(1, n + 1):
    # 숫자가 2, 3, 5 중 하나로 나누어 떨어지면 continue
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    # 친근하지 않은 수인 경우 count 증가
    count += 1

# 결과 출력
print(count)