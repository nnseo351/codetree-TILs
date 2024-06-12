n=int(input())
sum=0

for i in range(n):
    if n%2==0 and n%3==0:
        sum += i
print(sum)