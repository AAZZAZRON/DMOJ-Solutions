import sys
input = sys.stdin.readline


def getWait(off, on, time):
    time %= (on + off)
    if time < off:
        return off - time
    return 0


n, l = [int(x) for x in input().split()]
lights = [[int(x) for x in input().split()] for _ in range(n)]


c = 0
current = 0
for ind, off, on in lights:
    c += ind - current
    current = ind
    c += getWait(off, on, c)
c += l - current
print(c)
