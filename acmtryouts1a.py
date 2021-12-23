import sys
input = sys.stdin.readline


moves = {"Scissors": "Rock", "Rock": "Paper", "Paper": "Scissors", "Fox": "Foxen"}
num = int(input())
done = False
for i in range(0, num):
    opponent = input()[:-1]
    if opponent == "Foxen":
        done = True
    if not done:
        print(moves[opponent])
