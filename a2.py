print("Ready")
while True:
    x = input()
    if x == "  ":
        break
    if x == "qp" or x == "pq" or x == "db" or x == "bd":
        print("Mirrored pair")
    else:
        print("Ordinary pair")
