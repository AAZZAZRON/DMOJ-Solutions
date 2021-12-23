from sys import stdin
input = stdin.readline


num, amount, questions = [int(x) for x in input().split()]
cubes = [int(x) for x in input().split()]
indexes = [-1] * (max(cubes) + 1)
psa = []
add = 0
for i in range(num):
    add += float(cubes[i]) / 2
    psa.append(add)
    indexes[cubes[i]] = i
psa.append(0)
for i in range(questions):
    start, end = [int(x) for x in input().split()]
    one = indexes[start]
    two = indexes[end]
    if psa[two] - psa[one - 1] >= amount:
        print("Enough")
    else:
        print("Not enough")
