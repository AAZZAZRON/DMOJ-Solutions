num, q = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
psa = [0] * (num + 1)
for i in range(num):
    psa[i + 1] = psa[i] + numbers[i]
for _ in range(q):
    start, end = [int(x) for x in input().split()]
    print((psa[end] - psa[start - 1]) // (end - start + 1))
