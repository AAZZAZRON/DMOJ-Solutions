L = int(input())
D = int(input())
X = int(input())
low, high = D, L
for i in range(L, D + 1):
    val = 0
    for j in str(i):
        val += int(j)
    if val == X:
        if i < low:
            low = i
        if i > high:
            high = i
print(low)
print(high)
