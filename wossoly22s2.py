n = int(input())
print(*[x for x in range(1, n + 1)][::-1])
print(1, *[x for x in range(3, n + 1)], 2 if n != 1 else "")
