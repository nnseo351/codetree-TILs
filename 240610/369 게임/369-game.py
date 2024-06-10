n = int(input())

for i in range(1, n + 1):
    # 숫자를 문자열로 변환하여 '3', '6', '9' 중 하나가 포함되어 있는지 확인
    if '3' in str(i) or '6' in str(i) or '9' in str(i) or i % 3 == 0:
        print(0, end=" ")
    else:
        print(i, end=" ")