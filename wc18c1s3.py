from sys import stdin
from sortedcontainers import SortedSet
input = stdin.readline


reach, jump, num = map(int, input().split())
itch = [False] * (2 * reach)
counter = 0
completed = False
for _ in range(num):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        itch[i] = True
dp = [1000001] * (2 * reach)
dp[0] = 0
drops = SortedSet()
for i in range(2 * reach):
    if 0 <= i - jump and not itch[i] and not itch[i - jump]:
        dp[i] = min(dp[i - jump] + 1, dp[drops[0] % (2 ** 25)] + 2)
    drops.add(dp[i] * 2 ** 25 + i)
    if len(drops) > jump:
        drops.discard(dp[i - jump] * 2 ** 25 + i - jump)
minimum = min(dp[reach:])
[print(minimum) if minimum < 1000000 else print(-1)]
