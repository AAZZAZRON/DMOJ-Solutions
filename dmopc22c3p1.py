n, m = [int(x) for x in input().split()]
if n * m % 2 == 0:
    print(n * m // 2, n * m // 2)
else:
    ans = max(n // 2 * m, m // 2 * n)
    print(n * m - ans, ans)
