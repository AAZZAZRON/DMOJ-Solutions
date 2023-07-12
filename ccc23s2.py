import sys
input = sys.stdin.readline
n = int(input())
arr = [int(x) for x in input().split()]
ans = [float('inf')] * (n + 1)
ans[1] = 0

for i in range(n):
    ct = 0
    j = 1
    while i - j >= 0 and i + j < n:
        ct += abs(arr[i - j] - arr[i + j])
        ans[j * 2 + 1] = min(ans[j * 2 + 1], ct)
        j += 1
for i in range(n):
    ct = 0
    j = 0
    while i - j >= 0 and i + j + 1 < n:
        ct += abs(arr[i - j] - arr[i + j + 1])
        j += 1
        ans[j * 2] = min(ans[j * 2], ct)
print(*ans[1:])