from collections import defaultdict

n = int(input())
arr = sorted([int(x) for x in input().split()])

'''# create
tmp = []
for i in range(n):
    for j in range(n):
        tmp.append(arr[i] + arr[j])
tmp.sort()
arr = tmp

print(arr)'''

f = defaultdict(int)
for i in arr:
    f[i] += 1
ans = []
for key in f.keys():
    if f[key] % 2 == 1:
        ans.append(key // 2)
print(*ans)