one = input()
two = input()
oneL = len(one)
twoL = len(two)
dp = [[0] * (twoL + 1) for _ in range(oneL + 1)]
for i in range(1, oneL + 1):
    for j in range(1, twoL + 1):
        if one[i - 1] == two[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
word = ""
i = oneL
j = twoL
while i > 0 and j > 0:
    if one[i - 1] == two[j - 1]:
        word += one[i - 1]
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(word[::-1])
