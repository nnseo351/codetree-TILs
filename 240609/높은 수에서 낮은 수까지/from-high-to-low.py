a, b = map(int, input().split())

if a>=b:
    for i in range(a,b+1):
      print(i,end=" ")
elif a<b:
     for n in range(b,a-1,-1):
       print(n,end=" ")