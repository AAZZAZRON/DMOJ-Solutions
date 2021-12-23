lines = int(input())
define = {"E": "Educational", "C": "Computing", "O": "Organization of Ontario"}

for _ in range(lines):
    stuff = input()
    arr = []
    [arr.append(define["E"]) for _ in range(stuff.count("E"))]
    [arr.append(define["C"]) for _ in range(stuff.count("C"))]
    [arr.append(define["O"]) for _ in range(stuff.count("O") // 2)]
    print(" ".join(arr))
