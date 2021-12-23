from sys import stdin
input = stdin.readline


num = int(input())
tint = int(input())
sweep = [[-100000000000]]
line = {-1000000000000}
for _ in range(num):
    x1, y1, x2, y2, t = [int(x) for x in input().split()]
    sweep.append([x1, y1, y2, t])
    sweep.append([x2, y1, y2, -t])
    line.add(y1)
    line.add(y2)
sweep.sort()
line = list(line)
line.sort()
hash = {}
for i in range(1, len(line)):
    hash[line[i]] = i
# print(sweep)
# print(line)
counter = 0
track = [0] * (len(line) + 1)
for i in range(1, len(sweep)):
    for j in range(1, len(line)):
        if track[j] >= tint:
            counter += (line[j + 1] - line[j]) * (sweep[i][0] - sweep[i - 1][0])
    for j in range(hash[sweep[i][1]], hash[sweep[i][2]]):
        track[j] += sweep[i][3]
    # print(track)
print(counter)
