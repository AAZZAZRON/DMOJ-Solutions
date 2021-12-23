import sys
input = sys.stdin.readline


letters, queries = [int(x) for x in input().split()]
alreadyUsed = {x: [0, 0] for x in "abcdefghijklmnopqrstuvwxyz"}
sweep = []
for _ in range(queries):
    letter, a, b = input().split()
    sweep.append([int(b), letter, int(a)])
sweep.sort()
# print(sweep)
word = [""] * letters
# alreadyused[ind][count]
for end, l, c in sweep:  # forward sweep
    copy = c
    c -= alreadyUsed[l][1]
    for i in range(alreadyUsed[l][0], end):
        if c <= 0:
            break
        if word[i] == "":
            word[i] = l
            c -= 1
    if c != 0:
        print(-1)
        sys.exit()
    else:
        alreadyUsed[l] = [end, copy]
sweep.sort(reverse=True)
end = letters
used = set()
for start, l, c in sweep:
    letter = -1
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in used:
            letter = i
            break
    for i in range(start, end):
        if word[i] == "":
            if letter == -1:
                print(-1)
                sys.exit()
            word[i] = letter
    used.add(l)
    end = start
letter = -1
for i in "abcdefghijklmnopqrstuvwxyz":
    if i not in used:
        letter = i
        break
for i in range(end):
    if word[i] == "":
        if letter == -1:
            print(-1)
            sys.exit()
        word[i] = letter
print("".join(word))
# print(word)
# print(alreadyUsed)
