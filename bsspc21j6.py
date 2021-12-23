import sys
input = sys.stdin.readline


def traverse(node):
    global final
    localC = []
    visited[node] = 1
    for i in connections[node]:
        if not visited[i]:
            localC.append(traverse(i) + kill[i - 2])
    localC.sort(reverse=True)
    if node != 1:
        while len(localC) > 2:
            final += localC.pop()
        return sum(localC)
    return localC


final = 0
n = int(input())
kill = [int(x) for x in input().split()] + [0]
connections = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    connections[a].append(b)
    connections[b].append(a)
finalV = traverse(1)
# print(final)
# print(finalV)
finalV.sort(reverse=True)
# node 1 can have 3 children
while len(finalV) > 3:
    final += finalV.pop()
print(final)
