import sys
input = sys.stdin.readline


# discard of the soups that die of freshness before temperature
# sort soups based on time to be cold, then sorted by freshness
x, n = [int(x) for x in input().split()]
soups = [[] for _ in range(500001)]
for i in range(n):
    t, f = [int(x) for x in input().split()]
    t = max(0, t - x)
    soups[t].append(f)
total = 0
additional = 0
for i in range(500001):
    if not soups[i] and additional != 0:
        additional -= 1
    soups[i].sort()
    for fresh in soups[i]:
        found = 0
        if fresh - (i - additional) >= 0:
            if found:
                additional += 1
            total += 1
            found = 1
print(total)
