distance_input = input()
distance_split = distance_input.split()
distance = []
for i in range(0, 4):
    distance.append(int(distance_split[i]))

c = [0]

for i in range(0, 4):
    c.append(c[i] + distance[i])
for i in range(0, 5):
    r = []
    for j in range(0, 5):
        d = c[j] - c[i]
        if d < 0:
            d = d * -1
        r.append(d)
    print(*r)
