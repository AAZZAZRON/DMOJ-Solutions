from sys import exit

n = int(input())
go = [0] * (n + 1)
q = int(input())
for i in range(q):
    # print(go)
    v = int(input())
    while go[v] != 0 and v - go[v] >= 1:
        tmp = v - go[v]
        go[v] += 1
        v = tmp
    if go[v] != 0:
        print(i)
        exit()
    go[v] += 1
print(q)
