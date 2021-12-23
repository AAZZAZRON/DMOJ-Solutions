highest = 0
player = 0
for i in range(1, 6):
    x = eval("+".join(input().split()))
    if x > highest:
        highest = x
        player = i
print(player, highest)
