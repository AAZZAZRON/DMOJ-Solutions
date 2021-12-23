from sys import stdin
input = stdin.readline


people = int(input())
bids = {}
for i in range(people):
    name = input()
    money = int(input())
    if money not in bids:
        bids[money] = name
maximum = max(list(bids.keys()))
print(bids[maximum])
