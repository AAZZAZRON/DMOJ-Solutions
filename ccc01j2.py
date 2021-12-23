x = int(input())
m = int(input())

for i in range(0, m):
    prod = x * i
    if prod % m == 1:
        print(i)
        break
    if i == m - 1:
        print("No such integer exists.")