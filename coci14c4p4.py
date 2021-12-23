from sys import stdin
input = stdin.readline


def isEnough(node, liquid):
    if need[node] != -1 and liquid < need[node]:
        return False
    elif need[node] == -1:
        for go, percent, superPipe in adj[node]:
            total = liquid * (percent / 100)
            if superPipe == 1:
                total *= total
            if not isEnough(go, total):
                return False
    return True


holes = int(input())
adj = [[] for _ in range(holes + 1)]
for _ in range(holes - 1):
    one, two, perc, isSuper = [int(x) for x in input().split()]
    adj[one].append([two, perc, isSuper])
need = [0] + [int(x) for x in input().split()]
high = 2000000000
low = 0
while high - low > 0.00001:
    mid = (low + high) / 2
    if isEnough(1, mid):
        high = mid
    else:
        low = mid
print("{0:.3f}".format(high))
