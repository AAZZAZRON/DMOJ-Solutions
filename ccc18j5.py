import sys
input = sys.stdin.readline


n = int(input())
connections = [[]]
for i in range(1, n + 1):
    connections.append([int(x) for x in input().split()][1:])
# print(connections)
visited = [0] * (n + 1)
fastest = n + 1
counter = 0
q = [[1]]
visited[1] = 1
while q:
    counter += 1
    queued = q.pop()
    added = []
    for node in queued:
        for next in connections[node]:
            if not visited[next]:
                visited[next] = 1
                added.append(next)
        if not connections[node]:
            fastest = min(fastest, counter)
    if added:
        q.append(added)
print("Y" if sum(visited) == n else "N")
print(fastest)
