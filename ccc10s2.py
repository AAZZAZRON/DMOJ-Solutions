n = int(input())
m = {}
for _ in range(n):
    a, b = input().split()
    m[b] = a
word = input()
ind = 0
f = ""
while ind < len(word):
    for i in m:
        if word[ind:].find(i) == 0:
            f += m[i]
            ind += len(i)
print(f)
