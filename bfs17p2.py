colours = {"red": 0, "orange": 0, "yellow": 0, "green": 0,
           "blue": 0, "black": 0}
n = int(input())
for i in input().split():
    colours[i] += 1
m = max(colours.values())
v = n - m
# use biggest # colour to "buffer", then rainbow the rest
print(min(v + 1, m) + v)
