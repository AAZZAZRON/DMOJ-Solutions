import sys
input = sys.stdin.readline

def cost(ch, num):
    return ch[0] * num + ch[1]


n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(n)]
arr.sort(reverse=True)
prev = [0] * (n + 1)
dp = None
# print(arr)
for i in range(m):
    dp = [float('inf')] * (n + 1)
    for j in range(1, n + 1):
        dp[j] = min(dp[j - 1], prev[j - 1] + cost(arr[j - 1], i))
    # print(dp)
    prev, dp = dp, prev
print(prev[n])
