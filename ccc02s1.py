def search(number, tickets=None):
    global combos
    global minimumTickets
    if tickets is None:
        tickets = {1: 0, 2: 0, 3: 0, 4: 0}
    if number == 0:
        if tickets not in visited:
            combos += 1
            visited.append(tickets.copy())
            print(f"# of PINK is {tickets[1]} # of GREEN is {tickets[2]} # of RED is {tickets[3]} # of ORANGE is {tickets[4]}")
        num = tickets[1] + tickets[2] + tickets[3] + tickets[4]
        if minimumTickets > num:
            minimumTickets = num
        return
    for i in range(1, 5):
        if number - ticketPrice[i - 1] >= 0:
            tickets[i] += 1
            search(number - ticketPrice[i - 1], tickets)
            tickets[i] -= 1


ticketPrice = [int(input()) for i in range(4)]
price = int(input())
visited = []
minimumTickets = 10000000000000000000000000000
combos = 0
search(price)
print(f"Total combinations is {combos}.")
print(f"Minimum number of tickets to print is {minimumTickets}.")
