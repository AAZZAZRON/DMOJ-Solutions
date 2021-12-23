from sys import stdin
input = stdin.readline


lines = int(input())
for w in range(1, lines + 1):
    tree = {}
    num, gen = [int(x) for x in input().split()]
    for _ in range(num):
        person, number, *descendants = input().split()
        tree[person] = descendants
    print(f"Tree {w}:")
    fit = {}
    for person in tree:
        queue = [[person]]
        counter = 0
        people = 0
        while queue and counter < gen:
            counter += 1
            queued = queue.pop()
            added = []
            for x in queued:
                if x in tree:
                    added.extend(tree[x])
                    if counter == gen:
                        people += len(tree[x])
            if added:
                queue.append(added)
        if people > 0:
            if people not in fit:
                fit[people] = []
            fit[people].append(person)
    keys = list(fit.keys())
    keys.sort(reverse=True)
    printed = 0
    for i in range(0, min(3, len(keys))):
        if printed >= 3:
            break
        for x in sorted(fit[keys[i]]):
            printed += 1
            print(f"{x} {keys[i]}")

    if w != lines:
        print()
