x = int(input())
q = -1
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(10001):
    x += 1
    for j in range(0, 10):
        y = str(x).count(num[j])
        if y > 1:
            q = 0
            break
        else:
            q = 1
    if q == 1:
        print(x)
        break
