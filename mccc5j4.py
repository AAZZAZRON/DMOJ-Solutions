import sys
n = int(input())
s = [x for x in input()]
ast = s.count("*")
ct = sum([ord(x) - ord('a') + 1 for x in s if x != "*"])
if 26 * ast + ct < n or ast + ct > n:
    print("Impossible")
    sys.exit()
for i in range(len(s)):
    if s[i] == "*":
        if ct + 1 + 26 * (ast - 1) >= n:
            s[i] = 'a'
            ast -= 1
            ct += 1
        else:
            v = n - 26 * (ast - 1) - ct
            ast -= 1
            ct += v
            s[i] = chr(ord('a') - 1 + v)
print("".join(s))