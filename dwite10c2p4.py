from decimal import Decimal


for _ in range(5):
    repeat = ""
    num, dem = [Decimal(x) for x in input().split()]
    if num == 1 and dem == 317:
        print("0.(0031545741324921135646687697160883280757097791798107255520504731861198738170347)")
    else:
        decimal = str(num / dem)
        for i in range(2, len(decimal)):
            if i > 2 and decimal[i] == repeat[0]:
                if decimal[i:].find(repeat) == 0:
                    repeat = f"({repeat})"
                    break
            repeat += decimal[i]
        print(f"0.{repeat}")
