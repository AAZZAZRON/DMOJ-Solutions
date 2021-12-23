s = int(input())
n = int(input())
check = []
for i in range(1, n + 1):
    a, b, c = [int(x) for x in input().split()]
    if a >= s:
        check.append([a, c, -i])
    else:
        check.append([a, b, -i])
check.sort(reverse=True)
for _ in range(int(input())):
    print(-check[int(input()) - 1][2])