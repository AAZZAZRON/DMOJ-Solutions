import sys
input = sys.stdin.readline


rounds, health = input().split()
charlie, bot = [], []
[charlie.append(input().split()) for i in range(int(rounds))]
charlie.append(["Q", "0"])
[bot.append(input().split()) for j in range(int(rounds))]
charlieH = int(health)
botH = int(health)
charlieD, botD = False, False
while bot:
    charlieMove = charlie.pop(0)
    if charlieMove[0] == "A" and not botD:
        botH -= int(charlieMove[1])
    elif charlieMove[0] == "D":
        if bot[0][0] != "A":
            charlieH -= int(charlieMove[1])
        else:
            charlieD = True
    if botD:
        botD = False
    botMove = bot.pop(0)
    if charlieH <= 0:
        print("DEFEAT")
        break
    if botMove[0] == "A" and not charlieD:
        charlieH -= int(botMove[1])
    elif botMove[0] == "D":
        if charlie[0][0] != "A":
            botH -= int(botMove[1])
        else:
            botD = True
    if charlieD:
        charlieD = False
    if botH <= 0:
        print("VICTORY")
        break
if charlieH > 0 and botH > 0:
    print("TIE")
