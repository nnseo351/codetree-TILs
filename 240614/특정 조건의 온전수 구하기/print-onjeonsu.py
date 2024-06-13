n=int(input())
for i in range(1, n+1):
    if i%2==0 and (i%5==0 and i%20==0) and (i%3==0 and i%9!=0):
        continue

print(i)