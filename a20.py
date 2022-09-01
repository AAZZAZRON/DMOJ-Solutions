t = "0123456789ABCDEF"
for _ in range(int(input())):
    n = input()
    ind = t.index(n[2])
    if ind % 2 == 0:
        print(n)
    else:
        print(n[:2] + t[ind - 1] + n[3:], n)
