def recurse(i, j, s):
    global one, two, lO, lT
    if i == len(one) and j == len(two):
        ans.add(s)
        return
    if j != len(two):
        recurse(i, j+1, s+two[j])
    if i != len(one):
        recurse(i+1, j, s+one[i])


one, two = input().split()
lO = len(one)
lT = len(two)
ans = set()
recurse(0, 0, '')
[print(x) for x in ans]