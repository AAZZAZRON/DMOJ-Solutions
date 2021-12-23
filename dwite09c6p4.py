from sys import stdin
input = stdin.readline


for x in range(5):
    amount = int(input())
    numCoins = int(input())
    coins = [int(input()) for _ in range(numCoins)]
    queue = [{0}]
    counter = 0
    while queue:
        added = set()
        queued = queue.pop()
        for i in queued:
            for j in coins:
                if i + j <= amount:
                    added.add(i + j)
        counter += 1
        if amount in added:
            print(counter)
        elif added:
            queue.append(added)
