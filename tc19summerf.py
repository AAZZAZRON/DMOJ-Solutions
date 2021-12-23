from math import sqrt
start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]
print(max(abs(start[0] - end[0]), abs(start[1] - end[1]), abs(start[2] - end[2])))
print(int(sqrt(float(start[0] - end[0]) ** 2 + float(start[1] - end[1]) ** 2 + float(start[2] - end[2]) ** 2)))
print(abs(start[0] - end[0]) + abs(start[1] - end[1]) + abs(start[2] - end[2]))

