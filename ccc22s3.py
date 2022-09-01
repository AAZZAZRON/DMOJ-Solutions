import sys
input = sys.stdin.readline

n, m, k = [int(x) for x in input().split()]

arr = [1] * n
tot = n
if n > k:
    print(-1)
    sys.exit()
for i in range(n):
    if tot == k:
        arr[i] = arr[i - 1]
    elif i < m and tot + i <= k:
        arr[i] = i + 1
        tot += i
    elif tot + m - 1 <= k:
        arr[i] = arr[i - m]
        tot += m - 1
    else:
        arr[i] = arr[i - (k - tot) - 1]
        tot = k

if tot == k:
    print(*arr)
else:
    print(-1)
