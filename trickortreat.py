num, limit = [int(x) for x in input().split()]
barter = sorted([int(x) for x in input().split()])
barter.append(1000000000000000000000)
time = -1
counter = 0
while time <= limit and counter < num:
    time += 1
    time += barter[counter]
    counter += 1
if counter == 10000:
    counter += 1
print(counter - 1)
