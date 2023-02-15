import sys
input = sys.stdin.readline
freq = [0] * 65537
arr = []
while True:
    tmp = int(input())
    if tmp == 0:
        break
    arr.append(tmp)
l = 0
ind = 0
m = 0
for r in range(len(arr)):
    v = arr[r]
    freq[v] += 1
    while freq[v] > 1:
        freq[arr[l]] -= 1
        l += 1
    if r - l + 1 > m:
        m = r - l + 1
        ind = l
    # print(l, ind, m)

for i in range(ind, ind + m):
    print(arr[i])
