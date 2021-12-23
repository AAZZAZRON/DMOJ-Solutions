from sys import stdin
input = stdin.readline


while True:
    size, num = [int(x) for x in input().split()]
    if size == num == 0:
        break
    buckets = [int(input()) for _ in range(num)]
    dp = [101] * (size + 1)
    dp[0] = 0
    for bucket in buckets:
        for i in range(bucket, 2 * bucket):
            for j in range(i, size + 1, bucket):
                if dp[j - bucket] != 101:
                    dp[j] = min(dp[j], dp[j - bucket] + 1)
    if dp[-1] == 101:
        print(-1)
    else:
        print(dp[-1])
