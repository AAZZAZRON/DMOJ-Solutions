from sys import setrecursionlimit
setrecursionlimit(1000000)


def search(h):
    global added
    if 0 < h <= num and not visited[h]:
        visited[h] = True
        added.append(h)
    return


num = int(input())
fib = [0] * (num + 1)
fib[1] = 1
fib[2] = 1
for i in range(3, num + 1):
    fib[i] = (fib[i - 1] + fib[i - 2]) % 2021
fib = [(fib[x]) + (x % 50) for x in range(num + 1)]
queue = [[1]]
visited = [False] * (num + 1)
counter = 0
while True:
    counter += 1
    queued = queue.pop()
    added = []
    for house in queued:
        search(house + 1)
        search(house - 1)
        search(house + fib[house])
        search(house - fib[house])
    queue.append(added)
    if visited[num]:
        break
print(counter)
