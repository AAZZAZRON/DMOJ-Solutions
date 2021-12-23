import sys
input = sys.stdin.readline
A, B, C, D, E, F = 0, 0, 0, 0, 0, 0


while True:
    x = int(input())
    if 0 <= x <= 9999:
        A += 1
    elif 10000 <= x <= 19999:
        B += 1
    elif 20000 <= x <= 29999:
        C += 1
    elif 30000 <= x <= 39999:
        D += 1
    elif 40000 <= x <= 49999:
        E += 1
    elif 50000 <= x <= 1000000:
        F += 1
    else:
        break
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
