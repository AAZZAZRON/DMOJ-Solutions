import sys
input = sys.stdin.readline


tax = int(input())
n = int(input())
final = sum([int(input()) for _ in range(n)])
print(tax * (n + 1) - final)
