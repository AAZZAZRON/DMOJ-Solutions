n = int(input())
days = [int(x) for x in input().split()]
ans = 0
for k in range(2, 25):
    ct = 0
    for day in days:
        ct += day - (day % k)
    ans = max(ans, ct)
print(ans)