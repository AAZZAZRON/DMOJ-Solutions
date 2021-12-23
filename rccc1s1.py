letters, consonant, vowels = [int(x) for x in input().split()]
v = set([x for x in "aeiouy"])
c = set([x for x in "bcdfghjklmnpqrstvwxyz"])
word = input()
vCounter = 0
cCounter = 0
cCount, vCount = 0, 0
finish = False
done = False
while not finish:
    if word[vCounter] in v:
        changed = False
        done = True
        if word[vCounter] == "y":
            changed = True
            cCounter = vCounter
            cCount = 1
        else:
            cCount = 0
        for x in range(1, vowels + 1 - vCount):
            if letters == vCounter + x:
                done = False
                finish = True
                break
            if word[vCounter + x] not in v:
                if word[vCounter + x - 1] != "y":
                    cCount = 0
                else:
                    cCount += 1
                cCounter = vCounter + x
                done = False
                break
            elif word[vCounter + x] == "y":
                if word[vCounter + x - 1] != "y":
                    cCount = 0
                else:
                    cCount += 1
                cCounter = vCounter + x
    if not done:
        if word[cCounter] in c:
            changed = False
            done = True
            if word[cCounter] == "y":
                changed = True
                vCounter = cCounter
                vCount = 1
            else:
                vCount = 0
            for x in range(1, consonant + 1 - cCount):
                if letters == cCounter + x:
                    done = False
                    finish = True
                    break
                if word[cCounter + x] not in c:
                    if word[cCounter + x - 1] != "y":
                        vCount = 0
                    else:
                        vCount += 1
                    vCounter = cCounter + x
                    done = False
                    break
                elif word[cCounter + x] == "y":
                    if word[cCounter + x - 1] != "y":
                        vCount = 0
                    else:
                        vCount += 1
                    vCounter = cCounter + x
    if done:
        print("NO")
        finish = True
        break
if not done:
    print("YES")
