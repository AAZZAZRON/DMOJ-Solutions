from sys import stdin
input = stdin.readline


num = int(input())
relationships = {}
dM = {}
for i in range(num):
    m, d = input()[:-1].split()
    dM[d] = m
    if m not in relationships:
        relationships[m] = set()
    relationships[m].add(d)
for i in range(10):
    person = input()[:-1]
    grandmother = dM[dM[person]]
    cousins = 0
    for mother in relationships[grandmother]:
        if mother in relationships and mother != dM[person]:
            cousins += len(relationships[mother])
    sisters = len(relationships[dM[person]]) - 1
    print(f"Cousins: {cousins}, Sisters: {sisters}")
