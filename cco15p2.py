from sys import stdin
input = stdin.readline


def DFS(node, visited):
    hash = int(visited, 2) * 10 + node
    if node == cities - 1:
        return 0, 1
    elif memo[hash] != -1:
        return memo[hash], memo[hash] != 0
    tmp = 0
    reached = 0
    for i, add in adj[node]:
        if visited[i] == "0":
            current, found = DFS(i, visited[:i] + "1" + visited[i + 1:])
            if found:
                reached = 1
                if add + current > tmp:
                    tmp = add + current
    memo[hash] = tmp
    return tmp, reached


memo = [-1] * 10000000
cities, roads = [int(x) for x in input().split()]
adj = [[] for _ in range(cities)]
for _ in range(roads):
    a, b, c = [int(x) for x in input().split()]
    if a == cities - 1 or b == 0:
        continue
    adj[a].append([b, c])
print(DFS(0, "1" + "0" * (cities - 1))[0])
