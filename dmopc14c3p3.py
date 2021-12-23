import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline()[:-1]

people = [""] * 1001
skills = []
n = int(input())
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if people[score] == "":
        people[score] = name
    skills.append(score)
skills.sort()
for _ in range(int(input())):
    skill, adapt = [int(x) for x in input().split()]
    ind = bisect_left(skills, skill)
    if ind == n or skills[ind] - skill > adapt:
        person = "No suitable teacher!"
    else:
        person = people[skills[ind]]
    print(person)
