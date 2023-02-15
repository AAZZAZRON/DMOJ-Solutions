import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    den = (c - b) ** 2
    posOut = (c - b) ** 2 - (a + c) ** 2
    posIn = (a - c) ** 2
    '''print(posIn)
    print(posOut)
    print(den)'''

    ans = (max(0, posIn) + max(0, posOut)) / den
    # assert 0 <= ans <= 1
    print(min(1, ans))
