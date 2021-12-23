string = input()
length = len(string)
l, o, v, e = 0, 0, 0, 0
for i in string[::-1]:
    if i == 'e':
        e += 1
    elif i == 'v':
        v += e
    elif i == 'o':
        o += v
    elif i == 'l':
        l += o
print(l)
