from sys import stdin
input = stdin.readline


intersections = int(input())
roads = {x: {} for x in range(1, intersections + 1)}
distance, adj, before = {}, {}, [0] * (intersections + 1)
queue = []
# print(roads)
num = int(input())
for _ in range(num):
    m, n, d, s = [int(x) for x in input().split()]
    time = float(d) / s * 60
    if n not in roads[m]:
        roads[m][n] = [time, d, s]
        roads[n][m] = [time, d, s]
    elif roads[m][n][0] > time:
        roads[m][n] = [time, d, s]
        roads[n][m] = [time, d, s]
# print(roads)
start = 1
for i in range(1, intersections + 1):
    distance[i] = 9999999999
    adj[i] = None
    queue.append(i)
distance[1] = 0
while queue:
    # find closest unvisited node
    keyMin = queue[0]
    minVal = distance[keyMin]
    for i in queue[1:]:
        if distance[i] < minVal:
            keyMin = i
            minVal = distance[i]
    current = keyMin
    queue.remove(current)
    # print(current)

    # get the closest paths connected to the current node
    for i in roads[current]:
        alt = roads[current][i][0] + distance[current]
        if distance[i] > alt:
            distance[i] = alt
            adj[i] = current
            before[i] = before[current] + 1
        elif distance[i] == alt:
            if before[current] + 1 < before[i]:
                distance[i] = alt
                adj[i] = current
                before[i] = before[current] + 1

# print(distance)
# print(adj)
# print(before)

total = 0
x = intersections
while True:
    y = adj[x]
    total += float(roads[y][x][1]) / (roads[y][x][2] * 0.75) * 60
    x = y
    if x == 1:
        break

print(before[intersections])
print(round(total - distance[intersections]))
