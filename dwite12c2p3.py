def bitStrings(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = bitStrings(n - 2, memo) + bitStrings(n - 3, memo)
        return memo[n]


[print(bitStrings(int(input()))) for _ in range(5)]
