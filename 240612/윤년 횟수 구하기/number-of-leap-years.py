# 첫 번째 줄에서 정수 n을 입력받습니다.
n = int(input())

# 윤년 횟수를 세는 변수 초기화
leap_year_count = 0

# 1년부터 n년까지 각 해를 확인
for year in range(1, n + 1):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap_year_count += 1

# 결과 출력
print(leap_year_count)