v = [0] * 101
m = 0
n = int(input())
while n != -1:
    v[n] += 1
    m = max(m, v[n])
    n = int(input())
for i in range(1, 101):
    if v[i] == m:
        print(i)