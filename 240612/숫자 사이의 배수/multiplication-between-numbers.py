a, b = map(int, input().split())
sum_val1 = 0
sum_val2=0
cnt1=0
cnt2=0

for i in range(a,b+1):
    if i % 5 ==0 : 
        sum_val1 += i
        cnt1 += 1

    if i % 7 == 0:
        sum_val2 += i
        cnt2 += 1

sum=sum_val1+sum_val2
cnts=cnt1+cnt2
print(sum,(round(sum/cnts,1)))