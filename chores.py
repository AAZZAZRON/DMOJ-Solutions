import sys
input = sys.stdin.readline


numTasks = int(input())
tasks = sorted([[int(x) for x in input().split()] for i in range(numTasks)])
count, last = 0, 0
for time, amount in tasks:
    count += (last * amount) + (time * (amount * (amount + 1) // 2))
    last += time * amount
print(count % 1000000007)
