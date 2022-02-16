from collections import defaultdict

a, b = [int(x) for x in input().split()]
one = defaultdict(int)
two = defaultdict(int)

for i in input():
    one[i] += 1
for i in input():
    two[i] += 1

ct = 0
rm = ""
minimum = (a + 1) * (b + 1)
maximum = -1
for key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ct += one[key] * two[key]
    maximum = max(maximum, one[key])
    if two[key] != 0 and one[key] < minimum:
        minimum = one[key]
        rm = key

print(ct + maximum - one[rm])