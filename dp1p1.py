'''''''''
num = int(input())
numbers = [int(input()) for _ in range(num)]
incl, excl = 0, 0
for i in numbers:
    new = max(incl, excl)
    incl = excl + i
    excl = new
    # print(incl, excl)
print(max(incl, excl))
'''''''''

num = int(input())
dp = [int(input()) for _ in range(num)] + [0, 0]
for i in range(num):
    dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])
print(dp[-3])
