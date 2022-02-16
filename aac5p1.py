n = int(input())
v = [0, 0]
for i in [int(x) for x in input().split()]:
    v[i % 2] += 1
print(v[0] // 2 + v[1] // 2)