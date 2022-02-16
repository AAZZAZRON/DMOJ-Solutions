n, m = [int(x) for x in input().split()]
ct = 0
for _ in range(n):
    line = input()
    ct += line.count("t")
print(ct)
