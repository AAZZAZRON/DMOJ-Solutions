n = int(input())
cmds = input()

oppAmmo = 0
score = 0
myAmmo = 0

for cmd in cmds:
    if cmd == "R":
        oppAmmo += 1
        if myAmmo > 0:
            myAmmo -= 1
            score += 1
        else:
            myAmmo += 1
    elif cmd == "F":
        if oppAmmo == 0:
            if myAmmo > 0:
                myAmmo -= 1
                score += 1
            else:
                myAmmo += 1
        else:
            oppAmmo -= 1
    else:
        myAmmo += 1
print(score)