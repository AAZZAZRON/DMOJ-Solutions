num, maxPickup = [int(x) for x in input().split()]
garbage = sorted([int(x) for x in input().split()])
print(sum(garbage[max(0, num - maxPickup):]))
