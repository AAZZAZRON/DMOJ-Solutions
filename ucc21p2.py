num = int(input())
numbers = [int(x) for x in input().split()]
maximum = 0
current = 0
for i in numbers:
    if i % 2 == 0:
        current += i
    else:
        maximum = max(maximum, current)
        current = 0
maximum = max(maximum, current)
print(maximum)
