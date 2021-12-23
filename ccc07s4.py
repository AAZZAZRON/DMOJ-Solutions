from sys import stdin
input = stdin.readline


numbers = int(input())
routes = {x: [] for x in range(1, numbers + 1)}
while True:
    possible = [int(x) for x in input().split()]
    if possible == [0, 0]:
        break
    routes[possible[1]].append(possible[0])
slide = [0] * numbers + [1]
for i in range(numbers, 0, -1):
    for num in routes[i]:
        slide[num] += slide[i]
print(slide[1])
