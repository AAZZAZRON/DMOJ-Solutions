from sys import stdin
input = stdin.readline


num, q = [int(x) for x in input().split()]
friends = [{x} for x in range(num + 1)]
for _ in range(q):
    command, *line = [int(x) for x in input().split()]
    if command == 1:  # add connection
        one, two = line
        if one not in friends[two]:
            friends[two] = friends[two].union(friends[one])
            for i in friends[two]:
                friends[i] = friends[two]
    else:  # answer query
        print(len(friends[line[0]]))
# print(friends)
