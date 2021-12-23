num = int(input())
data = []

for i in range(0, num):
    input_data = input()
    data.append(input_data)
r = []
x = []
for i in range(0, len(data)):
    data_split = data[i].split()
    r.append(data_split)
    x.append(data_split)
g = r
a = g[0][0]
b = g[0][-1]
c = g[-1][0]
d = g[-1][-1]


small = 10000000000
for i in range(0, len(g)):
    if small > int(r[0][i]):
        small = int(r[0][i])
    if small > int(r[-1][i]):
        small = int(r[-1][i])
    if small > int(r[i][0]):
        small = int(r[i][0])
    if small > int(r[i][-1]):
        small = int(r[i][-1])

small = str(small)
if small == a:
    for line in range(0, len(data)):
        print(data[line])
elif small == d:
    printed = ''
    for i in range(1, len(r) + 1):
        printed = ''
        for j in range(1, len(r) + 1):
            printed = printed + r[-i][-j] + ' '
        printed = printed.rstrip()
        print(printed)
elif small == c:
    printed = ''
    for i in range(0, len(r)):
        printed = ''
        for j in range(1, len(r) + 1):
            printed = printed + x[-j][i] + ' '
        printed = printed.rstrip()
        print(printed)
elif small == b:
    printed = ''
    for i in range(1, len(r) + 1):
        printed = ''
        for j in range(0, len(r)):
            printed = printed + r[j][-i] + ' '
        printed = printed.rstrip()
        print(printed)
