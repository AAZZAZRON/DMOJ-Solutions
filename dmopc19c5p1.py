import sys
input = lambda: sys.stdin.readline()[:-1]


n, q = [int(x) for x in input().split()]
items = {input() for _ in range(n)}
counter = 0
for _ in range(q):
    done = 1
    for _ in range(int(input())):
        if input() not in items:
            done = 0
    if done:
        counter += 1
print(counter)
