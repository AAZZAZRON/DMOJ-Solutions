import sys
input = sys.stdin.readline


n, k = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]
count = [0] * 1000001
distinct = 0
right = 0
total = 0
for left in range(n - k + 1):
    while right < n and distinct < k:
        count[values[right]] += 1
        if count[values[right]] == 1:
            distinct += 1
        right += 1
    if distinct >= k:
        total += n - right + 1
    count[values[left]] -= 1
    if count[values[left]] == 0:
        distinct -= 1
print(total)
