words = {}
for _ in range(int(input())):
    x, y = input().split()
    words[y] = x
line = input()[:-1].split()
for i in range(len(line)):
    if line[i] in words:
        line[i] = words[line[i]]
print(" ".join(line) + ".")
