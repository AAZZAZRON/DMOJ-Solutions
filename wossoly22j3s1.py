n = int(input())
grid = [input().split() for _ in range(5)]
for _ in range(n):
    words = input()
    s = ""
    ind = 0
    while ind < len(words):
        if words[ind].islower():
            s += words[ind]
            ind += 1
        else:
            r = ord(words[ind]) - ord("A")
            c = int(words[ind + 1]) - 1
            ind += 2
            s += grid[r][c]
    print(s)