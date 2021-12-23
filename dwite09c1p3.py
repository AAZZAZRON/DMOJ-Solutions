for _ in range(5):
    m = int(input())
    found = [0] * (m + 2)
    found[0] = 1
    for _ in range(m):
        found[int(input())] = 1
    print(found.index(0))