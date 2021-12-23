from sys import stdin
input = stdin.readline


num, people = int(input()), int(input())
convert = {"S": 0, "M": 1, "L": 2}
possible = [-1]
for _ in range(num):
    possible.append(convert[input()[:-1]])
counter = 0
for _ in range(people):
    size, n = input().split()
    size = convert[size]
    n = int(n)
    if 0 < n <= num and possible[n] >= size:
        counter += 1
        possible[n] = -1
print(counter)
