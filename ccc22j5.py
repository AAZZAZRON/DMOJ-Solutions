n = int(input())
trees = [[int(x) for x in input().split()] for _ in range(int(input()))]
trees.append([0, 0])
tX = [x[0] for x in trees]
tY = [x[1] for x in trees]
ans = 0
for x in tX:
    for y in tY:
        s = min(n - y, n - x)
        for a, b in trees:
            if x < a and y < b:
                s = min(s, max(a - x, b - y) - 1)
        ans = max(ans, s)
print(ans)
