import sys
input = sys.stdin.readline


n = int(input())
arr = [0] * n
last = 0
for i in range(1, n, 2):
    print("?", i, i + 1)
    sys.stdout.flush()
    two = int(input())
    print("?", i + 1, i)
    sys.stdout.flush()
    one = int(input())
    a = two - one
    arr[i] = (two - a) // -2
    arr[i - 1] = a - arr[i]
    last = one
if n % 2 == 1:
    print("?", n - 2, n)
    sys.stdout.flush()
    v = int(input())
    arr[-1] = -(v - last)
print("!", " ".join([str(x) for x in arr]))
