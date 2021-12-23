humidity = int(input())
maxHours = int(input())
t = 1
while t < maxHours:
    alt = (-6*t**4) + (humidity*t**3) + (2*t**2) + t
    if alt <= 0:
        print('The balloon first touches ground at hour:')
        print(t)
        t = maxHours + 1
    else:
        t += 1

if t == maxHours:
    print('The balloon does not touch ground in the given time.')
