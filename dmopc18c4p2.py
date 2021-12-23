num = int(input())
tasks = [int(x) for x in input().split()]
total = sum(tasks)

half = round(total / 2)
prev = [0] * (half + 1)
dp = [0] * (half + 1)

for i in range(1, num + 1):
    task = tasks[i - 1]
    for j in range(1, half + 1):
        if j < task:
            dp[j] = prev[j]
        else:
            dp[j] = max(prev[j], prev[j - task] + task)
    # print(dp)
    prev, dp = dp, prev

print(abs(total - prev[-1] * 2))
