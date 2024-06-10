a, b = map(int, input().split())

current = a

while current <= b:
    print(current, end=' ')
    if current % 2 == 1: 
        current *= 2
    else: 
        current += 3