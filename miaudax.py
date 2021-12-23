line = [int(x) for x in input().split("x")]
line.sort()
print("x".join([str(x) for x in line]))
prod = 1
for i in line:
    prod *= i
print(prod)
