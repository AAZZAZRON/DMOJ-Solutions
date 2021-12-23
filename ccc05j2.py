low = int(input())
high = int(input())
count = 0
for num in range(low, high + 1):
    factors = 0
    for factor in range(2, num // 2 + 1):
        if num % factor == 0:
            factors += 1
    if factors == 2:
        count += 1
print(f"The number of RSA numbers between {low} and {high} is {count}")
