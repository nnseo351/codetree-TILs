# 짝수 횟수를 세는 변수 초기화
even_count = 0

# 5개의 숫자를 입력받고 처리합니다.
for _ in range(5):
    num = int(input())
    # 짝수인 경우 even_count 증가
    if num % 2 == 0:
        even_count += 1

# 결과 출력
print(even_count)