import sys
input = sys.stdin.readline
n = int(input())
arr = [int(x) for x in input().split()]
# let dp[i][0] be the longest next going down
# let dp[i][1] be the longest next going up
pD = [1, 1]
pV = [arr[0], arr[0]]
for i in range(1, n):
    cD = [pD[0], pD[1]]
    cV = [pV[0], pV[1]]
    if pV[0] > arr[i]:
        if pD[0] + 1 > cD[1]:
            cD[1] = pD[0] + 1
            cV[1] = arr[i]
        elif pD[0] + 1 == cD[1]:
            cV[1] = min(cV[1], arr[i])
    if pV[1] < arr[i]:
        if pD[1] + 1 > cD[0]:
            cD[0] = pD[1] + 1
            cV[0] = arr[i]
        elif pD[1] + 1 == cD[0]:
            cV[0] = max(cV[0], arr[i])
    cV, pV = pV, cV
    cD, pD = pD, cD
print(max(pD))
