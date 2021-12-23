numSwitches = int(input())
switches = input()
tries = 0
currently = switches[0]
for i in switches:
    if i != currently:
        currently = i
        tries += 1
if switches[-1] == "1":
    print(tries + 1)
else:
    print(tries)
