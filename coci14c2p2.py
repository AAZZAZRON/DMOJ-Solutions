from sys import stdin
input = stdin.readline

num = int(input())
people = set()
freq = {}
for i in range(num):
    name = input()[:-1]
    if name in people:
        freq[name] += 1
    else:
        people.add(name)
        freq[name] = 1
for i in range(num - 1):
    name = input()[:-1]
    freq[name] -= 1
    if freq[name] == 0:
        people.remove(name)
print(people.pop())
