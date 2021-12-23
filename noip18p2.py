import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    found = set()
    arr.sort()
    dp = [0] * 25001
    for i in arr:
        dp[i] = 1
    for i in range(25001):
        if dp[i]:
            for j in arr:
                if i + j <= 25000:
                    if dp[i + j] and i + j in arr and i + j not in found:
                        n -= 1
                    dp[i + j] = 1
    print(n)
