import sys
input = sys.stdin.readline


q, kill, death = [int(x) for x in input().split()]
beat = float(input())
addDeath = 0
for _ in range(q):
    a, b = [int(x) for x in input().split()]
    kill += a
    death += b
if death == 0:
    print("stop hacking!")
elif kill / death > beat:
    print("Y")
else:
    print("N")
