import sys
input = sys.stdin.readline


numDays = int(input())
storage = [0, 0, 0]
for i in range(1, numDays + 1):
    days = [int(x) for x in input().split()]
    days[0] += max(storage[1], storage[2])
    days[1] += max(storage[0], storage[2])
    days[2] += max(storage[1], storage[0])
    storage = days
print(max(storage))
