import sys
input = lambda: sys.stdin.readline()[:-1]


n = int(input())
for _ in range(n):
    string = input() + "0"
    ops = int(input())
    take = []
    i = 0
    while i < len(string) - 1 and ops != 0:
        if int(string[i]) > int(string[i + 1]):
            take.append(string[i])
            string = string[:i] + string[i + 1:]
            ops -= 1
            if i != 0:
                i -= 1
        else:
            i += 1
    print(string[:-1] + "".join(sorted(take)))
