import sys
input = lambda: sys.stdin.readline()[:-1]


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
encrypt = {}
for i in letters:
    encrypt[i] = input()
times = int(input())
word = input()
foundBefore = set()
modulo = []
mod = -1
for i in range(times + 1):
    if word in foundBefore:
        mod = i
        break
    foundBefore.add(word)
    modulo.append(word)
    new = ""
    for j in word:
        new += encrypt[j]
    word = new
if mod == -1:
    print(modulo[-1])
else:
    print(modulo[times % mod])
