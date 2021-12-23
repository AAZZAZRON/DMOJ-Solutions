input = input()
suits = {"C": "", "D": "", "H": "", "S": ""}
points = {"J": 1, "Q": 2, "K": 3, "A": 4}
score = 0
suitScore = {"C": 0, "D": 0, "H": 0, "S": 0}
suit = ""
void = {0: 3, 2: 2, 4: 1}
for i in input:
    if i == "C":
        suit = i
    elif i == "H":
        suit = i
    elif i == "S":
        suit = i
    elif i == "D":
        suit = i
    else:
        suits[suit] += i + " "
        if i in points.keys():
            score += points[i]
            suitScore[suit] += points[i]
if len(suits["C"]) in void:
    score += void[len(suits["C"])]
    suitScore["C"] += void[len(suits["C"])]
if len(suits["H"]) in void:
    score += void[len(suits["H"])]
    suitScore["H"] += void[len(suits["H"])]
if len(suits["D"]) in void:
    score += void[len(suits["D"])]
    suitScore["D"] += void[len(suits["D"])]
if len(suits["S"]) in void:
    score += void[len(suits["S"])]
    suitScore["S"] += void[len(suits["S"])]
print("Cards Dealt\t\t\t\t\tPoints")
print("Clubs", suits["C"], "\t\t" + str(suitScore["C"]))
print("Diamonds", suits["D"], "\t\t" + str(suitScore["D"]))
print("Hearts", suits["H"], "\t\t" + str(suitScore["H"]))
print("Spades", suits["S"], "\t\t" + str(suitScore["S"]))
print("\t\t\t\t\t\tTotal", score)
