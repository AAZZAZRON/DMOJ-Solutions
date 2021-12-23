n = int(input())
numbers = sorted([int(x) for x in input().split()])
final = []
l = n // 2 + (n % 2) - 1
r = l + 1
for i in range(n):
    if i % 2 == 0:
        final.append(str(numbers[l]))
        l -= 1
    else:
        final.append(str(numbers[r]))
        r += 1
print(" ".join(final))
