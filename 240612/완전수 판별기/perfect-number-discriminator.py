sum=0
n=int(input())
for i in range(1, n):
    if n%i==0:
        sum += i
if n==sum:
    print("P")
else:
    print("N")