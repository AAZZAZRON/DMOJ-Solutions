import sys
n = int(input())
l = input()
for i in range(n - 1):
    if int(l[i]) < int(l[i + 1]):
        print(l[:i] + l[i + 1] + l[i] + l[i + 2:])
        sys.exit()
print(l)
