def possible_scores(roundNumbers, totalScore, teams, team1, team2, c, d, n, amount, history, history2):
    # roundNumbers = the rounds that are left
    # totalScore = the scores of all four teams
    # team is my favourable team
    # team1 and team2 are the teams that compete, c and d are team1 score and team2 score respectively
    # n = a number; how i keep track of which rounds are played - this is the base case
    # amount is amount of times my team comes on top
    # history is the history of games for team1
    # history2 is the history of games for team2
    # abc is the match that is happening currently

    # this adds the three possible outcomes of the game to each team, and to their history
    totalScore[team1] += c
    totalScore[team2] += d
    history.append([team1, c])
    history2.append([team2, d])

    # this is the base case: if N becomes the amount of rounds left that means all rounds are played
    # then we check to see if my favourable team wins
    if n == len(roundNumbers):
        x = 0
        for abc in range(0, 5):
            if abc == teams:
                pass
            elif totalScore[teams] > totalScore[abc]:
                x += 1
        # x is the counter to see how many of the matches my team won
        # its out of five because i have a score[0] so that
        # when i call the teams i don't need to do score[x - 1]

        if x == 4:
            amount.append(1)

        # because this part of the tree is a dead end, this deletes the history of the dead end
        totalScore[history[-1][0]] -= history[-1][1]
        totalScore[history2[-1][0]] -= history2[-1][1]
        del history[-1]
        del history2[-1]
        return
    else:
        # this finds out what the next match is, assigns the teams to team1 and 2
        # and then there's recursion for the three outcomes
        abc = roundNumbers[n]
        team1 = abc[0]
        team2 = abc[1]
        c = 0
        d = 0
        n += 1
        possible_scores(roundNumbers, totalScore, teams, team1, team2, c + 3, d, n, amount, history, history2)
        possible_scores(roundNumbers, totalScore, teams, team1, team2, c, d + 3, n, amount, history, history2)
        possible_scores(roundNumbers, totalScore, teams, team1, team2, c + 1, d + 1, n, amount, history, history2)

        # we delete the history again after the third recursion
        # because we know all three outcomes of that portion of the tree diagram
        totalScore[history[-1][0]] -= history[-1][1]
        totalScore[history2[-1][0]] -= history2[-1][1]
        del history[-1]
        del history2[-1]


# this is the code
team = int(input())
played = int(input())
rounds = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
score = [-10000, 0, 0, 0, 0]

# based on our input, I see which team won, and add points to the team's score
for i in range(0, played):
    qq = input()
    x_split = qq.split()
    y = [int(x_split[0]), int(x_split[1])]
    z = rounds.index(y)
    del rounds[z]
    if int(x_split[2]) > int(x_split[3]):
        score[y[0]] += 3
    elif int(x_split[3]) > int(x_split[2]):
        score[y[1]] += 3
    else:
        score[y[0]] += 1
        score[y[1]] += 1
team1 = 0
team2 = 0
c = 0
d = 0
n = 0
amount = []
history = []
history2 = []
# calls the function
possible_scores(rounds, score, team, team1, team2, c, d, n, amount, history, history2)
print(len(amount))
