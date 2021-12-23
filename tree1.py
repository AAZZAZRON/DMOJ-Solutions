def isTree(start):
    visited = {start}
    queue = [[start, -1]]
    while queue:
        branch, prev = queue.pop(0)
        for x in connections[branch]:
            if x in visited and x != prev:
                return False
            if x not in visited:
                visited.add(x)
                queue.append([x, branch])
    if 0 in visited and 1 in visited and 2 in visited and 3 in visited:
        return True
    return False


connections = [[], [], [], []]
for x in range(4):
    q = [int(x) for x in input().split()]
    for y in range(4):
        if q[y] == 1:
            connections[x].append(y)
# print(connections)
for i in range(4):
    if isTree(i):
        print("Yes")
        break
    if i == 3:
        print("No")
