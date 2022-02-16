p, q, w = [int(input()) for _ in range(3)]
m = -1
q *= 100
q -= 50
for i in range(100, -1, -1):
    if p * (100 - w) + w * i >= q:
        m = i
print(m if m != -1 else "DROP THE COURSE")

