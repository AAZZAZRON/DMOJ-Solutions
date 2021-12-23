from sys import stdin
input = stdin.readline


num = int(input())
numbers = sorted([int(input()) for i in range(num)])
if num % 2 == 1:
    print(float(numbers[num // 2]))
else:
    print(float(numbers[num // 2 - 1] + numbers[num // 2]) / 2)
