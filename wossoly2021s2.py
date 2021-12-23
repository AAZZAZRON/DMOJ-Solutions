vals = {"BR": 0, "GR": 0, "BG": 0, "R": 0, "B": 0, "G": 0}
n = int(input())
top = input()
right = input()
down = input()
left = input()
c = 0
for i in range(n):
    a = top[i]
    b = down[i]
    if a == b:
        vals[a] += 1
    else:
        vals["".join(sorted([a, b]))] += 1
        vals[a] += 1
        vals[b] += 1
for i in range(n):
    a = left[i]
    b = right[i]
    v = []
    for j in "BGR":
        if a != j and j != b:
            v.append(j)
    c += vals["".join(v)]
print(c)