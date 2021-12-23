import sys
input = sys.stdin.readline


def updateBIT(ind, val):
    while ind <= 1000000:
        BIT[ind] = max(BIT[ind], val)
        ind += ind & (-ind)


def maximum(ind):
    m = 0
    while ind > 0:
        m = max(m, BIT[ind])
        ind -= ind & (-ind)
    return m


lenA = int(input())
one = [int(x) for x in input().split()]
lenB = int(input())
two = [int(x) for x in input().split()]
indexes = [-1] * 1000001
BIT = [0] * 1000001
for i in range(1, lenB + 1):
    indexes[two[i - 1]] = i

# let dp[i] be the longest common subsequence ending at i
for i in range(1, lenA + 1):
    if indexes[one[i - 1]] != -1:
        updateBIT(indexes[one[i - 1]], maximum(indexes[one[i - 1]]) + 1)
print(maximum(lenB))
