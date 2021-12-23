string = input()
n = int(input())
minimum = "z" * n
for i in range(len(string) - n):
    if string[i:i + n] < minimum:
        minimum = string[i:i + n]
print(minimum)
