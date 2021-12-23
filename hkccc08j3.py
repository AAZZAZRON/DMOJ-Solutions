import sys
input = sys.stdin.readline


phonebook = {}
names = {}
n = int(input())
for i in range(n):
    x, y = input().split()
    phonebook[int(y)] = [0, x]
for _ in range(int(input())):
    phonebook[int(input())][0] += 1
maximum = 0
name = ""
num = 0
for i in phonebook.keys():
    if phonebook[i][0] > maximum:
        maximum = phonebook[i][0]
        name = phonebook[i][1]
        num = i
    elif phonebook[i][0] == maximum:
        if i < num:
            num = i
            name = phonebook[i][1]
print(name)
