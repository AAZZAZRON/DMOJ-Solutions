n, m = [int(x) for x in input().split()]
queens = [[int(x) for x in input().split()] for _ in range(m)]
c = n * n
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for x, y in queens:
            if i == x or j == y or abs(i - x) == abs(j - y):
                c -= 1
                break
print(c)
