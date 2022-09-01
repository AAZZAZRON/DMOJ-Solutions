ct = 0
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    ct += (a > b)
print(ct)