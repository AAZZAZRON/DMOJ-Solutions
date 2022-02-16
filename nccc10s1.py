def solve(curr, ind):
    global n, k
    if ind == k:
        return min(curr)
    return max(solve([curr[x] + (grades[x][ind] == "T") for x in range(n)], ind + 1), solve([curr[x] + (grades[x][ind] == "F") for x in range(n)], ind + 1))


n, k = [int(x) for x in input().split()]
grades = [input() for _ in range(n)]
print(solve([0] * n, 0))
