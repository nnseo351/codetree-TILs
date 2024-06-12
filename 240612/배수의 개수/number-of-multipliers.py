# 3의 배수와 5의 배수를 세는 변수 초기화
count_3 = 0
count_5 = 0

# 10개의 숫자를 입력받고 처리합니다.
for _ in range(10):
    num = int(input())
    # 3의 배수인 경우 count_3 증가
    if num % 3 == 0:
        count_3 += 1
    # 5의 배수인 경우 count_5 증가
    if num % 5 == 0:
        count_5 += 1

# 결과 출력
print(count_3, count_5)