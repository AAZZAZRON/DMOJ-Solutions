n, q = [int(x) for x in input().split()]
word = input().split("0")
costs = [int(x) for x in input().split()]
vals = sorted([[costs[i], i] for i in range(q)])
# print(word)
# print(vals)
first = 0
for i in range(q):
    ind = vals[i][1]
    if i == q - 1:
        word[ind - 1] += word[ind]
        word[ind] = ""
    else:
        word[ind] += word[ind + 1]
        word[ind + 1] = ""
    first = ind
    # print(word)
print("".join(word[first:]) + "".join(word[:first]))