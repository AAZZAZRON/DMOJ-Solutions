import sys
input = lambda: sys.stdin.readline()[:-1]


grades = {}
n, c, m = [int(x) for x in input().split()]
if c > n:
    print("Ace is dunzos")
    sys.exit()
for _ in range(n):
    line = input().split()
    x = " ".join(line[:-1])
    y = line[-1]
    grades[x] = int(y)
total = 0
for _ in range(m):
    course = input()
    if course not in grades:
        print("Ace is dunzos")
        sys.exit()
    total += grades[course]
    del grades[course]
# print(grades)
vals = sorted(list(grades.values()), reverse=True)
total += sum(vals[:c - m])
print("%.2f" % (total / c))
