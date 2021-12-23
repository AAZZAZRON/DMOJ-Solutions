import sys
input = sys.stdin.readline


n, minimum = int(input()), int(input())
diff = [0] * (n + 2)
for _ in range(int(input())):
    l, r, k = [int(x) for x in input().split()]
    diff[l] += k
    diff[r + 1] -= k
for i in range(1, n + 1):
    diff[i] += diff[i - 1]
# print(diff)
counter = 0
for i in diff[1:n + 1]:
    if i < minimum:
        counter += 1
print(counter)
