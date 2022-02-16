q, w = [int(x) for x in input().split()]
a, b, c, d = [int(x) for x in input().split()]
print("Yes" if (a <= q <= c and b <= w <= d) else "No")