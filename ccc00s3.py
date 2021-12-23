import sys
input = sys.stdin.readline


def check(start, end):
    valid.append(start)
    queue.append(start)
    while queue:
        s = queue.pop(0)
        for n in linksGoTo[s]:
            if n == end:
                return "yes"
            if n not in valid:
                valid.append(n)
                queue.append(n)


linksGoTo = {}
links = int(input())
for i in range(links):
    link = input()
    if "\n" in link:
        link = link[:-1]
    linksGoTo[link] = []
    while True:
        x = input()
        while True:
            if "<A HREF=" not in x:
                break
            split = x.split("\"")
            linksGoTo[link].append(split[1])
            print("Link from {} to {}".format(link, split[1]))
            x = "\"".join(split[2:])
        if "</HTML>" in x:
            break
while True:
    x = input()
    if "\n" in x:
        x = x[:-1]
    if x == "The End":
        break
    else:
        y = input()
        if "\n" in y:
            y = y[:-1]
        valid = []
        queue = []
        if check(x, y) == "yes":
            print("Can surf from {} to {}.".format(x, y))
        else:
            print("Can't surf from {} to {}.".format(x, y))
