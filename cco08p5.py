from sys import stdin
input = stdin.readline


num = int(input())
items = []
total = 0
for _ in range(num):
    quantity, val = [int(x) for x in input().split()]
    items.append([quantity, val])
    total += quantity * val

half = total // 2
dp = [False] * (half + 1)
dp[0] = True
maximum = 0
for q, item in items:
    for j in range(0, item):
        counter = q + 1
        while j <= half:
            if dp[j]:
                counter = 0
            else:
                if counter < q:
                    dp[j] = True
                    counter += 1
                    maximum = max(maximum, j)
            j += item
    # print(dp)
print(total - maximum * 2)
