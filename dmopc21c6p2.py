n, k = [int(x) for x in input().split()]
s = input()

t = [len(x) for x in s.split("1")]
t.sort(reverse=True)
print(sum(t[:k]))
