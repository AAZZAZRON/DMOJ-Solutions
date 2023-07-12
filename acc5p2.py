def dfs(tmp="", dep=0):
    global s, S, m
    if dep == 4:
        if s.find(tmp) != -1:
            m = min(m, 4 - len(tmp))
        return
    dfs(tmp, dep + 1)
    dfs(tmp + S[dep], dep + 1)


s = input()
S = "DMOJ"
m = 4
dfs()
print(m)
