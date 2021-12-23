low = int(input())
high = int(input())
start = (low ** (1. / 2)) // 1
squares = set()
while start ** 2 <= high:
    squares.add(start ** 2)
    start += 1
start = (low ** (1. / 3)) // 1
cubes = set()
while start ** 3 <= high:
    cubes.add(start ** 3)
    start += 1
print(len(squares) - len(squares.difference(cubes)))
