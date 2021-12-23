negativeD, positiveD, negativeR, positiveR = [], [], [], []
donors = [int(x) for x in input().split()]
recipients = [int(x) for x in input().split()]
count = 0
for i in range(8):
    if i % 2 == 1:
        positiveD.append(donors[i])
        positiveR.append(recipients[i])
    else:
        negativeD.append(donors[i])
        negativeR.append(recipients[i])

for i in range(3): # negative recipients
    donorsLeft = negativeD[i] - negativeR[i]
    if donorsLeft < 0: # too many recipients
        count += negativeD[i]
        negativeD[i] = 0
        if i == 0:
            continue
        back = 0
        while back != -1 and donorsLeft < 0:
            donorsLeft += negativeD[back]
            if donorsLeft >= 0:
                count += negativeD[back] - donorsLeft
                negativeD[back] -= negativeD[back] - donorsLeft
            else:
                count += negativeD[back]
                negativeD[back] = 0
            back -= 1
    else:
        count += negativeR[i]
        negativeD[i] -= negativeR[i]

for i in range(3): # positive recipients
    donorsLeft = positiveD[i] - positiveR[i]
    if donorsLeft < 0:  # too many recipients
        count += positiveD[i]
        positiveD[i] = 0
        if i == 0:
            continue
        back = 0
        while back != -1 and donorsLeft < 0:
            donorsLeft += positiveD[back]
            if donorsLeft >= 0:
                count += positiveD[back] - donorsLeft
                positiveD[back] -= positiveD[back] - donorsLeft
            else:
                count += positiveD[back]
                positiveD[back] = 0
            back -= 1
        queue = [i, 0]
        while queue and donorsLeft < 0:
            back = queue.pop(0)
            donorsLeft += negativeD[back]
            if donorsLeft >= 0:
                count += negativeD[back] - donorsLeft
                negativeD[back] -= negativeD[back] - donorsLeft
            else:
                count += negativeD[back]
                negativeD[back] = 0
    else:
        count += positiveR[i]
        positiveD[i] -= positiveR[i]
add = sum(negativeD)
donorsLeft = add - negativeR[3]
if donorsLeft < 0:  # too many recipients
    count += add
    add = 0
else:
    count += negativeR[3]
    add -= negativeR[3]
add += sum(positiveD)
donorsLeft = add - positiveR[3]
if donorsLeft < 0:  # too many recipients
    count += add
    add = 0
else:
    count += positiveR[3]
    add -= positiveR[3]

print(count)
