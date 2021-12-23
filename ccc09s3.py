from sys import stdin
input = stdin.readline


connections = [set(), {6}, {6}, {4, 5, 6, 15}, {3, 5, 6}, {3, 4, 6},
               {1, 2, 3, 4, 5, 7}, {6, 8}, {7, 9}, {8, 10, 12}, {9, 11},
               {10, 12}, {9, 11, 13}, {12, 14, 15}, {13}, {3, 13},
               {17, 18}, {16, 18}, {16, 17}, set(), set(), set(), set(),
               set(), set(),
               set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(),
               set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(),
               set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]

while True:
    command = input()[:-1]
    if command == "i":
        x, y = int(input()), int(input())
        connections[x].add(y)
        connections[y].add(x)
    elif command == "d":
        x, y = int(input()), int(input())
        connections[x].remove(y)
        connections[y].remove(x)
    elif command == "n":
        print(len(connections[int(input())]))
    elif command == "f":
        x = int(input())
        friends = set()
        for i in connections[x]:
            friends = friends.union(connections[i])
        print(len(friends.difference(connections[x])) - 1)
    elif command == "s":
        x, y = int(input()), int(input())
        visited = {x}
        queue = [[x]]
        found = False
        counter = 0
        while queue:
            counter += 1
            added = []
            queued = queue.pop()
            for i in queued:
                for j in connections[i]:
                    if j not in visited:
                        visited.add(j)
                        added.append(j)
                    if j == y:
                        found = True
                        break
                if found:
                    break
            if added and not found:
                queue.append(added)
        if found:
            print(counter)
        else:
            print("Not connected")
    else:
        break
