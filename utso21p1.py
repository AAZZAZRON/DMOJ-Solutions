people = int(input())


dimensions = 1
capacity = 2
add = 3
while True:
    if capacity >= people:
        print(dimensions)
        break
    capacity += add
    dimensions += 1
    if add == dimensions:
        add += 2
    print(dimensions, people, capacity)
