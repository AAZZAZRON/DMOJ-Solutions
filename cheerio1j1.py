v = "aeiou"
w = input()

p = w[0] in v
ans = 1
for i in w[1:]:
    if (i in v) == p:
        ans = 0
    p = not p
print("YES" if ans == 1 else "NO")