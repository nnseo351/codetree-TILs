# 첫 번째 줄에서 정수 n을 입력받습니다.
n = int(input())

# 각 청소 횟수를 세는 변수 초기화
classroom_cleaning_count = 0
hallway_cleaning_count = 0
bathroom_cleaning_count = 0

# 1일부터 n일까지 각 날을 확인
for day in range(1, n + 1):
    if day % 12 == 0:
        bathroom_cleaning_count += 1
    elif day % 3 == 0:
        hallway_cleaning_count += 1
    elif day % 2 == 0:
        classroom_cleaning_count += 1

# 결과 출력
print(classroom_cleaning_count, hallway_cleaning_count, bathroom_cleaning_count)