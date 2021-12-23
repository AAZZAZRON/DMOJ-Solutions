import sys
input = sys.stdin.readline


def bfs(node, noGo, noGo2):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for neighbour in dictionary[s]:
            if neighbour not in visited:
                if s == noGo and neighbour == noGo2:
                    pass
                elif s == noGo2 and neighbour == noGo:
                    pass
                else:
                    visited.append(neighbour)
                    queue.append(neighbour)


for q in range(5):
    numNodes = int(input())
    edges = int(input())
    dictionary = {}
    check = []
    for i in range(edges):
        x = input().split()
        if int(x[0]) in dictionary:
            dictionary[int(x[0])].append(int(x[1]))
        else:
            dictionary[int(x[0])] = [int(x[1])]
        if int(x[1]) in dictionary:
            dictionary[int(x[1])].append(int(x[0]))
        else:
            dictionary[int(x[1])] = [int(x[0])]
        check.append([int(x[0]), int(x[1])])
    alreadyChecked = []
    counter = 0
    for i in check:
        visited = []
        queue = []
        bfs(i[0], i[0], i[1])
        if len(visited) != numNodes:
            counter += 1
    print(counter)
