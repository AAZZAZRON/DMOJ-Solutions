import sys
input = lambda: sys.stdin.readline()[:-1]
n, q = [int(x) for x in input().split()]
dict = {"home": 0, "Waterloo GO": n + 1}
for i in range(1, n + 1):
    dict[input()] = i
connections = [[0] * (n + 2) for _ in range(n + 2)]
for _ in range(q):
    one, two = input().split("-")
    a = dict[one]
    b = dict[two]
    connections[a][b] = 1
    connections[b][a] = 1

visited = [0] * (n + 2)
visited[0] = 1
queue = [[0]]
counter = 0
while queue:
    counter += 1
    queued = queue.pop()
    added = []
    for node in queued:
        for j in range(1, n + 2):
            if connections[node][j] and not visited[j]:
                visited[j] = 1
                added.append(j)
                if j == n + 1:
                    print(counter)
                    sys.exit()
    if added:
        queue.append(added)
print("RIP ACE")

