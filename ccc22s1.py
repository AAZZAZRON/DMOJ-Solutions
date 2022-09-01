n = int(input())
ct = 0
for i in range(n // 4 + 1):
    if (n - 4 * i) % 5 == 0:
        ct += 1
print(ct)
