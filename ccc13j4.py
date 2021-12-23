time = int(input())
num_chores = int(input())
chore_time = []
for i in range(0, num_chores):
    x = int(input())
    chore_time.append(x)
chore_time.sort()
q = 0
z = 0
while q <= time:
    q = q + chore_time[z]
    z += 1
print(z - 1)
