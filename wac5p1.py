import sys
input = sys.stdin.readline

n = int(input())
acorns = [int(x) for x in input().split()]
acorns.sort()
i = 0
while i < n:
    j = i - 1
    while j >= 0:
        if acorns[j] < acorns[i]:
            acorns.pop(j)
            n -= 1
            break
        j -= 1
    if j < 0:
        i += 1
print(sum(acorns))
