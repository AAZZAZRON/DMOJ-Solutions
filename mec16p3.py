from sys import stdin
input = stdin.readline


num, time = [int(x) for x in input().split()]
items = []
for i in range(num):
    psa = [[0, 0]]
    x, *skill = [int(x) for x in input().split()]
    for q in range(0, x * 2, 2):
        psa.append([psa[-1][0] + skill[q], psa[-1][1] + skill[q + 1]])
    items.append(psa)
# print(items)
dp = [0] * (time + 1)
for i in range(num):
    psa = items[i]
    countdown = psa[-1][0]
    for j in range(time, 0, -1):
        if psa == [[0, 0]]:
            break
        elif j < countdown:
            while j < countdown:
                psa.pop()
                countdown = psa[-1][0]
        dp[j] = max([dp[j - x] + y for x, y in psa])
    # print(dp)
print(dp[-1])
