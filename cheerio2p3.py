import sys
input = sys.stdin.readline
one, two, q = map(int, input().split())
if one < two:
    one, two = two, one
for _ in range(q):
    n = int(input())
    if n < two:
        print(9)
    elif n == two:
        print(8)
    elif n <= one:
        print(9)
    elif n < one + two:
        print(0)
    elif n == one + two:
        print(1)