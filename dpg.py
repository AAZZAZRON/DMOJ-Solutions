from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline


def solve(node):
    if memo[node] != -1:
        return memo[node] + 1
    elif node == -1:
        longest = 0
        for i in range(1, nodes + 1):
            longest = max(longest, solve(i))
        return longest
    else:
        longest = -1
        for next in connections[node]:
            longest = max(longest, solve(next))
        memo[node] = longest
        return longest + 1


nodes, num = [int(x) for x in input().split()]
memo = [-1] * (nodes + 1)
connections = [[] for _ in range(nodes + 1)]
for _ in range(num):
    a, b = [int(x) for x in input().split()]
    connections[a].append(b)
print(solve(-1))
# print(memo)
