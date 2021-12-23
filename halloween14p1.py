N = int(input())
K = int(input())
moves = 0
taking, finding = N % K, K - (N % K)
if K <= N:
    if taking <= finding:
        print(moves + taking)
    else:
        print(moves + finding)
else:
    print(moves + finding)
