from sys import stdin
input = stdin.readline


num, q = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
psa = [0]
for number in numbers:
    psa.append(psa[-1] + number)
# print(psa)
for _ in range(q):
    start, end = [int(x) for x in input().split()]
    print(psa[-1] - (psa[end] - psa[start - 1]))
