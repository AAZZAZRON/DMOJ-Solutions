n = int(input())
p = 1
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    p *= (b - a) / b
print(p)