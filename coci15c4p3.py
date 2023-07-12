n = int(input())
arr = [[int(x) for x in input().split()] for _ in range(n)]
ans = [0] * n
for i in range(n):
    tmp = 0
    for x in arr[i]:
        tmp |= x
    ans[i] = tmp
print(*ans)
