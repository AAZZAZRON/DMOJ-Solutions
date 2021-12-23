from bisect import bisect_right


lenS, lenT = [int(x) for x in input().split()]
bigS = input()
s = {}
for q in range(1, lenS + 1):
    i = bigS[q - 1]
    if i in s:
        s[i].append(q)
    else:
        s[i] = [q]
t = input()
counter = 0
before = 0
track = 0
for letter in t:
    if letter not in s:
        counter = -1
        break
    index = bisect_right(s[letter], track)
    if index == len(s[letter]):
        counter += (lenS - before)
        before = 0
        track = 0
        index = bisect_right(s[letter], track)
    track = s[letter][index]
    counter += (s[letter][index] - before)
    before = s[letter][index]
print(counter)
