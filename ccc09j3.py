time = int(input())
print(f"{time} in Ottawa")
time -= 300
if time < 0:
    time += 2400
print(f"{time} in Victoria")
time += 100
if time >= 2400:
    time -= 2400
print(f"{time} in Edmonton")
time += 100
if time >= 2400:
    time -= 2400
print(f"{time} in Winnipeg")
time += 100
if time >= 2400:
    time -= 2400
print(f"{time} in Toronto")
time += 100
if time >= 2400:
    time -= 2400
print(f"{time} in Halifax")
time += 30
if time % 100 >= 60:
    time += 40
if time >= 2400:
    time -= 2400
print(f"{time} in St. John's")
