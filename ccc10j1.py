num = int(input())
if num <= 5:
    hand1 = num
    hand2 = 0
else:
    hand1 = 5
    hand2 = num - 5
amount = 1

for i in range(0, 5):
    if hand1 < 1 or hand2 > 5 or hand1 == hand2 or hand1 + 1 == hand2 or hand2 + 1 == hand1:
        break
    else:
        amount += 1
        hand1 -= 1
        hand2 += 1

print(amount)
