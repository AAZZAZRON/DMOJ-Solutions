def get_hash(s):
    hash = 0
    for i in range(len(s)):
        hash = hash * 13 + ord(s[i]) - ord('a') + 1
    return hash


def genword(s):
    global n, m, ans
    if len(s) == n:
        if get_hash(s) == m:
            ans += 1
        return
    for c in 'abcdefghijklmnopqrstuvwxyz':
        genword(s + c)


n = int(input())
m = int(input())
ans = 0
genword("")
print(ans)