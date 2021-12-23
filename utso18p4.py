from sys import stdin
input = stdin.readline

possible = {}
for _ in range(int(input())):
    k, m = [int(x) for x in input().split()]
    if k + m not in possible:
        possible[k + m] = []
    possible[k + m].append([k, m])
maximum = 0
for i in possible:
    possible[i].sort()
    smallMax = 0
    keyboard, monitor = 0, 0
    for j, k in possible[i]:
        keyboard += k
    for j, k in possible[i][::-1]:
        keyboard -= k
        monitor += j
        smallMax = max(smallMax, min(keyboard, monitor))
    maximum = max(maximum, smallMax)
print(maximum)
