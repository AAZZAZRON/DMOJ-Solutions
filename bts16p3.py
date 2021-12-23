n = int(input())
names = [x[0] for x in input().split()]
before = ""
counter = 0
total = 0
for i in names:
    if i == before:
        counter += 1
    else:
        before = i
        total += counter * (counter + 1) // 2
        counter = 1
total += counter * (counter + 1) // 2
print(total % 1000000007)
