from sys import stdin
input = stdin.readline


num = int(input())
problems = [0] * 1000001
maximum = 0
for i in range(num):
    x, y = [int(x) for x in input().split()]
    problems[x] = max(problems[x], y)
psa = [0]
for i in range(1000001):
    if problems[i] != 0:
        maximum = max(i, maximum)
        x = [psa[-1]] * (i - len(psa))
        psa.extend(x)
        psa.append(max(psa[-1], problems[i]))
# print(psa)
for i in range(int(input())):
    x = min(int(input()), maximum)
    print(psa[x])
