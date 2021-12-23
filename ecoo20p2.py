import sys
input = sys.stdin.readline


for _ in range(int(input())):
    items = {}
    for _ in range(int(input())):
        for _ in range(int(input())):
            n, p, q = input().split()
            p = int(p)
            q = int(q)
            if n in items:
                items[n].append([p, q])
            else:
                items[n] = [[p, q]]
    total = 0
    for _ in range(int(input())):
        name, q = input().split()
        q = int(q)
        items[name].sort()
        for p, amount in items[name]:
            if q <= 0:
                break
            total += p * min(q, amount)
            q -= amount
    print(total)
