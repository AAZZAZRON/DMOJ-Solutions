# 58 cents requires 2 quarters, 1 nickel, 3 cents.
number = int(input())
copy = number
money = {}
while number >= 25:
    if "quarter" not in money:
        money["quarter"] = 0
    money["quarter"] += 1
    number -= 25
while number >= 10:
    if "dime" not in money:
        money["dime"] = 0
    money["dime"] += 1
    number -= 10
while number >= 5:
    if "nickel" not in money:
        money["nickel"] = 0
    money["nickel"] += 1
    number -= 5
while number >= 1:
    if "cent" not in money:
        money["cent"] = 0
    money["cent"] += 1
    number -= 1
sentence = f"{copy} cents requires " if copy != 1 else f"{copy} cent requires "
for i in money.keys():
    sentence += f"{money[i]} {i}s" if money[i] != 1 else f"{money[i]} {i}"
    sentence += ", "
print(sentence[:-2] + ".")
