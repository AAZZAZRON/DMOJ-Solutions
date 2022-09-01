ct = 0
n = int(input())
for i in range(n):
    ct += 5 * int(input()) - 3 * int(input()) > 40
print(str(ct) + ("+" if ct == n else ""))
