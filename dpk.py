num, k = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
dp = [0] * (k + 1)
# 1 = whoever gets this loses
# 2 = whoever gets this wins
for i in range(k + 1):
    for n in numbers:
        if i - n >= 0 and not dp[i - n]:
            dp[i] = 1
            break

# print(dp)
if dp[k] == 1:
    print("First")
else:
    print("Second")
