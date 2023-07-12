n = int(input())
best = 0
two = 1
while two * 2 < n:
    best = max(best, two * (n - two * 2) * (n - two * 2 - 1) // 2)
    two += 1
print(best)
