def check(s):
    for a, b in rules:
        if a in s and b in s:
            return 0
    return 1


def gen(s, c, cc=0):
    if check(s):
        ct = cc
    else:
        ct = 0
    for i in range(c + 1, n + 1):
        ct = max(ct, gen(s | {i}, i, cc + 1))
    return ct


n, m = [int(x) for x in input().split()]
rules = [[int(x) for x in input().split()] for _ in range(m)]
print(gen(set(), 0))
