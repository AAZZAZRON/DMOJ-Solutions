current = input()
transform = input()
match = 0
for i in range(len(min(current, transform))):
    if current[i] != transform[i]:
        break
    match += 1
print(len(current) - match + len(transform) - match)
