yes = {}
no = {}
group = {}
for _ in range(int(input())):
    a, b = input().split()
    if a not in yes:
        yes[a] = [b]
    else:
        yes[a].append(b)
for _ in range(int(input())):
    a, b = input().split()
    if a not in no:
        no[a] = [b]
    else:
        no[a].append(b)
for i in range(int(input())):
    for name in input().split():
        group[name] = i
ct = 0
for i in yes:
    for j in yes[i]:
        if group[i] != group[j]:
            ct += 1
for i in no:
    for j in no[i]:
        if group[i] == group[j]:
            ct += 1
print(ct)
