sum=0
cnt=0
n=0
for i in range(n):
    n=int(input())
    sum += i
    cnt += 1
print(sum)
average = sum / cnt if cnt > 0 else 0

# 합과 평균을 출력합니다. 평균은 소수점 첫째자리까지 출력합니다.
print(sum, round(average, 1))