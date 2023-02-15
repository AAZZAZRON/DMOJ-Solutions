import sys
sys.setrecursionlimit(1000000)


def recurse(v="", dep=0):
    global l, r, ct
    if l <= int(v, 16) <= r:
        ct += 1
    if dep == 8:
        return
    recurse(v + "A", dep + 1)
    recurse(v + "C", dep + 1)
    recurse(v + "E", dep + 1)


l = int(input())
r = int(input())
ct = 0
recurse()
print(ct)
