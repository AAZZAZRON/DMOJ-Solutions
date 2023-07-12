arr = sorted([[int(x) for x in input().split()] for _ in range(int(input()))])

s = 0.0
for i in range(1, len(arr)):
    s = max(s, abs((arr[i][1] - arr[i - 1][1]) / (arr[i][0] - arr[i - 1][0])))
print(s)
