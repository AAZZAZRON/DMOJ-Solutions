n = int(input())
curr = 3
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    if a == curr:
        curr = b
    elif b == curr:
        curr = a
print(curr)
