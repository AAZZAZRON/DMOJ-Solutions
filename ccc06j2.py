dice1 = int(input())
dice2 = int(input())
if dice1 >= 10:
    dice1 = 10
if dice2 >= 10:
    dice2 = 10
dice = sorted([dice1, dice2])
ans = 0
for i in range(1, dice[0] + 1):
    if 10 - i <= dice[1] and 10 - i != 0:
        ans += 1
if ans == 1:
    print("There is 1 way to get the sum 10.")
else:
    print(f"There are {ans} ways to get the sum 10.")
