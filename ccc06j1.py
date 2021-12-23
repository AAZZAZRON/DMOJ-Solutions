cal = 0
calories = [[461, 431, 420, 0], [100, 57, 70, 0], [130, 160, 118, 0], [167, 266, 75, 0]]
for i in range(4):
    cal += calories[i][int(input()) - 1]
print(f"Your total Calorie count is {cal}.")
