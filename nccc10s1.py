import sys
input = lambda: sys.stdin.readline()[:-1]
def check(key):
    global n, k
    m = k + 1
    for test in arr:
        ct = 0
        for i in range(k):
            if test[i] == key[i]:
                ct += 1
        m = min(m, ct)
    return m


def makeKeys(key="", dep=0):
    global n, k, ans
    if dep == k:
        ans = max(ans, check(key))
        return
    makeKeys(key + "T", dep + 1)
    makeKeys(key + "F", dep + 1)