n = int(input())
a, b, c = [int(x) for x in input().split()]
ans = 1 * a + 4 * b + c * 7
print("Time to go shopping!" if ans <= n else "You cannot afford them all.")
