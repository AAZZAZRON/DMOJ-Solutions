from sys import stdin
input = stdin.readline


subways, start, end, n = [int(x) for x in input().split()]
connections = [[] for _ in range(subways + 1)]
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    connections[x].append(y)
visited = {start}
queue = [[start]]
counter = 0
done = False
while queue and not done:
    counter += 1
    queued = queue.pop()
    added = []
    for num in queued:
        for connect in connections[num]:
            if connect not in visited:
                visited.add(connect)
                if connect == end:
                    done = True
                added.append(connect)
    if added:
        queue.append(added)
print(counter)
