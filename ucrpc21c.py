import sys
n, m = [int(x) for x in input().split()]
one, two = 0, 0
for i in range(1, m + 1):
    a, b, c, d = [int(x) for x in input().split()]
    one += a * b
    two += c * d
    if one >= n and two >= n:
        print(f"It's a tie at round {i}!")
        sys.exit()
    if one >= n:
        print(f"Team 1 wins at round {i}!")
        sys.exit()
    if two >= n:
        print(f"Team 2 wins at round {i}!")
        sys.exit()
print("Oh no!")
