num = int(input())
towers = [int(x) for x in input().split()]
canSee = [0] * num
arr = [[0, 100000001]]
for x in range(num):
    while arr and towers[x] >= arr[-1][1]:
        arr.pop()
    canSee[x] = x - arr[-1][0]
    arr.append([x, towers[x]])
print(" ".join([str(x) for x in canSee]))
