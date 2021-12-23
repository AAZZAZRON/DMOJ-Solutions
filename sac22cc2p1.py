n, q = [int(x) for x in input().split()]
checks = []
for i in range(n):
    a, b = input().split()
    checks.append([int(a), b])
curr = 0
for _ in range(q):
    a = int(input())
    for i in checks:
        if curr < i[0] <= a:
            print(i[1])
    curr = a
