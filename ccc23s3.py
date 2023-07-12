def isValid(s, l):
    assert len(s) == l
    for i in range(l):
        if s[i] != s[l - i - 1]:
            return 0
    return 1


n, m, r, c = map(int, input().split())

ans = [['b'] * m for _ in range(n)]
for i in range(1, n):
    ans[i][-1] = 'c'
    ans[i - 1][0] = 'd'
for i in range(1, m):
    ans[-1][i] = 'e'
    ans[0][i - 1] = 'f'

# [print(x) for x in ans]

for i in range(r):
    ans[i] = ['a'] * m
for i in range(c):
    for j in range(n):
        ans[j][i] = 'a'

if r == n:
    ans[-1] = ['z'] * m
    if m % 2 == 1 and c % 2 == 1:
        # print((m - c) // 2, (m - c) // 2 + c)
        for i in range((m - c) // 2, (m - c) // 2 + c):
            for j in range(n):
                ans[j][i] = 'x'
    elif c % 2 == 0:
        for i in range(c // 2):
            for j in range(n):
                ans[j][i] = 'x'
                ans[j][-i - 1] = 'x'
elif c == m:
    for i in range(n):
        ans[i][-1] = 'z'
    if n % 2 == 1 and r % 2 == 1:
        for i in range((n - r) // 2, (n - r) // 2 + r):
            for j in range(m):
                ans[i][j] = 'x'
    elif r % 2 == 0:
        for i in range(r // 2):
            for j in range(m):
                ans[i][j] = 'x'
                ans[-i - 1][j] = 'x'

rCt = 0
cCt = 0
for i in range(n):
    if isValid("".join(ans[i]), m):
        rCt += 1
for i in range(m):
    tmp = [ans[x][i] for x in range(n)]
    if isValid("".join(tmp), n):
        cCt += 1

# print(rCt, cCt)
if rCt != r or cCt != c:
    print("IMPOSSIBLE")
else:
    [print("".join(x)) for x in ans]