m = {"A": 1, "B": 0.8, "C": 0.6, "D": 0.4, "E": 0.2}
ans = 1
for _ in range(int(input())):
    ans *= m[input()]
print(ans)