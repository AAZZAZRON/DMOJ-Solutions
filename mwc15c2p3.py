num = int(input())
moves = input().split()
visited = {(0, 0)}
coord = [0, 0]
direction = {"L": [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}
for i in range(num + 1):
    if i == num:
        print("Safe!")
        break
    x, y = direction[moves[i]]
    coord[0] += x
    coord[1] += y
    if tuple(coord) in visited:
        print(f"Fell at {i + 1}")
        break
    visited.add(tuple(coord))
