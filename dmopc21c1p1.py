n = int(input())
arr = [int(x) for x in input().split()]
duke, alice = 0, 0
for i in arr:
    if i % 2 == 0:
        duke += i // 2
    else:
        alice += i // 2 + 1
if duke > alice:
    print("Duke")
else:
    print("Alice")
