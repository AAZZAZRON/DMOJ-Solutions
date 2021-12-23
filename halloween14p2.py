from sys import stdin
from bisect import bisect_left
input = stdin.readline


num, field = [int(x) for x in input().split()]
cuteness = [0]
size = [0]
maximums = [0]
for _ in range(num):
    line = input().split()
    if line[0] == "A":
        # insert new numbers
        w, c = int(line[1]), int(line[2])
        cuteness.append(cuteness[-1] + c)
        size.append(size[-1] + w)

        # calculate "new" cuteness
        need = size[-1] - field
        index = bisect_left(size, need)
        maximums.append(max(maximums[-1], cuteness[-1] - cuteness[index]))

        print(maximums[-1])
    elif line[0] == "D":
        # remove last numbers
        cuteness.pop()
        size.pop()
        maximums.pop()
