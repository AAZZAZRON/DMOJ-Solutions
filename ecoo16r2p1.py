import sys
input = lambda: sys.stdin.readline()[:-1]


for _ in range(10):
    before = input()
    word = "#" + "".join([x + "#" for x in before])
    length = len(word)
    p = [0] * length
    c = 0
    r = 0
    maximum = 0
    for i in range(length):
        mirror = c - (i - c)
        if r > i:
            p[i] = min(r - i, p[mirror])
        while i + 1 + p[i] < length and word[i + 1 + p[i]] == word[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
        if i + 1 + p[i] == length or i - 1 - p[i] == -1:
            maximum = max(maximum, p[i])
    print(length // 2 - maximum)
