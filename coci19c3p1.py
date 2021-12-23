from sys import stdin
input = stdin.readline


num = int(input())
values = []
value = ["", 0]
ties = 1
for i in range(num):
    x = input()[:-1]
    if x != value[0]:
        values.append(value)
        value = [x, 1]
    else:
        value[1] += 1
values.append(value)
one, two = 0, 0
turnover = 0
for team, points in values[1:]:
    if team == "1":
        if one < two <= one + points:
            ties += 1
        if one < two < one + points:
            turnover = max(turnover, points)
        one += points
    else:
        if two < one <= two + points:
            ties += 1
        if two < one < two + points:
            turnover = max(turnover, points)
        two += points
# print(values)
print(one, two)
print(ties)
print(turnover)
