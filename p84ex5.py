a = float(input())
b = float(input())
if a == 0 and b == 0:
    print("indeterminate")
elif a == 0:
    print("undefined")
else:
    print(f"{(-b / a):.2f}")
