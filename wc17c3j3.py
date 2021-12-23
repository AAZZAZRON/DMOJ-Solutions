password = input()
valid = True
l, u, n = 0, 0, 0
if len(password) < 8 or len(password) > 12:
    valid = False
if valid:
    for i in password:
        asc = ord(i)
        if 65 <= asc <= 90:
            u += 1
        elif 97 <= asc <= 122:
            l += 1
        elif 48 <= asc <= 57:
            n += 1
    if l < 3 or u < 2 or n < 1:
        valid = False
if valid:
    print("Valid")
else:
    print("Invalid")
