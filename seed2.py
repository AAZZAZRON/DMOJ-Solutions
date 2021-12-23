import sys
input = sys.stdin.readline


high = 2000000000
num = 1000000000
low = 0
while high - low > 1:
    print(num)
    sys.stdout.flush()
    message = input()[:-1]
    if message == "SINKS":
        low = num
    elif message == "FLOATS":
        high = num
    elif message == "OK":
        break
    num = (low + high) // 2
