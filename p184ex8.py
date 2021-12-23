from sys import stdin
input = stdin.readline


votes = [0, 0, 0, 0, 0, 0, 0]
char = "ABCDEF"
num = int(input())
for i in range(num):
    vote = input()[:-1]
    votes[char.find(vote)] += 1
for i in votes:
    print(i)
