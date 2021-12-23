from sys import stdin
input = stdin.readline


num = int(input())
circle = {}
for i in range(num):
    one, two = [int(x) for x in input().split()]
    if one not in circle:
        circle[one] = [two]
    else:
        circle[one].append(two)
while True:
    one, two = [int(x) for x in input().split()]
    if one == two == 0:
        break
    visited = {one}
    queue = [circle[one]]
    count = 0
    found = False
    while queue:
        section = queue.pop(0)
        add = []
        for person in section:
            if person == two:
                found = True
                break
            elif person not in visited:
                visited.add(person)
                add.extend(circle[person])
        count += 1
        if not found and add:
            queue.append(add)
    if found:
        print("Yes", count - 1)
    else:
        print("No")
