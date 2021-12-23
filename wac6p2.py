numLights, numActions = [int(x) for x in input().split()]
config = [int(x) for x in input().split()]
moves = [int(x) for x in input().split()]
wesley = {}
done = False
num = config.count(1)
if config.count(1) == 0:
    print(0)
else:
    for i in range(0, numActions):
        move = moves[i]
        if config[move - 1] == 1:
            num -= 1
            config[move - 1] = 0
        else:
            num += 1
            config[move - 1] = 1
        if num <= i + 1:
            print(i + 1)
            done = True
            break
    if not done:
        print(num)
