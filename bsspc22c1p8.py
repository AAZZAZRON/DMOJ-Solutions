import sys
input = lambda: sys.stdin.readline()[:-1]

d = {"R": 0, "G": 1, "B": 2}

n = int(input())
start = [d[x] for x in input()]
end = [d[x] for x in input()]
dd = [(end[i] - start[i]) % 3 for i in range(n)] + [0]
diff = [0] * (n + 1)
diff[0] = dd[0]
for i in range(1, n + 1):
    diff[i] = (dd[i] - dd[i - 1]) % 3
ct = diff.count(0)
if ct == n + 1:
    print(0)
    sys.exit()
for i in range(int(input())):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if diff[a] == 0:
        ct -= 1
    if diff[b + 1] == 0:
        ct -= 1
    diff[a] = (diff[a] - 1) % 3
    diff[b + 1] = (diff[b + 1] + 1) % 3
    if diff[a] == 0:
        ct += 1
    if diff[b + 1] == 0:
        ct += 1
    if ct == n + 1:
        print(i + 1)
        sys.exit()
print(-1)