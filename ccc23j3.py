ct = [0] * 5
for _ in range(int(input())):
    line = input()
    for i in range(5):
        ct[i] += (1 if line[i] == "Y" else 0)
m = max(ct)
start = 1
for i in range(5):
    if ct[i] == m:
        if start:
            print(i + 1, end='')
            start = 0
        else:
            print(f",{i+1}", end='')
print()