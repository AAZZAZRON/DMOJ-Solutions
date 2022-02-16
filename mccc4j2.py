n, a, b = [int(x) for x in input().split()]
one, two = 0, 0
for _ in range(n):
    x, y = [int(q) for q in input().split()]
    if x < a:
        one += 1
    else:
        one += 2
    if y < b:
        two += 1
    else:
        two += 2
if one < two:
    print("Andrew wins!")
elif two < one:
    print("Tommy wins!")
else:
    print("Tie!")
