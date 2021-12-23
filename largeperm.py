import sys
input = sys.stdin.readline

n, swap = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
indexes = [0] * (n + 1)
for i in range(n):
    indexes[numbers[i]] = i
# print(maximum)
find = [x for x in range(1, n + 1)]
inc = 0
for i in range(swap):
    if not find:
        break
    a = find.pop()
    tmp = numbers[i + inc]
    while a == tmp and i + inc < n and find:
        inc += 1
        a = find.pop()
        tmp = numbers[i + inc]
    if i + inc >= n or not find:
        break
    numbers[i + inc] = a
    numbers[indexes[a]] = tmp
    indexes[tmp] = indexes[a]
print(" ".join([str(x) for x in numbers]))
