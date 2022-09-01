a = int(input())
b = int(input())
c = [int(x) for x in input().split()]
print(*[x + 2 * b for x in c])