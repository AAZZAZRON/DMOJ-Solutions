num = int(input())
one = []
two = []
score_one = 100
score_two = 100
for i in range(0, num):
    x = input()
    split = x.split()
    one.append(int(split[0]))
    two.append(int(split[1]))

for i in range(0, len(one)):
    x = one[i]
    y = two[i]
    if x == y:
        pass
    elif x > y:
        score_two = score_two - x
    else:
        score_one = score_one - y
print(score_one)
print(score_two)
