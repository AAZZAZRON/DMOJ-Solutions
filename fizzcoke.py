import sys
input = sys.stdin.readline


n, upTo = [int(x) for x in input().split()]
checks = []
for _ in range(n):
    line = input().split()
    line[0] = int(line[0])
    checks.append(line)
checks.sort()
output = [""] * (upTo + 1)
for interval, word in checks:
    for i in range(interval, upTo + 1, interval):
        output[i] += word
for i in range(1, upTo + 1):
    if output[i] == "":
        print(i)
    else:
        print(output[i])
