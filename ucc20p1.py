num = int(input())
one = input()
two = input()
counter = 0
for i in range(num):
    if one[i] == two[i] == "0":
        counter += 1
print(counter)
