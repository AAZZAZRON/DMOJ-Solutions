from sys import stdin
input = stdin.readline


def check(a, b):
    global visited, added, end
    if 1 <= a <= num and 1 <= b <= lines[a] and (a, b) not in visited:
        visited.add((a, b))
        added.append([a, b])
    return


num = int(input())
lines = [0] + [int(input()) for _ in range(num)] + [0]
start = [int(x) for x in input().split()]
end = tuple(int(x) for x in input().split())

visited = {tuple(start)}
queue = [[start]]
counter = 0
while queue:
    counter += 1
    queued = queue.pop()
    added = []
    for one, two in queued:
        x, y = one, two
        # right
        y += 1
        if y > lines[x]:
            x += 1
            y = 1
        check(x, y)

        x, y = one, two
        y -= 1
        # left
        if y < 1:
            x -= 1
            y = lines[x]
        check(x, y)

        x, y = one, two
        # up
        x -= 1
        y = min(lines[x], y)
        check(x, y)

        x, y = one, two
        # down
        x += 1
        y = min(lines[x], y)
        check(x, y)
    if end in visited:
        print(counter)
        break
    queue.append(added)

