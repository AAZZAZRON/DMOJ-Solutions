n, m, k, v = [int(x) for x in input().split()]
word = [x for x in input()]
missing = []
c = k ** m
for i in range(m):
    letters = "".join(sorted(input()))
    missing.append(letters)
for i in range(m - 1):
    c //= k
    t = v // c
    if v != 0:
        t += 1
    word[word.index("#")] = missing[i][t - 1]
    v %= c
word[word.index("#")] = missing[-1][v - 1]
print("".join(word))
