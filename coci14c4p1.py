vals = [int(x) for x in input()]
if 0 in vals and sum(vals) % 3 == 0:
    vals.sort(reverse=True)
    print("".join([str(x) for x in vals]))
else:
    print(-1)
