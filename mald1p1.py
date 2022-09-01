n = int(input())
websites = [input() for _ in range(n)]
ans = set()
for i in range(n):
    if "yubo" in websites[i]:
        ans.add(websites[max(0, i - 1)])
        ans.add(websites[i])
        ans.add(websites[min(n - 1, i + 1)])
[print(x) for x in sorted(list(ans))]