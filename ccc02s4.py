from sys import stdin
input = stdin.readline


capacity = int(input())
num = int(input())
people = [[input()[:-1], int(input())] for _ in range(num)]

dp = [999999] * (num + 1)
dp[0] = 0
groups = [-1] * (num + 1)

for i in range(num):
    maximum = 0
    for j in range(capacity):
        if i + j < num:
            maximum = max(maximum, people[i + j][1])
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + maximum)
            if dp[i + j + 1] == dp[i] + maximum:
                groups[i + j + 1] = j + 1

print(f"Total Time: {dp[-1]}")
printOut = []
x = num
while x > 0:
    y = groups[x]
    printOut.append(" ".join([x[0] for x in people[x - y: x]]))
    x -= y
[print(x) for x in printOut[::-1]]
