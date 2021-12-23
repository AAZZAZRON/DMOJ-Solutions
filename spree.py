from sys import stdin
input = stdin.readline


num, hours = [int(x) for x in input().split()]
problems = [[int(x) for x in input().split()] for i in range(num)]
prev = [0] * (hours + 1)
dp = [0]
for i in range(1, num + 1):
    points, minutes = problems[i - 1]
    for j in range(1, hours + 1):
        if minutes > j:
            dp.append(prev[j])
        else:
            dp.append(max(prev[j], prev[j - minutes] + points))
    prev = dp.copy()
    # print(dp)
    dp = [0]
print(prev[-1])
