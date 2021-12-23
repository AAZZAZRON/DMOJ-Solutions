import sys
input = lambda: sys.stdin.readline()[:-1]

items = {}
order = []
for _ in range(int(input())):
    word = input()
    items[word] = []
    order.append(word)
for i in range(1, int(input()) + 1):
    items[input()].append(i)
for i in order:
    [print(x) for x in items[i]]
