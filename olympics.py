n, b, s, g = [int(x) for x in input().split()]
t = b + 3 * s + 5 * g
print(max(0, (n - t) // 5 + 1))
