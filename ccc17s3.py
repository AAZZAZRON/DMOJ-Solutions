from collections import defaultdict
n = int(input())
vals = defaultdict(int)
for i in input().split():
    vals[int(i)] += 1
freq = defaultdict(int)
l = len(vals)
keys = list(vals.keys())
for i in range(l):
    freq[keys[i] * 2] += vals[keys[i]] // 2
    for j in range(i + 1, l):
        freq[keys[i] + keys[j]] += min(vals[keys[i]], vals[keys[j]])
m = -1
ct = 1

for i in freq.keys():
    if freq[i] > m:
        m = freq[i]
        ct = 1
    elif freq[i] == m:
        ct += 1
print(m, ct)
# print(freq)
