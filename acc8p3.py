import sys
input = sys.stdin.readline


m, q = [int(x) for x in input().split()]
fib = [0] * 100001
fib[1] = fib[2] = 1
final = "11"
length = 2
i = 4
fib[3] = 2 % m
final += str(fib[3])
length += len(str(fib[3]))
while True:  # find loop
    fib[i] = (fib[i - 1] + fib[i - 2]) % m
    final += str(fib[i])
    length += len(str(fib[i]))
    i += 1
    if final[-1] == "0" and final[:length // 2] == final[length // 2:]:
        break
length //= 2
repeat = final[:length]
# print(repeat)
for _ in range(q):
    ind = (int(input()) - 1) % length
    print(repeat[ind])
