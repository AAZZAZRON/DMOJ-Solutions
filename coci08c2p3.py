def rec(p, s, i):
    global ans, n
    for j in range(i, n):
        rec(p * v[j][0], s + v[j][1], j + 1)
    if i != 0:
        ans = min(ans, abs(p - s))


n = int(input())
v = [[int(x) for x in input().split()] for _ in range(n)]
ans = 10000000000
rec(1, 0, 0)

print(ans)
