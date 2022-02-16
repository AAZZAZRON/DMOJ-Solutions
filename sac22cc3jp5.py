import sys
sys.setrecursionlimit(100000)


def test(ind):
    global s, m
    if memo[ind] != "-1":
        return memo[ind]
    elif ind == m:
        return ""
    t = ""
    ret = "z" * 10001
    l = 10001
    for i in range(ind, min(m, ind + 11)):
        t += s[i]
        if t in alphabet:
            if ret == "":
                ret = alphabet[t] + test(i + 1)
                l = len(ret)
            else:
                tmp = alphabet[t] + test(i + 1)
                tL = len(tmp)
                if tL < l:
                    ret = tmp
                    l = tL
                elif tL == l:
                    ret = min(ret, tmp)
    memo[ind] = ret
    return ret


n, m = [int(x) for x in input().split()]
alphabet = {}
s = input()
memo = ["-1"] * 10001
for _ in range(n):
    a, b = input().split()
    if b in alphabet:
        alphabet[b] = min(a, alphabet[b])
    else:
        alphabet[b] = a
print(test(0))
