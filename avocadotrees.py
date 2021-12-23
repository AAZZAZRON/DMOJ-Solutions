import sys
input = sys.stdin.readline


trees, ranges, height = [int(x) for x in input().split()]
theRanch = [0]
count = 0
for i in range(trees):
    x = [int(x) for x in input().split()]
    if x[0] <= height:
        count += x[1]
    theRanch.append(count)
maximum = 0

for j in range(ranges):
    start, end = [int(x) for x in input().split()]
    count = theRanch[end] - theRanch[start - 1]
    if maximum < count:
        maximum = count
print(maximum)
