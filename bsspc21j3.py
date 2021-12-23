import sys
input = lambda: sys.stdin.readline()[:-1]


r, c = [int(x) for x in input().split()]
grid = [[x for x in input()] for _ in range(c)]
colours = [{"R", "O", "P", "B"}, {"Y", "O", "G", "B"}, {"U", "G", "P", "B"}]
counter = 0
final = []
for make in colours:
    counter = 0
    for t in grid:
        used = 0
        for i in t:
            if i in make:
                if not used:
                    used = 1
                    counter += 1
            else:
                if used:
                    used = 0
    final.append(str(counter))
print(" ".join(final))

