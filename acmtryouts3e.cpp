#include <bits/stdc++.h>

using namespace std;
#define MAX 101
#define pii pair<int, int>
int moves[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int vis[MAX][MAX];
char grid[MAX][MAX];
vector<pii> shops, q, added;
pii start;
int main() {
    int m; cin >> m;
    for (int _ = 0; _ < m; _ += 1) {
        shops.clear();

        int r, c; cin >> r >> c;
        for (int i = 0; i < r; i += 1) {
            for (int j = 0; j < c; j += 1) {
                vis[i][j] = 696969;
                cin >> grid[i][j];
                if (grid[i][j] == 'S') shops.push_back({i, j});
                if (grid[i][j] == 'C') start = {i, j};
            }
        }

        vis[start.first][start.second] = 0;
        q.push_back(start);
        while (!q.empty()) {
            added.clear();
            for (pii tmp : q) {
                int a = tmp.first; int b = tmp.second;
                for (int w = 0; w < 4; w += 1) {
                    int x = moves[w][0] + a;
                    int y = moves[w][1] + b;
                    if (0 <= x && x < r && 0 <= y && y < c && grid[x][y] != '#' && vis[a][b] + 1 < vis[x][y]) {
                        vis[x][y] = vis[a][b] + 1;
                        added.push_back({x, y});
                    }
                }
            }
            q = added;
        }
        int s = 0; int maxm = 0;
        for (pii el : shops) {
            int tmp = vis[el.first][el.second];
            s += tmp;
            maxm = max(maxm, tmp);
        }
        cout << s * 2 - maxm + 60 * shops.size() << '\n';
    }
    return 0;
}