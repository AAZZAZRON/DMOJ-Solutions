import sys
input = sys.stdin.readline


q = int(input())
for _ in range(q):
    n = int(input())
    numbers = [int(x) for x in input().split()]
    counter = 0
    for i in range(n):
        for j in range(n - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                counter += 1
    print(f"Optimal train swapping takes {counter} swaps.")
