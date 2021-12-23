from sys import stdin
input = stdin.readline


num = int(input())
word = input()[:-1]
freq = {}
for i in word:
    if i not in freq:
        freq[i] = 1
    else:
        if freq[i] == 2:
            freq[i] -= 1
        else:
            freq[i] += 1
values = list(freq.values())
one, two = 0, 0
for i in values:
    if i == 1:
        one += 1
    else:
        two += 1
if one == 0:
    if two == 0:
        print(0)
    else:
        print(1)
else:
    print(one)
