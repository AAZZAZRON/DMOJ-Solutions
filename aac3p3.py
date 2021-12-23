import sys
input = sys.stdin.readline


n = int(input())
stocks = sorted([int(x) for x in input().split()])
left, right = 0, n - 1
new = []
while left < right:
    new.append(stocks[left])
    new.append(stocks[right])
    left += 1
    right -= 1
if left == right:
    new.append(stocks[left])
print(" ".join([str(x) for x in new]))
print("BS" * (n // 2), end="")
if left == right:
    print("E")
else:
    print()
