import sys
input = sys.stdin.readline


n, q = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
maxL = [0] * (n + 2)
maxR = [0] * (n + 2)
freqL = [1] * (n + 2)
freqR = [1] * (n + 2)
for i in range(n):
    maxL[i + 1] = max(arr[i], maxL[i])
    freqL[i + 1] = freqL[i]
    if arr[i] == maxL[i]:
        freqL[i + 1] += 1
    elif arr[i] == maxL[i + 1]:
        freqL[i + 1] = 1

maxR[n] = arr[n - 1]
for i in range(n - 2, -1, -1):
    maxR[i + 1] = max(arr[i], maxR[i + 2])
    freqR[i + 1] = freqR[i + 2]
    if arr[i] == maxR[i + 2]:
        freqR[i + 1] += 1
    elif arr[i] == maxR[i + 1]:
        freqR[i + 1] = 1
# print(maxL)
# print(freqL)
# print(maxR)
# print(freqR)

for _ in range(q):
    l, r = [int(x) for x in input().split()]
    l -= 1
    r += 1
    if maxL[l] == maxR[r]:
        print(maxL[l], freqL[l] + freqR[r])
    elif maxL[l] > maxR[r]:
        print(maxL[l], freqL[l])
    else:
        print(maxR[r], freqR[r])
