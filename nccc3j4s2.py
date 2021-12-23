import sys
input = sys.stdin.readline


num = int(input())
median = []
for i in range(num):
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    median.append(numbers[num // 2])
median.sort()
print(median[num // 2])
